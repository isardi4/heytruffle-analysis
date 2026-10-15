#!/usr/bin/env python3
"""Prepara búsquedas y reúne documentos fuente para cada local.

El script no inventa evidencia ni intenta saltar bloqueos de sitios. En modo
normal crea una hoja de búsqueda por local/fuente. Con --results descarga las
URLs halladas por el investigador y guarda texto fuente con trazabilidad.
No persiste reseñas de Google Places, cuyas condiciones restringen su exportación.
"""
import argparse
import csv
import hashlib
import html
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.parse import urljoin, urldefrag
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
LOCATIONS_DEFAULT = ROOT / "data/locales.csv"
EVIDENCE_DEFAULT = ROOT / "data/evidencia_locales.csv"
OUTPUT_DEFAULT = ROOT / "data"
SOURCES = {
    "sitio_oficial": '"{name}" "{city}" "{state}" official menu phone orders hours',
    "avisos_empleo": '"{name}" "{city}" "{state}" (phone OR "phone orders") (restaurant jobs OR careers)',
    "resenas_cliente": '"{name}" "{city}" "{state}" (Yelp OR Tripadvisor OR DoorDash OR Uber Eats) (phone OR wait OR busy)',
    "noticias_comunidad": '"{name}" "{city}" "{state}" (news OR Reddit) (phone OR calls OR rush OR wait)',
}
PLAN_FIELDS = ["query_id", "company_id", "location_id", "company_name", "location_label", "city", "state", "source_type", "search_query", "status", "notes"]
RESULT_FIELDS = ["query_id", "source_type", "source_url", "published_at", "author", "location_match", "notes"]
OUTPUT_FIELDS = ["query_id", "search_query", "evidence_id", "company_id", "location_id", "company_name", "location_label", "source_type", "source_url", "captured_at", "published_at", "author", "location_match", "matched_address", "document_title", "search_snippet", "source_text", "collection_status", "notes"]


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
        self.title = False
        self.title_parts = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.extend(value for key, value in attrs if key == 'href' and value)
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip += 1
        if tag == "title":
            self.title = True

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript", "svg"} and self.skip:
            self.skip -= 1
        if tag == "title":
            self.title = False

    def handle_data(self, data):
        if self.title:
            self.title_parts.append(data)
        if not self.skip:
            cleaned = re.sub(r"\s+", " ", data).strip()
            if cleaned:
                self.parts.append(cleaned)


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        return list(reader)


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def stable_id(*values):
    return "evsrc_" + hashlib.sha256("\x1f".join(map(str, values)).encode()).hexdigest()[:14]


def project_id(prefix, *values):
    raw = "\x1f".join(str(value or "").strip().casefold() for value in values)
    return prefix + "_" + hashlib.sha256(raw.encode()).hexdigest()[:12]


def normalize_apollo_rows(rows):
    """Allow a raw Apollo account export; its address is only a search hint."""
    normalized_rows = []
    for row in rows:
        name = (row.get("Company Name") or "").strip()
        if not name:
            continue
        city, state = (row.get("Company City") or "").strip(), (row.get("Company State") or "").strip()
        street = (row.get("Company Street") or "").strip()
        account_key = row.get("Apollo Account Id") or row.get("Apollo Record Id") or ""
        cid = project_id("cmp", name)
        lid = project_id("loc", account_key or name, street, city, state)
        loc_label = " · ".join(part for part in (street, city, state) if part)
        if not loc_label:
            loc_label = "Ubicación de cuenta Apollo no validada"
        normalized_rows.append({
            **row,
            "project_company_id": cid,
            "project_location_id": lid,
            "project_company_name": name,
            "project_location_label": loc_label,
            "project_location_city": city,
            "project_location_state": state,
            "project_location_phone": row.get("Company Phone", ""),
            "project_verified_location_count": row.get("Number of Retail Locations", ""),
            "project_origin": "apollo_export_sin_normalizar",
            "_apollo_location_unverified": "true",
        })
    return normalized_rows


