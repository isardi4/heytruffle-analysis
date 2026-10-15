#!/usr/bin/env python3
"""Clasifica evidencia guardada por empresa con OpenAI Responses API.

Modo predeterminado: dry-run, sin llamadas ni cargos. Con --run llama una vez
por bloque de evidencias, guarda caché por huella de entrada y regenera dos
CSV: etiquetas por evidencia e indicadores agregados por empresa.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from load_local_env import load_local_env
from llm_archivos import load_responses, save_requests, validate

load_local_env()

ROOT = Path(__file__).resolve().parents[1]
COMPANIES_DEFAULT = ROOT / "data/locales.csv"
EVIDENCE_DEFAULT = ROOT / "data/evidencia_llm_procesada.csv"
OUT_DEFAULT = ROOT / "data"
PROMPT_PATH = ROOT / "prompts/clasificar_evidencias.md"
API_URL = "https://api.openai.com/v1/responses"
MAX_TEXT_PER_EVIDENCE = 5000
TOPICS = ["phone_service_issue", "demand_peak", "phone_order_channel", "phone_inquiry_channel", "shared_staff_workload", "wait_or_capacity", "multi_location_context", "other", "none"]
STRENGTHS = ["direct", "indirect", "context", "none"]
SENTIMENTS = ["negative", "positive", "mixed", "neutral", "unclear"]
ATTRIBUTIONS = ["this_location", "company_wide", "other_location", "unclear"]

LABEL_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["labels"],
    "properties": {"labels": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["evidence_id", "topic", "strength", "sentiment", "attribution", "verbatim_quote", "rationale"],
        "properties": {
            "evidence_id": {"type": "string"},
            "topic": {"type": "string", "enum": TOPICS},
            "strength": {"type": "string", "enum": STRENGTHS},
            "sentiment": {"type": "string", "enum": SENTIMENTS},
            "attribution": {"type": "string", "enum": ATTRIBUTIONS},
            "verbatim_quote": {"type": "string"},
            "rationale": {"type": "string"},
        }}}},
}

EVIDENCE_OUTPUT_FIELDS = [
    "company_id", "location_id", "company_name", "location_label", "evidence_id",
    "source_type", "source_url", "published_at", "content_kind", "topic", "strength",
    "sentiment", "attribution", "verbatim_quote", "rationale", "is_phone_problem",
    "is_peak_demand", "is_phone_order_channel", "is_shared_workload", "is_wait_or_capacity",
    "model", "prompt_version", "prompt_sha256", "input_tokens", "output_tokens", "cache_hit",
]
INDICATOR_FIELDS = [
    "company_id", "company_name", "analysis_status", "locations_in_input", "evidence_count",
    "distinct_sources_count",
    "phone_problem_mentions", "direct_phone_problem_mentions", "phone_problem_locations",
    "phone_problem_locations_count", "indirect_phone_problem_locations_count", "peak_demand_mentions", "peak_demand_locations_count",
    "phone_order_channel_mentions", "phone_inquiry_channel_mentions", "shared_workload_mentions", "wait_or_capacity_mentions",
    "evidence_locations_count", "locations_with_any_evidence", "cross_location_phone_problem_pattern",
    "first_evidence_date", "latest_evidence_date", "evidence_readiness", "input_sha256", "model", "prompt_version",
    "prompt_sha256", "input_tokens", "output_tokens", "cached_chunks", "api_chunks",
    "evidence_labels_json",
]


def stable_hash(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def format_api_error(exc):
    if not isinstance(exc, HTTPError):
        return str(exc)
    try:
        body = json.loads(exc.read().decode("utf-8", errors="replace"))
        detail = body.get("error", {})
        message = detail.get("message", "")
        code = detail.get("code", "")
        parts = [f"HTTP {exc.code}"]
        if code:
            parts.append(f"code={code}")
        if message:
            parts.append(message)
        retry_after = exc.headers.get("Retry-After") if exc.headers else None
        if retry_after:
            parts.append(f"Retry-After={retry_after}")
        return ": ".join(parts)
    except (ValueError, AttributeError):
        return str(exc)


def project_id(prefix, *values):
    return prefix + "_" + stable_hash([str(v or "").strip().casefold() for v in values])[:12]


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def nonempty(row, *keys):
    return next((str(row.get(key, "")).strip() for key in keys if str(row.get(key, "")).strip()), "")


def prepare_companies(rows):
    companies = {}
    for row in rows:
        name = nonempty(row, "project_company_name", "Company Name", "company_name")
        if not name:
            continue
        cid = nonempty(row, "project_company_id", "company_id") or project_id("cmp", name)
        loc_id = nonempty(row, "project_location_id", "location_id") or project_id(
            "loc", cid, nonempty(row, "Company Street", "project_location_label"),
            nonempty(row, "Company City", "project_location_city"), nonempty(row, "Company State", "project_location_state"))
        loc = {"location_id": loc_id, "location_label": nonempty(row, "project_location_label", "Company Street"),
               "city": nonempty(row, "project_location_city", "Company City"),
               "state": nonempty(row, "project_location_state", "Company State")}
        if cid not in companies:
            companies[cid] = {"company_id": cid, "company_name": name, "profile": row, "locations": {}}
        companies[cid]["locations"][loc_id] = loc
    return companies


def prepare_evidence(rows, companies):
    by_name = {c["company_name"].casefold(): cid for cid, c in companies.items()}
    evidence_by_company = defaultdict(list)
    for index, row in enumerate(rows, 1):
        name = nonempty(row, "company_name", "project_company_name", "Company Name")
        cid = nonempty(row, "company_id", "project_company_id") or by_name.get(name.casefold(), "")
        if cid not in companies:
            continue
        # Accept captured original text or a claim paired with its exact quote.
        # Old prose summaries and search snippets are retained only for counts.
        original_text = nonempty(row, "source_text")
        source_quote = nonempty(row, "source_quote")
        extracted_claim = nonempty(row, "evidence_description") if source_quote else ""
        if extracted_claim and source_quote:
            content = f"EXTRACTED CLAIM (paraphrase): {extracted_claim}\nVALIDATED EXACT SOURCE QUOTE: {source_quote}"
            content_kind = "verified_extraction"
        elif original_text:
            content = original_text
            content_kind = "source_text"
        elif row.get("evidence_description", "").strip() or row.get("fact", "").strip():
            content = ""
            content_kind = "previous_summary"
        elif row.get("search_snippet", "").strip():
            content = ""
            content_kind = "search_snippet"
        else:
            content = ""
            content_kind = "empty"
        loc_id = nonempty(row, "location_id", "project_location_id")
        loc = companies[cid]["locations"].get(loc_id, {})
        evidence_id = nonempty(row, "evidence_id") or project_id("evi", cid, loc_id, row.get("source_url"), content, index)
        item = {"company_id": cid, "location_id": loc_id, "company_name": companies[cid]["company_name"],
                "location_label": nonempty(row, "location_label") or loc.get("location_label", ""),
                "evidence_id": evidence_id, "source_type": nonempty(row, "source_type"),
                "source_url": nonempty(row, "source_url"), "published_at": nonempty(row, "published_at"),
                "content_kind": content_kind, "content": content[:MAX_TEXT_PER_EVIDENCE],
                "source_domain": re.sub(r"^www\.", "", __import__("urllib.parse", fromlist=["urlparse"]).urlparse(nonempty(row, "source_url")).netloc.lower()),
                "provenance_note": nonempty(row, "provenance_note", "notes")}
        evidence_by_company[cid].append(item)
    return evidence_by_company


def api_call(api_key, model, company, items, prompt, timeout):
    payload_data = {
        "company": {"name": company["company_name"], "locations": list(company["locations"].values()),
                    "apollo_profile": company["profile"]},
        "evidence": [{k: item[k] for k in ("evidence_id", "location_id", "location_label", "source_type", "source_url", "published_at", "content_kind", "content", "provenance_note")} for item in items],
    }
    payload = {"model": model,
        "instructions": prompt,
        "input": json.dumps(payload_data, ensure_ascii=False),
        "text": {"format": {"type": "json_schema", "name": "evidence_classification", "strict": True, "schema": LABEL_SCHEMA}},
        "max_output_tokens": max(1200, 180 * len(items)),
        "store": False,
    }
    request = Request("https://api.openai.com/v1/responses", data=json.dumps(payload).encode("utf-8"),
                      headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}, method="POST")
    with urlopen(request, timeout=timeout) as response:
        result = json.load(response)
    output_text = "".join(content.get("text", "") for output in result.get("output", [])
                          if output.get("type") == "message" for content in output.get("content", [])
                          if content.get("type") == "output_text")
    if not output_text:
        raise ValueError(f"API no devolvió texto de salida; status={result.get('status')}")
    parsed = json.loads(output_text)
    labels = parsed.get("labels", [])
    expected = {item["evidence_id"] for item in items}
    returned = [label.get("evidence_id") for label in labels]
    if set(returned) != expected or len(returned) != len(expected):
        raise ValueError("La respuesta no contiene exactamente una clasificación por evidence_id de entrada")
    source_by_id = {item["evidence_id"]: item["content"] for item in items}
    for label in labels:
        quote = label.get("verbatim_quote", "")
        if label['strength'] in {'direct','indirect'} and label['topic'] != 'none' and not quote:
            raise ValueError('Una señal directa o indirecta requiere una cita no vacía')
        if quote and quote not in source_by_id[label["evidence_id"]]:
            raise ValueError("La clasificación devolvió una cita que no aparece literalmente en su evidencia")
    usage = result.get("usage", {})
    return labels, {"response_id": result.get("id", ""), "input_tokens": usage.get("input_tokens", 0),
                    "output_tokens": usage.get("output_tokens", 0)}


def make_chunks(items, chunk_size):
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def classify(companies, evidence_by_company, out_dir, model, prompt, prompt_hash, run_enabled, max_companies, offset, chunk_size, timeout, delay, external=None, request_records=None):
    selected = list(companies.items())[offset:offset + max_companies]
    cache_dir = out_dir / ".pipeline" / "classification_cache"
    labels_by_company, usage_by_company, cache_stats, errors = {}, {}, {}, {}
    prompt_version = re.search(r"Versión:\s*`([^`]+)`", prompt).group(1) if re.search(r"Versión:\s*`([^`]+)`", prompt) else "unversioned"
    for cid, company in selected:
        all_items = evidence_by_company.get(cid, [])
        items = [item for item in all_items if item["content_kind"] in {"source_text", "verified_extraction"}]
        if not items:
            labels_by_company[cid], usage_by_company[cid], cache_stats[cid] = [], {"input_tokens": 0, "output_tokens": 0}, {"cached": 0, "api": 0}
            continue
        company_labels, total_usage, cached_count, api_count = [], {"input_tokens": 0, "output_tokens": 0}, 0, 0
        for chunk_index, chunk in enumerate(make_chunks(items, chunk_size)):
            fingerprint = stable_hash({"model": model, "prompt": prompt_hash, "company": company["company_name"], "items": chunk})
            if request_records is not None:
                request_records.append({'request_id': fingerprint, 'company_id': cid, 'company_name': company['company_name'], 'chunk': chunk_index,
                    'input': {'company': {'name': company['company_name'], 'locations': list(company['locations'].values()), 'apollo_profile': company['profile']},
                              'evidence': [{k: item[k] for k in ('evidence_id','location_id','location_label','source_type','source_url','published_at','content_kind','content','provenance_note')} for item in chunk]}})
            safe_cid = re.sub(r"[^A-Za-z0-9_-]", "_", cid)
            cache_path = cache_dir / f"{safe_cid}_{chunk_index}_{fingerprint[:16]}.json"
            if external is not None:
                if fingerprint not in external:
                    raise ValueError(f'Falta respuesta Codex para {cid}, bloque {chunk_index}')
                response = external[fingerprint]
                validate(response, LABEL_SCHEMA)
                labels, usage = response['labels'], {}
                expected = {item['evidence_id']: item['content'] for item in chunk}
                if len(labels) != len(expected) or {r['evidence_id'] for r in labels} != set(expected):
                    raise ValueError('Codex debe clasificar cada evidence_id exactamente una vez')
                for label in labels:
                    if label['strength'] in {'direct','indirect'} and label['topic'] != 'none' and not label['verbatim_quote']:
                        raise ValueError('Una señal directa o indirecta requiere una cita no vacía')
                    if label['verbatim_quote'] and label['verbatim_quote'] not in expected[label['evidence_id']]:
                        raise ValueError('Cita Codex no encontrada en su evidencia')
            elif cache_path.exists():
                cached = json.loads(cache_path.read_text(encoding="utf-8"))
                labels, usage = cached["labels"], cached["usage"]
                cached_count += 1
            elif run_enabled:
                try:
                    labels, usage = api_call(os.environ["OPENAI_API_KEY"], model, company, chunk, prompt, timeout)
                    cache_path.parent.mkdir(parents=True, exist_ok=True)
                    cache_path.write_text(json.dumps({"labels": labels, "usage": usage, "model": model,
                        "prompt_version": prompt_version, "prompt_sha256": prompt_hash}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                    api_count += 1
                    time.sleep(delay)
                except (HTTPError, URLError, TimeoutError, ValueError, KeyError) as exc:
                    errors[cid] = format_api_error(exc)
                    break
            else:
                continue
            company_labels.extend(labels)
            total_usage["input_tokens"] += usage.get("input_tokens", 0)
            total_usage["output_tokens"] += usage.get("output_tokens", 0)
        labels_by_company[cid] = company_labels
        usage_by_company[cid] = total_usage
        cache_stats[cid] = {"cached": cached_count, "api": api_count}
        state = "error" if cid in errors else ("done" if len(company_labels) == len(items) else "pending")
        print(f"{cid}: {state}; {len(items)} evidencias; {cached_count} bloques en caché; {api_count} llamadas API" + (f"; error={errors[cid]}" if cid in errors else ""))
    return selected, labels_by_company, usage_by_company, cache_stats, errors, prompt_version


def build_outputs(companies, evidence_by_company, selected, labels_by_company, usage_by_company, cache_stats, errors, model, prompt_version, prompt_hash, out_dir):
    evidence_rows, indicator_rows = [], []
    selected_ids = {cid for cid, _ in selected}
    for cid, company in companies.items():
        items = evidence_by_company.get(cid, [])
        analyzable_items = [item for item in items if item["content_kind"] in {"source_text", "verified_extraction"}]
        labels = {row["evidence_id"]: row for row in labels_by_company.get(cid, [])}
        usage, stats = usage_by_company.get(cid, {}), cache_stats.get(cid, {"cached": 0, "api": 0})
        for item in items:
            label = labels.get(item["evidence_id"])
            if not label:
                continue
            topic, strength = label["topic"], label["strength"]
            evidence_rows.append({**{k: item.get(k, "") for k in ("company_id", "location_id", "company_name", "location_label", "evidence_id", "source_type", "source_url", "published_at", "content_kind")},
                **label,
                "is_phone_problem": str(topic == "phone_service_issue" and strength in {"direct", "indirect"}).lower(),
                "is_peak_demand": str(topic == "demand_peak" and strength != "none").lower(),
                "is_phone_order_channel": str(topic == "phone_order_channel" and strength != "none").lower(),
                "is_shared_workload": str(topic == "shared_staff_workload" and strength != "none").lower(),
                "is_wait_or_capacity": str(topic == "wait_or_capacity" and strength != "none").lower(),
                "model": model, "prompt_version": prompt_version, "prompt_sha256": prompt_hash,
                "input_tokens": "", "output_tokens": "", "cache_hit": ""})
        matched = [(item, labels.get(item["evidence_id"])) for item in items if labels.get(item["evidence_id"])]
        unique = {}
        for item, label in matched:
            fp = stable_hash([item.get("source_url", ""), re.sub(r"\W+", " ", item.get("content", "").casefold()).strip()])
            unique.setdefault(fp, (item, label))
        unique_rows = list(unique.values())
        phone = [(i, l) for i, l in unique_rows if l["topic"] == "phone_service_issue" and l["strength"] in {"direct", "indirect"}]
        direct_phone = [(i, l) for i, l in phone if l["strength"] == "direct"]
        phone_locs = {i["location_id"] for i, l in direct_phone if i.get("location_id") and l["attribution"] == "this_location"}
        indirect_phone_locs = {i["location_id"] for i, l in phone if l["strength"] == "indirect" and i.get("location_id") and l["attribution"] == "this_location"}
        peak = [(i, l) for i, l in unique_rows if l["topic"] == "demand_peak" and l["strength"] != "none"]
        peak_locs = {i["location_id"] for i, l in peak if i.get("location_id") and l["attribution"] == "this_location"}
        phone_orders = [x for x in unique_rows if x[1]["topic"] == "phone_order_channel" and x[1]["strength"] != "none"]
        phone_inquiries = [x for x in unique_rows if x[1]['topic'] == 'phone_inquiry_channel' and x[1]['strength'] != 'none']
        workload = [x for x in unique_rows if x[1]["topic"] == "shared_staff_workload" and x[1]["strength"] != "none"]
        capacity = [x for x in unique_rows if x[1]["topic"] == "wait_or_capacity" and x[1]["strength"] != "none"]
        evidence_locs = {i["location_id"] for i, _ in matched if i.get("location_id")}
        reviewable = cid in selected_ids and cid not in errors and len(labels) == len(analyzable_items)
        if not analyzable_items:
            readiness = "no_source_text_captured"
        elif not reviewable:
            readiness = "analysis_incomplete" if cid in selected_ids else "not_processed"
        elif direct_phone:
            readiness = "direct_phone_issue_signal"
        elif phone or peak or phone_orders or phone_inquiries or workload or capacity:
            readiness = "operational_context_only"
        else:
            readiness = "no_relevant_public_signal"
        if len(phone_locs) >= 2:
            repeated = "yes_multiple_locations"
        elif phone:
            repeated = "one_location_only"
        else:
            repeated = "no_phone_issue_signal"
        if phone and not phone_locs and not indirect_phone_locs:
            repeated = "company_level_or_location_unclear"
        dates = sorted(i["published_at"][:10] for i, _ in matched if re.match(r"^\d{4}-\d{2}-\d{2}", i.get("published_at", "")))
        indicator_rows.append({"company_id": cid, "company_name": company["company_name"],
            "analysis_status": "error" if cid in errors else ("awaiting_source_text" if not analyzable_items else ("complete" if reviewable else "not_processed")),
            "locations_in_input": len(company["locations"]), "evidence_count": len(items),
            "distinct_sources_count": len({i["source_domain"] for i, _ in matched if i.get("source_domain")}),
            "phone_problem_mentions": len(phone), "direct_phone_problem_mentions": len(direct_phone),
            "phone_problem_locations": "|".join(sorted(phone_locs)), "phone_problem_locations_count": len(phone_locs),
            "indirect_phone_problem_locations_count": len(indirect_phone_locs),
            "peak_demand_mentions": len(peak), "peak_demand_locations_count": len(peak_locs),
            "phone_order_channel_mentions": len(phone_orders), "phone_inquiry_channel_mentions": len(phone_inquiries), "shared_workload_mentions": len(workload),
            "wait_or_capacity_mentions": len(capacity), "evidence_locations_count": len(evidence_locs),
            "locations_with_any_evidence": "|".join(sorted(evidence_locs)),
            "cross_location_phone_problem_pattern": repeated, "first_evidence_date": dates[0] if dates else "",
            "latest_evidence_date": dates[-1] if dates else "", "evidence_readiness": readiness,
            "input_sha256": stable_hash({"company": company["company_name"], "locations": list(company["locations"].values()), "evidence": items}),
            "model": model, "prompt_version": prompt_version, "prompt_sha256": prompt_hash,
            "input_tokens": usage.get("input_tokens", 0), "output_tokens": usage.get("output_tokens", 0),
            "cached_chunks": stats["cached"], "api_chunks": stats["api"],
            "error": errors.get(cid, "")})
    labels_by_cid = defaultdict(list)
    for row in evidence_rows:
        labels_by_cid[row["company_id"]].append({key: row.get(key, "") for key in (
            "evidence_id", "location_id", "source_type", "source_url", "topic", "strength",
            "sentiment", "attribution", "verbatim_quote", "rationale")})
    for row in indicator_rows:
        row["evidence_labels_json"] = json.dumps(labels_by_cid[row["company_id"]], ensure_ascii=False, separators=(",", ":"))
    output_path = out_dir / "resultados_evidencia_llm.csv"
    prior_rows = read_csv(output_path) if output_path.exists() else []
    current_by_id = {row["company_id"]: row for row in indicator_rows}
    valid_prior = {row["company_id"]: row for row in prior_rows
                   if row.get("company_id") in current_by_id
                   and row.get("model") == model and row.get("prompt_sha256") == prompt_hash
                   and row.get("input_sha256") == current_by_id[row["company_id"]].get("input_sha256")}
    merged_rows = []
    for row in indicator_rows:
        if row["company_id"] not in selected_ids and row["company_id"] in valid_prior:
            merged_rows.append(valid_prior[row["company_id"]])
        else:
            merged_rows.append(row)
    write_csv(output_path, INDICATOR_FIELDS + ["error"], merged_rows)
    print(f"Salida: {output_path} ({len(merged_rows)} empresas; incluye indicadores y evidencia etiquetada como JSON)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--companies", type=Path, default=COMPANIES_DEFAULT)
    parser.add_argument("--evidence", type=Path, default=EVIDENCE_DEFAULT)
    parser.add_argument("--out-dir", type=Path, default=OUT_DEFAULT)
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", ""), help="Modelo API; o configurar OPENAI_MODEL.")
    parser.add_argument("--max-companies", type=int, default=30, help="Límite seguro por corrida (default 30; usar 5700 para lote completo).")
    parser.add_argument("--offset", type=int, default=0, help="Índice inicial para correr por lotes.")
    parser.add_argument("--chunk-size", type=int, default=25, help="Evidencias máximas por solicitud de análisis.")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--delay", type=float, default=0.2)
    parser.add_argument("--run", action="store_true", help="Ejecuta llamadas al API. Sin esta opción solo hace dry-run y lee la caché.")
    parser.add_argument('--responses', type=Path, help='Respuestas JSON nuevas de Codex; no llama API.')
    parser.add_argument('--requests', type=Path, help='Exporta prompts y entradas exactas para Codex.')
    args = parser.parse_args()
    if args.run and args.responses:
        raise SystemExit('Elegir API o respuestas de archivos, no ambos.')
    external = load_responses(args.responses) if args.responses else None
    request_records = []
    if args.max_companies < 1 or args.offset < 0 or not 1 <= args.chunk_size <= 100:
        raise SystemExit("Revisá --max-companies, --offset y --chunk-size (1 a 100).")
    company_rows, evidence_rows = read_csv(args.companies), read_csv(args.evidence)
    companies = prepare_companies(company_rows)
    if not companies:
        raise SystemExit("No hay empresas con nombre para analizar.")
    evidence_by_company = prepare_evidence(evidence_rows, companies)
    prompt = PROMPT_PATH.read_text(encoding="utf-8")
    prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    model = args.model or "(configurar OPENAI_MODEL)"
    if args.run and not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("--run requiere OPENAI_API_KEY; no se hizo ninguna llamada.")
    if args.run and not args.model:
        raise SystemExit("--run requiere --model o OPENAI_MODEL para hacer reproducible la selección del modelo.")
    selected_count = min(args.max_companies, max(0, len(companies) - args.offset))
    selected_companies = list(companies.items())[args.offset:args.offset + args.max_companies]
    evidence_count = sum(len(evidence_by_company.get(cid, [])) for cid, _ in selected_companies)
    analyzable_count = sum(sum(item["content_kind"] in {"source_text", "verified_extraction"} for item in evidence_by_company.get(cid, [])) for cid, _ in selected_companies)
    chunks = sum((sum(item["content_kind"] in {"source_text", "verified_extraction"} for item in evidence_by_company.get(cid, [])) + args.chunk_size - 1) // args.chunk_size for cid, _ in selected_companies)
    print(f"Empresas: {len(companies)}; lote: {selected_count}; registros de evidencia: {evidence_count}; evidencias analizables: {analyzable_count}; bloques estimados: {chunks}")
    if args.responses:
        print('CODEX POR ARCHIVOS: validación de respuestas nuevas guardadas; sin llamadas API.')
    elif args.run:
        print(f"OpenAI API habilitada; modelo={model}. Se guardará caché para reanudar sin repetir llamadas.")
    else:
        print("DRY-RUN: sin llamadas ni consumo de API. Agregación para entradas en caché y estado pendiente para el resto.")
    selected, labels, usage, stats, errors, prompt_version = classify(companies, evidence_by_company, args.out_dir,
        model, prompt, prompt_hash, args.run, args.max_companies, args.offset, args.chunk_size, args.timeout, args.delay, external, request_records)
    build_outputs(companies, evidence_by_company, selected, labels, usage, stats, errors, model, prompt_version, prompt_hash, args.out_dir)
    # Una extracción completada sin afirmaciones no equivale a falta de texto.
    extraction_status = args.out_dir / '.pipeline' / 'estado_extraccion_llm.csv'
    if extraction_status.exists():
        reviewed_empty = {r['company_id'] for r in read_csv(extraction_status)
            if r.get('model') == model and r.get('extraction_status') in {
                'sin_evidencia_relevante_con_codex', 'sin_evidencia_relevante', 'sin_evidencia_relevante_en_cache'}}
        result_path = args.out_dir / 'resultados_evidencia_llm.csv'
        result_rows = read_csv(result_path)
        for row in result_rows:
            if row['company_id'] in reviewed_empty and row['analysis_status'] == 'awaiting_source_text':
                row['analysis_status'] = 'complete'
                row['evidence_readiness'] = 'no_relevant_public_signal'
        write_csv(result_path, INDICATOR_FIELDS + ['error'], result_rows)
    save_requests(args.requests, prompt, LABEL_SCHEMA, request_records)


if __name__ == "__main__":
    try:
        main()
    except (OSError, csv.Error, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
