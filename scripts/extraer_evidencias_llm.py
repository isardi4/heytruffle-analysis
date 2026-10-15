#!/usr/bin/env python3
"""Usa un LLM para convertir documentos fuente capturados en evidencia atómica.

Solo procesa source_text original. Resúmenes previos y snippets no se envían.
Modo predeterminado: dry-run. --run habilita llamadas pagas al OpenAI API.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from load_local_env import load_local_env
from llm_archivos import load_responses, save_requests, validate

load_local_env()

ROOT = Path(__file__).resolve().parents[1]
INPUT_DEFAULT = ROOT / "data/evidencia_locales.csv"
REVIEWS_DEFAULT = ROOT / "data/evidencia_resenas.csv"
OUT_DEFAULT = ROOT / "data"
PROMPT_PATH = ROOT / "prompts/extraer_evidencias.md"
CHUNK_SIZE = 14000
CHUNK_OVERLAP = 500
TOPICS = ["phone_service_issue", "demand_peak", "phone_order_channel", "phone_inquiry_channel", "shared_staff_workload", "wait_or_capacity", "order_operations", "location_structure", "other"]
SCOPES = ["this_location", "company_wide", "unclear"]
SCHEMA = {"type": "object", "additionalProperties": False, "required": ["claims"], "properties": {
    "claims": {"type": "array", "items": {"type": "object", "additionalProperties": False,
        "required": ["evidence_description", "source_quote", "topic", "scope", "location_label"],
        "properties": {"evidence_description": {"type": "string"}, "source_quote": {"type": "string"},
            "topic": {"type": "string", "enum": TOPICS}, "scope": {"type": "string", "enum": SCOPES},
            "location_label": {"type": "string"}}}}}}
OUTPUT_FIELDS = ["evidence_id", "document_id", "source_sha256", "company_id", "location_id", "company_name", "location_label", "evidence_description", "source_quote", "topic", "evidence_scope", "source_type", "source_url", "captured_at", "published_at", "author", "model", "prompt_version", "prompt_sha256"]
STATUS_FIELDS = ["document_id", "source_sha256", "company_id", "location_id", "company_name", "source_type", "source_url", "captured_at", "source_text_chars", "chunks", "extraction_status", "evidence_count", "model", "prompt_version", "prompt_sha256", "input_tokens", "output_tokens", "cache_hits", "api_calls", "error"]


def digest(value):
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


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


def stable_id(prefix, *parts):
    return prefix + "_" + digest("\x1f".join(str(p or "") for p in parts))[:14]


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def get(row, *keys):
    return next((str(row.get(k) or "").strip() for k in keys if str(row.get(k) or "").strip()), "")


def chunks(text):
    result, start = [], 0
    while start < len(text):
        end = min(start + CHUNK_SIZE, len(text))
        result.append((start, text[start:end]))
        if end == len(text):
            break
        start = end - CHUNK_OVERLAP
    return result


def call_api(api_key, model, prompt, document, text, timeout):
    content = {"document_id": document["document_id"], "company_name": document["company_name"],
        "location_label": document["location_label"], "source_type": document["source_type"],
        "source_url": document["source_url"], "published_at": document["published_at"], "source_text": text}
    payload = {"model": model, "instructions": prompt,
        "input": json.dumps(content, ensure_ascii=False),
        "text": {"format": {"type": "json_schema", "name": "evidence_extraction", "strict": True, "schema": SCHEMA}},
        "max_output_tokens": 2000, "store": False}
    req = Request("https://api.openai.com/v1/responses", data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}, method="POST")
    with urlopen(req, timeout=timeout) as response:
        result = json.load(response)
    text_out = "".join(c.get("text", "") for o in result.get("output", []) if o.get("type") == "message"
                       for c in o.get("content", []) if c.get("type") == "output_text")
    if not text_out:
        raise ValueError(f"No se recibió salida estructurada: {result.get('status')}")
    claims = json.loads(text_out).get("claims", [])
    for claim in claims:
        quote = claim.get("source_quote", "")
        if not quote or quote not in text:
            raise ValueError("La salida incluyó una cita que no aparece literalmente en el fragmento fuente")
    usage = result.get("usage", {})
    return claims, {"response_id": result.get("id", ""), "input_tokens": usage.get("input_tokens", 0), "output_tokens": usage.get("output_tokens", 0)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--documents", type=Path, default=INPUT_DEFAULT)
    parser.add_argument("--reviews", type=Path, default=REVIEWS_DEFAULT,
                        help="Reseñas de una fuente que permita exportar y analizar el contenido.")
    parser.add_argument("--out-dir", type=Path, default=OUT_DEFAULT)
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", ""))
    parser.add_argument("--max-documents", type=int, default=30)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--delay", type=float, default=0.2)
    parser.add_argument("--run", action="store_true", help="Habilita llamadas pagas a OpenAI; por defecto es dry-run.")
    parser.add_argument('--responses', type=Path, help='Respuestas JSON nuevas de Codex, separadas del código; no llama API.')
    parser.add_argument('--requests', type=Path, help='Exporta prompts/entradas exactas para interpretar con Codex.')
    args = parser.parse_args()
    if args.run and args.responses:
        raise SystemExit('Elegir API o respuestas de archivos, no ambos.')
    external = load_responses(args.responses)
    request_records = []
    if args.max_documents < 1 or args.offset < 0:
        raise SystemExit("--max-documents debe ser positivo y --offset no puede ser negativo")
    documents = read_csv(args.documents) + (read_csv(args.reviews) if args.reviews.exists() else [])
    prompt = PROMPT_PATH.read_text(encoding="utf-8")
    prompt_hash = digest(prompt)
    version_match = re.search(r"Versión:\s*`([^`]+)`", prompt)
    prompt_version = version_match.group(1) if version_match else "unversioned"
    model = args.model or "(configurar OPENAI_MODEL)"
    if args.run and not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("--run requiere OPENAI_API_KEY; no se hizo ninguna llamada")
    if args.run and not args.model:
        raise SystemExit("--run requiere --model o OPENAI_MODEL")
    normalized = []
    for rownum, row in enumerate(documents, 1):
        text = get(row, "source_text")
        doc = {"document_id": get(row, "document_id") or stable_id("doc", get(row, "company_id") or get(row, "project_company_id"), get(row, "location_id") or get(row, "project_location_id"), get(row, "source_url"), rownum),
            "company_id": get(row, "company_id"), "location_id": get(row, "location_id"),
            "company_name": get(row, "company_name"), "location_label": get(row, "location_label"),
            "source_type": get(row, "source_type"), "source_url": get(row, "source_url"),
            "captured_at": get(row, "captured_at"), "published_at": get(row, "published_at"),
            "author": get(row, "author"), "source_text": text}
        doc["source_sha256"] = digest({k: doc[k] for k in ("source_url", "source_text", "published_at", "author")})
        normalized.append(doc)
    without_text = [doc for doc in normalized if not doc["source_text"]]
    processable = [doc for doc in normalized if doc["source_text"]]
    batch = processable[args.offset:args.offset + args.max_documents]
    mode = 'Codex por archivos' if args.responses else ('API' if args.run else 'dry-run')
    print(f"Documentos en entrada: {len(normalized)}; con texto fuente: {len(processable)}; lote LLM: {len(batch)}; modo={mode}")
    cache_dir = args.out_dir / ".pipeline" / "extraction_cache"
    all_claim_rows, status_rows = [], []
    for doc in batch:
        text = doc["source_text"]
        doc_id = doc["document_id"]
        doc_claims, input_tokens, output_tokens, cache_hits, api_calls = [], 0, 0, 0, 0
        error = ""
        if not text:
            status = "sin_texto_fuente_original"
        else:
            status = "pendiente_dry_run" if not args.run else "complete"
            for chunk_no, (start, chunk_text) in enumerate(chunks(text)):
                fingerprint = digest({"model": model, "prompt": prompt_hash, "document": doc, "start": start, "text": chunk_text})
                request_records.append({'request_id': fingerprint, 'company_id': doc['company_id'], 'location_id': doc['location_id'],
                    'company_name': doc['company_name'], 'chunk': chunk_no, 'input': {**{k: doc[k] for k in ('document_id','company_name','location_label','source_type','source_url','published_at')}, 'source_text': chunk_text}})
                cache_path = cache_dir / f"{doc_id}_{chunk_no}_{fingerprint[:14]}.json"
                if args.responses:
                    if fingerprint not in external:
                        raise ValueError(f'Falta respuesta Codex para {doc_id}, bloque {chunk_no}')
                    response = external[fingerprint]
                    validate(response, SCHEMA)
                    claims, usage = response['claims'], {}
                    for claim in claims:
                        if not claim['source_quote'] or claim['source_quote'] not in chunk_text:
                            raise ValueError(f'Cita Codex no encontrada en el texto: {doc_id}')
                elif cache_path.exists():
                    cached = json.loads(cache_path.read_text(encoding="utf-8"))
                    claims, usage = cached["claims"], cached["usage"]
                    cache_hits += 1
                elif args.run:
                    try:
                        claims, usage = call_api(os.environ["OPENAI_API_KEY"], model, prompt, doc, chunk_text, args.timeout)
                        cache_path.parent.mkdir(parents=True, exist_ok=True)
                        cache_path.write_text(json.dumps({"claims": claims, "usage": usage, "model": model,
                            "prompt_version": prompt_version, "prompt_sha256": prompt_hash}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                        api_calls += 1
                        time.sleep(args.delay)
                    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
                        error, status = format_api_error(exc), "error"
                        break
                else:
                    continue
                input_tokens += usage.get("input_tokens", 0)
                output_tokens += usage.get("output_tokens", 0)
                doc_claims.extend(claims)
            # Overlapping chunks can return the same sourced assertion; dedupe exact quote + claim.
            unique_claims = {}
            for claim in doc_claims:
                unique_claims[(claim["source_quote"], claim["evidence_description"].casefold())] = claim
            doc_claims = list(unique_claims.values())
            if args.responses:
                status = 'evidencia_extraida_con_codex' if doc_claims else 'sin_evidencia_relevante_con_codex'
            if not args.run and cache_hits:
                status = "evidencia_extraida_en_cache" if doc_claims else "sin_evidencia_relevante_en_cache"
            if args.run and status == "complete" and not doc_claims:
                status = "sin_evidencia_relevante"
            if args.run and status == "complete" and doc_claims:
                status = "evidencia_extraida"
        for ordinal, claim in enumerate(doc_claims, 1):
            all_claim_rows.append({"evidence_id": stable_id("evi", doc_id, ordinal, claim["source_quote"]),
                "source_sha256": doc["source_sha256"],
                "document_id": doc_id, **{k: doc[k] for k in ("company_id", "location_id", "company_name", "location_label", "source_type", "source_url", "captured_at", "published_at", "author")},
                "evidence_description": claim["evidence_description"], "source_quote": claim["source_quote"],
                "topic": claim["topic"], "evidence_scope": claim["scope"],
                "model": model, "prompt_version": prompt_version, "prompt_sha256": prompt_hash})
        status_rows.append({"document_id": doc_id, "source_sha256": doc["source_sha256"], "company_id": doc["company_id"], "location_id": doc["location_id"],
            "company_name": doc["company_name"], "source_type": doc["source_type"], "source_url": doc["source_url"],
            "captured_at": doc["captured_at"], "source_text_chars": len(text), "chunks": len(chunks(text)),
            "extraction_status": status, "evidence_count": len(doc_claims), "model": model,
            "prompt_version": prompt_version, "prompt_sha256": prompt_hash, "input_tokens": input_tokens,
            "output_tokens": output_tokens, "cache_hits": cache_hits, "api_calls": api_calls, "error": error})
        print(f"{doc_id}: {status}; {len(doc_claims)} afirmaciones; {cache_hits} caché; {api_calls} llamadas")
    for doc in without_text:
        status_rows.append({"document_id": doc["document_id"], "source_sha256": doc["source_sha256"],
            "company_id": doc["company_id"], "location_id": doc["location_id"], "company_name": doc["company_name"],
            "source_type": doc["source_type"], "source_url": doc["source_url"], "captured_at": doc["captured_at"],
            "source_text_chars": 0, "chunks": 0, "extraction_status": "sin_texto_fuente_original",
            "evidence_count": 0, "model": model, "prompt_version": prompt_version, "prompt_sha256": prompt_hash,
            "input_tokens": 0, "output_tokens": 0, "cache_hits": 0, "api_calls": 0, "error": ""})
    all_document_ids = {doc["document_id"] for doc in normalized}
    batch_ids = {doc["document_id"] for doc in batch + without_text}
    output_path = args.out_dir / "evidencia_llm_procesada.csv"
    status_path = args.out_dir / ".pipeline" / "estado_extraccion_llm.csv"
    prior_claims = read_csv(output_path) if output_path.exists() else []
    source_hashes = {doc["document_id"]: doc["source_sha256"] for doc in normalized}
    prior_claims = [row for row in prior_claims if row.get("document_id") in all_document_ids
                    and row.get("model") == model and row.get("prompt_sha256") == prompt_hash
                    and row.get("source_sha256") == source_hashes.get(row.get("document_id"))
                    and row.get("document_id") not in batch_ids]
    merged_claims = prior_claims + all_claim_rows
    prior_status = read_csv(status_path) if status_path.exists() else []
    prior_status = [row for row in prior_status if row.get("document_id") in all_document_ids
                    and row.get("model") == model and row.get("prompt_sha256") == prompt_hash
                    and row.get("source_sha256") == source_hashes.get(row.get("document_id"))
                    and row.get("document_id") not in batch_ids]
    write_csv(output_path, OUTPUT_FIELDS, prior_claims + all_claim_rows)
    write_csv(status_path, STATUS_FIELDS, prior_status + status_rows)
    save_requests(args.requests, prompt, SCHEMA, request_records)
    print(f"Salida: {output_path} ({len(merged_claims)} evidencias acumuladas); estado técnico en .pipeline/")


if __name__ == "__main__":
    try:
        main()
    except (OSError, csv.Error, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