def build_plan(locations, evidence):
    # Existing evidence URLs are carried forward as fetch tasks; other source
    # families get a query to run and cite, rather than fabricated results.
    by_location = {}
    for item in evidence:
        by_location.setdefault(item.get("location_id", ""), []).append(item)
    tasks = []
    for loc in locations:
        cid, lid = loc["project_company_id"], loc["project_location_id"]
        name = loc.get("project_company_name") or loc.get("Company Name", "")
        city, state = loc.get("project_location_city", ""), loc.get("project_location_state", "")
        label = loc.get("project_location_label", "")
        existing = by_location.get(lid, [])
        for source, template in SOURCES.items():
            matches = [row for row in existing if row.get("source_type") == source and row.get("source_url")]
            if matches:
                unique_urls = sorted({row["source_url"] for row in matches})
                for url in unique_urls:
                    prior = next((row for row in matches if row.get("source_url") == url), {})
                    tasks.append({"query_id": prior.get("query_id") or stable_id(cid, lid, source, url), "company_id": cid, "location_id": lid,
                        "company_name": name, "location_label": label, "city": city, "state": state,
                        "source_type": source, "search_query": url, "status": "url_previamente_documentada",
                        "notes": "URL heredada de evidencia previa; el resumen previo no equivale a texto original."})
            else:
                query = template.format(name=name, city=city, state=state)
                note = "Registrar URL original; un snippet de buscador no se acepta como evidencia."
                if loc.get("_apollo_location_unverified"):
                    note += " Dirección de Apollo es solo referencia de cuenta; validar sucursal exacta antes de atribuir evidencia."
                tasks.append({"query_id": stable_id(cid, lid, source, query), "company_id": cid, "location_id": lid,
                    "company_name": name, "location_label": label, "city": city, "state": state,
                    "source_type": source, "search_query": query, "status": "pendiente_busqueda", "notes": note})
    return tasks


def fetch_document(url, timeout):
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("URL debe comenzar con http:// o https://")
    req = Request(url, headers={"User-Agent": "heytruffle-evidence-research/1.0 (research; contact: project owner)"})
    with urlopen(req, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        body = response.read(5_000_000)
        charset = response.headers.get_content_charset() or "utf-8"
    if "html" not in content_type and "text/plain" not in content_type:
        return "", f"Tipo de contenido no textual: {content_type}", []
    parser = TextExtractor()
    parser.feed(body.decode(charset, errors="replace"))
    title = " ".join(parser.title_parts).strip()
    text = html.unescape(" ".join(parser.parts))
    links = list(dict.fromkeys(urldefrag(urljoin(url, href))[0] for href in parser.links))
    return (title + "\n" + text).strip(), "", links


def fetch_page(url, timeout):
    text, note, _ = fetch_document(url, timeout)
    return text, note


def focus_passages(text, limit=3500):
    """Selección de pasajes literales; no genera afirmaciones ni etiquetas."""
    if len(text) <= limit:
        return text
    spans = [(0, min(550, len(text)))]
    pattern = r'phone|call|busiest|busy|peak|rush|host|cashier|take.?out|to.?go|wait|capacity|locations|pizza|barbecue|taco'
    for match in re.finditer(pattern, text, re.I):
        start, end = max(0, match.start()-100), min(len(text), match.end()+240)
        if spans and start <= spans[-1][1]:
            spans[-1] = (spans[-1][0], max(end, spans[-1][1]))
        else:
            spans.append((start, end))
    output = ''
    for start, end in spans:
        room = limit - len(output) - 7
        if room <= 0:
            break
        output += ('\n[...]\n' if output else '') + text[start:min(end,start+room)]
    return output


def source_family(url):
    host = urlparse(url).netloc.lower().removeprefix('www.')
    return 'plataforma_pedidos_tercera' if any(host == d or host.endswith('.'+d) for d in ('doordash.com','ubereats.com','grubhub.com')) else 'sitio_oficial'


def collect_official(locations, output_dir, timeout, max_pages, workers):
    """Arranca SOLO de Website de locales y sigue enlaces explícitos del sitio."""
    def one(loc):
        cid = loc.get('project_company_id') or loc.get('company_id')
        lid = loc.get('project_location_id') or loc.get('location_id')
        name = loc.get('project_company_name') or loc.get('company_name') or loc.get('Company Name')
        website = (loc.get('Website') or loc.get('website') or '').strip()
        if website and not website.startswith(('http://','https://')):
            website = 'https://' + website
        pending, seen, results = ([website] if website else []), set(), []
        while pending and len(results) < max_pages:
            url = pending.pop(0)
            if url in seen:
                continue
            seen.add(url)
            qid = stable_id(cid, lid, 'sitio_oficial', url)
            text, links, error = '', [], ''
            try:
                text, error, links = fetch_document(url, timeout)
                status = 'capturado' if text else 'sin_texto'
            except (OSError, ValueError) as exc:
                status, error = 'fallo_descarga', str(exc)
            if text:
                raw = output_dir / 'textos_originales' / (qid + '.txt')
                raw.parent.mkdir(parents=True, exist_ok=True)
                raw.write_text(text, encoding='utf-8')
            results.append({'query_id': qid, 'evidence_id': qid, 'company_id': cid, 'location_id': lid,
                'company_name': name, 'location_label': loc.get('project_location_label') or loc.get('location_label',''),
                'source_type': source_family(url), 'source_url': url,
                'captured_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                'published_at': '', 'author': '', 'location_match': 'sucursal_o_cadena_por_confirmar',
                'matched_address': '', 'document_title': text.split('\n')[0] if text else '',
                'search_query': website, 'search_snippet': '', 'source_text': focus_passages(text),
                'collection_status': status,
                'notes': 'Adquisición nueva desde Website del único archivo de entrada. Pasajes literales seleccionados por palabras clave (máximo 3500 caracteres); texto completo en textos_originales/'+qid+'.txt. Cobertura parcial, no ausencia de problemas. '+error})
            host = urlparse(website).netloc.lower().removeprefix('www.')
            candidates = []
            for link in links:
                parsed = urlparse(link)
                if parsed.scheme not in {'http','https'} or parsed.netloc.lower().removeprefix('www.') != host or link in seen:
                    continue
                path = parsed.path.lower()
                score = 100 if re.search(r'faq|frequent|important.info',path) else 80 if re.search(r'career|jobs|employment',path) else 60 if re.search(r'contact|order|location',path) else 0
                if score and not re.search(r'\.(pdf|jpg|png|zip)$',path):
                    candidates.append((-score, link))
            pending = list(dict.fromkeys([link for _,link in sorted(candidates)] + pending))
        print(f'{name}: {len(results)} páginas; {sum(bool(r["source_text"]) for r in results)} con texto', flush=True)
        return results
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return [row for group in pool.map(one, locations) for row in group]


def collect_results(tasks, results, timeout, delay):
    task_by_id = {task["query_id"]: task for task in tasks}
    output = []
    for result in results:
        qid = result.get("query_id", "")
        task = task_by_id.get(qid)
        if not task:
            raise ValueError(f"query_id no encontrado en el plan: {qid}")
        url = result.get("source_url", "").strip()
        if not url:
            continue
        try:
            text, note = fetch_page(url, timeout)
            status = "capturado" if text else "sin_texto"
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            text, status, note = "", "fallo_descarga", str(exc)
        output.append({"query_id": qid, "search_query": task["search_query"], "evidence_id": stable_id(qid, url), "company_id": task["company_id"], "location_id": task["location_id"],
            "company_name": task["company_name"], "location_label": task["location_label"],
            "source_type": result.get("source_type") or task["source_type"], "source_url": url,
            "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "published_at": result.get("published_at", ""), "author": result.get("author", ""),
            "location_match": result.get("location_match", "por_confirmar"), "matched_address": "",
            "document_title": text.split("\n", 1)[0] if text else "",
            "search_snippet": result.get("search_snippet", ""),
            "source_text": text[:30000], "collection_status": status,
            "notes": "; ".join(filter(None, [result.get("notes", ""), note]))})
        time.sleep(delay)
    return output


def brave_search(tasks, api_key, max_searches, start_at, timeout, delay):
    """Search pending source tasks using Brave Search API; no browser scraping."""
    all_pending = [task for task in tasks if task["status"] == "pendiente_busqueda"]
    pending = all_pending[start_at:start_at + max_searches]
    results = []
    for task in pending:
        query = urlencode({"q": task["search_query"], "count": 5})
        req = Request("https://api.search.brave.com/res/v1/web/search?" + query,
            headers={"Accept": "application/json", "X-Subscription-Token": api_key,
                     "User-Agent": "heytruffle-evidence-research/1.0"})
        with urlopen(req, timeout=timeout) as response:
            data = json.load(response)
        for item in (data.get("web") or {}).get("results", []):
            results.append({"query_id": task["query_id"], "source_type": task["source_type"],
                "source_url": item.get("url", ""), "published_at": item.get("page_age", ""),
                "author": "", "location_match": "por_confirmar",
                "notes": "Resultado de Brave Search; verificar identidad y localidad antes de usar.",
                "search_snippet": item.get("description", "")})
        time.sleep(delay)
    return results, len(pending)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locations", type=Path, default=LOCATIONS_DEFAULT)
    parser.add_argument("--evidence", type=Path, default=EVIDENCE_DEFAULT)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DEFAULT)
    parser.add_argument("--results", type=Path, help="CSV de URLs halladas usando el plan; columnas: " + ", ".join(RESULT_FIELDS))
    parser.add_argument("--brave-search", action="store_true", help="Busca URLs automáticamente. Requiere BRAVE_SEARCH_API_KEY; puede consumir crédito del proveedor.")
    parser.add_argument("--max-searches", type=int, default=20, help="Máximo de consultas Brave por ejecución (predeterminado: 20).")
    parser.add_argument("--start-at", type=int, default=0, help="Índice inicial de tarea pendiente Brave para procesar en lotes.")
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument('--discover-official', action='store_true', help='Descubre páginas desde Website, sin API de búsqueda ni fuentes heredadas.')
    parser.add_argument('--max-pages', type=int, default=3)
    parser.add_argument('--workers', type=int, default=6)
    args = parser.parse_args()
    locations = read_csv(args.locations)
    evidence = read_csv(args.evidence) if args.evidence.exists() else []
    if locations and not locations[0].get("project_location_id"):
        if locations[0].get("location_id"):
            locations = [{**row,
                "project_company_id": row.get("company_id", ""),
                "project_location_id": row.get("location_id", ""),
                "project_company_name": row.get("company_name") or row.get("Company Name", ""),
                "project_location_label": row.get("location_label", ""),
                "project_location_city": row.get("city", ""),
                "project_location_state": row.get("state", ""),
                "project_location_phone": row.get("phone", ""),
            } for row in locations]
        else:
            locations = normalize_apollo_rows(locations)
        if not locations:
            raise SystemExit("El export de Apollo no contiene filas con Company Name")
    if not locations:
        raise SystemExit("El archivo de locales está vacío")
    loc_ids = {row.get("project_location_id") for row in locations}
    if None in loc_ids or "" in loc_ids or len(loc_ids) != len(locations):
        raise SystemExit("Faltan IDs de local o hay IDs duplicados")
    plan = build_plan(locations, evidence)
    old_rows = read_csv(args.evidence) if args.evidence.exists() else []
    by_query = {row.get("query_id"): row for row in old_rows if row.get("query_id")}
    old_by_source = {(row.get("company_id"), row.get("location_id"), row.get("source_type"), row.get("source_url")): row
                     for row in old_rows if row.get("source_url")}
    manifest = []
    for task in plan:
        prior = by_query.get(task["query_id"]) or old_by_source.get((task["company_id"], task["location_id"], task["source_type"], task["search_query"]), {})
        manifest.append({**prior, "query_id": task["query_id"], "search_query": task["search_query"],
            "evidence_id": prior.get("evidence_id") or task["query_id"],
            "company_id": task["company_id"], "location_id": task["location_id"],
            "company_name": task["company_name"], "location_label": task["location_label"],
            "source_type": task["source_type"],
            "source_url": prior.get("source_url") or (task["search_query"] if task["status"] == "url_previamente_documentada" else ""),
            "collection_status": prior.get("collection_status") or task["status"],
            "notes": prior.get("notes") or task["notes"]})
    write_csv(args.evidence, OUTPUT_FIELDS, manifest)
    print(f"Plan actualizado en {args.evidence} ({len(manifest)} tareas). No se realizaron búsquedas externas.")
    collected = []
    if args.discover_official:
        if args.max_pages < 1 or args.workers < 1:
            raise SystemExit('max-pages y workers deben ser positivos')
        collected.extend(collect_official(locations, args.output_dir, args.timeout, args.max_pages, args.workers))
    if args.results:
        results = read_csv(args.results)
        collected.extend(collect_results(plan, results, args.timeout, args.delay))
    if args.brave_search:
        key = os.environ.get("BRAVE_SEARCH_API_KEY")
        if not key:
            raise SystemExit("Definiste --brave-search pero falta BRAVE_SEARCH_API_KEY; no se hizo consulta.")
        if args.max_searches < 1 or args.start_at < 0:
            raise SystemExit("--max-searches debe ser mayor que cero y --start-at no puede ser negativo.")
        web_results, searched = brave_search(plan, key, args.max_searches, args.start_at, args.timeout, args.delay)
        print(f"Brave Search ejecutó {searched} consultas (límite configurado: {args.max_searches}) y devolvió {len(web_results)} URLs.")
        collected.extend(collect_results(plan, web_results, args.timeout, args.delay))
    if collected:
        page_path = args.output_dir / "evidencia_locales.csv"
        existing = read_csv(page_path) if page_path.exists() else []
        by_id = {row.get("query_id") or row.get("evidence_id"): row for row in existing}
        by_id.update({row.get("query_id") or row.get("evidence_id"): row for row in collected})
        write_csv(page_path, OUTPUT_FIELDS, list(by_id.values()))
        print(f"Páginas y fuentes guardadas: {page_path} ({len(collected)} nuevas/actualizadas).")
    print("Las páginas capturadas son documentos fuente, no etiquetas ni conclusiones. El análisis/atribución queda para la etapa LLM y revisión humana.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, csv.Error, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
