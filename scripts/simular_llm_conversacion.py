#!/usr/bin/env python3
"""Simula ambas etapas LLM sobre el corpus capturado, sin invocar una API.

Las afirmaciones y etiquetas se revisaron manualmente en esta conversación.
El script comprueba cada cita contra el texto local y aplica los agregados
Python del pipeline; no imita ni acredita una respuesta de OpenAI.
"""
import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from extraer_evidencias_llm import OUTPUT_FIELDS, SCHEMA as EXTRACTION_SCHEMA, chunks as extraction_chunks, digest, read_csv, stable_id, write_csv
from analizar_evidencias_llm import (
    INDICATOR_FIELDS,
    LABEL_SCHEMA,
    build_outputs,
    prepare_companies,
    prepare_evidence,
    read_csv as read_analysis_csv,
    write_csv as write_analysis_csv,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DEFAULT = ROOT / "data/evidencia_locales.csv"
COMPANIES_DEFAULT = ROOT / "data/locales.csv"
OUT_DEFAULT = ROOT / "data/simulacion_conversacion"
EXTRACTION_PROMPT = ROOT / "prompts/extraer_evidencias.md"
CLASSIFICATION_PROMPT = ROOT / "prompts/clasificar_evidencias.md"
SIMULATED_MODEL = "simulacion_chatgpt_no_api"


# claim tuple: source_quote, description, extraction topic, scope,
# classification topic, strength, sentiment, attribution, rationale.
CLAIMS = {
    "https://pequodspizza.com/faqs/": [
        ("Our busiest day is Saturday, and our peak hours are typically the dinner rush between 6-8PM.", "La FAQ indica que el sábado es el día más concurrido y que el pico habitual ocurre durante la cena, entre 6 y 8 p. m.", "demand_peak", "company_wide", "demand_peak", "direct", "neutral", "company_wide", "Declara los días y horas pico; no documenta un problema telefónico."),
        ("You can place orders for Take-out and Delivery in advance by calling the restaurant or ordering online at order.pequodspizza.com.", "Se pueden anticipar pedidos de takeout y delivery por teléfono o mediante pedidos en línea.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "El teléfono es un canal de pedido, no una señal de falla."),
        ("We always recommend making a reservation through our partner Tock, as walk-in availability is limited. On short notice, you can call the restaurant for current availability.", "La FAQ señala disponibilidad limitada para clientes sin reserva e indica llamar para consultar disponibilidad a corto plazo.", "wait_or_capacity", "company_wide", "wait_or_capacity", "context", "neutral", "company_wide", "La disponibilidad limitada es contexto de capacidad, no evidencia de llamadas perdidas."),
        ("In Chicago, Take-out orders are available for pick up at the host stand. On Friday & Saturday from 4pm – 9pm and Sunday from 5pm – 8pm, all Take-out orders are available at Whale Tale just two doors down from Pequod’s.", "El punto de retiro de takeout en Chicago cambia según el horario: host stand o Whale Tale.", "order_operations", "this_location", "multi_location_context", "context", "neutral", "this_location", "Describe una modalidad operativa para Chicago, sin reportar una falla."),
        ("The Chicago location is open Monday – Saturday: 11am – 2am and Sunday: 11am – 12am. In Morton Grove, the hours are as follows: Monday – Thursday: 11am – 9:30pm, Friday: 11am – 11:30pm, Saturday: 12pm – 11:30pm, Sunday: 12pm – 9:30pm.", "La FAQ publica horarios distintos para las ubicaciones de Chicago y Morton Grove.", "location_structure", "company_wide", "multi_location_context", "direct", "neutral", "company_wide", "La página distingue dos ubicaciones; el resto de la FAQ no se atribuye automáticamente a Chicago."),
    ],
    "https://www.pappyssmokehouse.com/contact": [
        ("All pick up orders can be placed by calling Pappy's directly at (314) 535-4340 .", "Pappy's publica el teléfono como canal para pedidos de retiro.", "phone_order_channel", "this_location", "phone_order_channel", "direct", "neutral", "this_location", "Confirma pedidos telefónicos en la sucursal de St. Louis; no indica problemas al atender."),
        ("We do not take reservations, as we operate on a first come, first serve basis.", "El restaurante atiende sin reservas y por orden de llegada.", "wait_or_capacity", "company_wide", "wait_or_capacity", "context", "neutral", "company_wide", "Es contexto de flujo presencial, no una queja ni una espera medida."),
    ],
    "https://www.litzaspizza.com/blog/midvale-family-pizza/": [
        ("Friday and Saturday nights it’s packed.", "La publicación describe el salón de Midvale como lleno los viernes y sábados por la noche.", "demand_peak", "this_location", "demand_peak", "direct", "neutral", "this_location", "La frase describe ocupación recurrente en horarios concretos; no habla del teléfono."),
        ("Pick your shop, then order online through Slice or call it in.", "La web permite elegir la sucursal y hacer el pedido por Slice o por teléfono.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "Confirma el canal telefónico; no demuestra una falla."),
    ],
    "https://www.joeskc.com/pages/contact-us": [
        ("All orders must be made by phone or in-person.", "Joe's indica que los pedidos de retiro se toman por teléfono o en persona.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "La política hace explícito el canal telefónico."),
        ("If you are calling to place an order and the phones are busy, please call back. Our phones are working. We will get to your call as soon as we can.", "La página pide volver a llamar cuando las líneas están ocupadas y señala que atenderán cuando puedan.", "phone_service_issue", "company_wide", "phone_service_issue", "direct", "neutral", "company_wide", "Reconoce ocupación de líneas y reintentos; no cuantifica llamadas abandonadas ni atribuye causa."),
    ],
    "https://www.blacksbbq.com/locations/lockhart/pick-up-delivery": [
        ("Place your bbq order by giving us a call to have our legendary Texas BBQ hot and ready for you.", "Black's invita a llamar para preparar pedidos de BBQ para retiro.", "phone_order_channel", "this_location", "phone_order_channel", "direct", "neutral", "this_location", "Confirma pedidos por teléfono en Lockhart."),
        ("When we're really busy we'll be taking walk-ins only, but give us call to find out how we can best serve you.", "Cuando el local está muy ocupado, puede limitarse a atender clientes sin reserva y pide llamar para consultar opciones.", "wait_or_capacity", "this_location", "wait_or_capacity", "direct", "neutral", "this_location", "La limitación operativa está expresamente publicada; es condicional y no demuestra frecuencia ni llamadas perdidas. Confirmar si el límite es la cocina."),
    ],
    "https://downtownpizzasc.com/contact": [
        ("Do you take orders over the phone? Yes, but online ordering (Toast) is usually faster during busy hours.", "La sucursal acepta pedidos telefónicos, aunque recomienda Toast durante horas concurridas.", "phone_order_channel", "this_location", "phone_order_channel", "direct", "neutral", "this_location", "Confirma pedidos por teléfono y menciona horas concurridas; no afirma que las llamadas queden sin atender."),
        ("Spartanburg and Inman are separate locations with separate ordering systems — it’s the guest’s responsibility to pick the correct place.", "Spartanburg e Inman tienen sistemas de pedido separados y el cliente debe elegir la sucursal correcta.", "location_structure", "company_wide", "multi_location_context", "direct", "neutral", "company_wide", "Es contexto de estructura de sucursales y pedidos."),
    ],
    "https://www.salvatorestomatopies.com/careers/": [
        ("Helping team members by answering phones, greeting and seating guests, and assisting in orders", "El puesto combina responder teléfonos con recibir, sentar y ayudar a los clientes con pedidos.", "shared_staff_workload", "unclear", "shared_staff_workload", "direct", "neutral", "unclear", "La descripción laboral asigna varias tareas al mismo rol; no demuestra saturación actual ni una sucursal específica."),
        ("The position involves answering the phones, taking reservations, taking phone orders, and backing up servers when needed.", "El puesto contempla atender llamadas, reservas y pedidos telefónicos, además de apoyar al equipo de salón.", "shared_staff_workload", "unclear", "shared_staff_workload", "direct", "neutral", "unclear", "Enumera tareas compartidas en el puesto, sin reportar problemas de atención."),
    ],
    "https://zacharys.com/frequently-asked-questions/": [
        ("We take dine-in orders over the phone 11 am- 4 pm only.", "Zachary's acepta pedidos telefónicos para consumir en el salón solo entre las 11 y las 16.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "Describe el alcance horario del canal telefónico."),
        ("After 4 pm we are only able to accept take-out orders over the phone.", "Después de las 16, la página limita los pedidos por teléfono a takeout.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "Es una política de canal, no evidencia de llamadas perdidas."),
    ],
    "https://zacharys.com/locations/pleasant-hill/": [
        ("Call your personal pizza in ahead of time so it’s ready when you arrive!", "La página de Pleasant Hill invita a llamar con anticipación el pedido individual.", "phone_order_channel", "this_location", "phone_order_channel", "direct", "neutral", "this_location", "Confirma pedidos telefónicos anticipados en Pleasant Hill."),
        ("If there is a wait for tables when you arrive, you will be able to order your pizzas once you have been added to the waitlist.", "Los clientes pueden hacer el pedido después de incorporarse a la lista de espera cuando hay espera para mesas.", "wait_or_capacity", "this_location", "wait_or_capacity", "context", "neutral", "this_location", "Describe cómo se gestiona una espera presencial; no es una queja telefónica."),
    ],
    "https://www.vpizza.com/jobs/cashier-and-food-runner/": [
        ("Taking orders accurately on our Toast POS, including answering phones and placing to-go orders", "El rol de caja incluye responder teléfonos y tomar pedidos para llevar.", "shared_staff_workload", "company_wide", "shared_staff_workload", "direct", "neutral", "company_wide", "La descripción laboral combina tareas de caja y teléfono, sin probar que se acumulen."),
        ("And we will show you why we have grown to 12 locations, with 2 new locations under construction, and no slowing down in our future!", "La empresa informa 12 ubicaciones y dos nuevas en construcción.", "location_structure", "company_wide", "multi_location_context", "direct", "neutral", "company_wide", "El conteo publicado describe la escala de la empresa; las aperturas futuras no se suman como locales activos."),
    ],
    "https://katies.com/pages/important-info": [
        ("Due to a high volume of phone calls and limited lines, we encourage online ordering only.", "Katie's atribuye su recomendación de pedido online al alto volumen de llamadas y a la cantidad limitada de líneas.", "phone_service_issue", "company_wide", "phone_service_issue", "direct", "negative", "company_wide", "Es la señal pública más directa de presión en el canal telefónico; no informa cuántas llamadas no se atienden."),
        ("If phone is busy that means that we are on all phone lines helping another guest and you will have to call back until you get through.", "La página explica que, si el teléfono está ocupado, todas las líneas atienden a otros clientes y hay que volver a llamar.", "phone_service_issue", "company_wide", "phone_service_issue", "direct", "negative", "company_wide", "Describe explícitamente el reintento ante líneas ocupadas; no cuantifica su frecuencia."),
    ],
    "https://www.pizzeriadelfina.com/catering/": [
        ("Whether you prefer to order online, over the phone, or through email, we have you covered.", "Pizzeria Delfina ofrece pedidos de catering en línea, por teléfono o correo electrónico.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "Confirma teléfono como canal de pedidos de catering, no de pedidos regulares."),
    ],
    "https://www.goldenboypizza.com/": [
        ("TAKE OUT ONLY. PHONE AHEAD, ORDER IN PERSON, OR ORDER FOR DELIVERY.", "Golden Boy describe un modelo takeout y permite llamar por adelantado, pedir en persona o delivery.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "Es contexto de canal y formato del negocio, no una falla."),
    ],
    "https://www.hotlipspizza.com/": [
        ("If our online ordering site says we're closed (or that you’re out of our zone and you know you’re not), we just need to control order times a little more accurately over the phones & have our online ordering temporarily deactivated. Please call us directly!", "HOTLIPS indica que puede desactivar temporalmente pedidos online para controlar mejor los horarios y pide llamar directamente.", "order_operations", "company_wide", "order_operations", "direct", "neutral", "company_wide", "Describe gestión de horarios/canales cuando el pedido online está desactivado; no dice que las llamadas fallen."),
    ],
    "https://www.hotlipspizza.com/jobs": [
        ("We’re open seven days a week and our busiest times are evenings and weekends - that’s when we typically look for availability.", "La página de empleo identifica las tardes y fines de semana como los momentos de mayor actividad.", "demand_peak", "company_wide", "demand_peak", "direct", "neutral", "company_wide", "La página identifica períodos concurridos, no problemas telefónicos."),
    ],
    "https://hollandfarms.com/manlius/": [
        ("Place a Phone Order: (315) 671 – 6344", "Holland Farms publica un número específico para pedidos por teléfono en Manlius.", "phone_order_channel", "this_location", "phone_order_channel", "direct", "neutral", "this_location", "Confirma el canal telefónico en la sucursal identificada."),
        ("Because it’s an express window, we ask you to order no more than three cups of coffee and six pastries so that we can serve everyone quickly and with a smile.", "La ventanilla express limita el tamaño de algunos pedidos para poder atender con rapidez.", "wait_or_capacity", "this_location", "wait_or_capacity", "context", "neutral", "this_location", "Es una regla de capacidad de una ventanilla; no evidencia llamadas sin atender."),
    ],
    "https://www.dallasbbq.com/careers": [
        ("Apply online or in-person at any one of our 12 locations.", "Dallas BBQ informa que recibe solicitudes en cualquiera de sus 12 locales.", "location_structure", "company_wide", "multi_location_context", "direct", "neutral", "company_wide", "La página corrobora 12 locales activos para el contexto de escala."),
        ("Non-tipped positions include Phone Operator, Host, Bartender, Barista, Dishwasher, Line Cook, Prep Cook, and Takeout Packing", "La empresa publica puestos diferenciados de operador telefónico y preparación de pedidos para llevar.", "other", "company_wide", "other", "context", "neutral", "company_wide", "Muestra funciones separadas, pero no demuestra volumen, fallas ni tareas compartidas."),
    ],
    "https://pizzaluce.com/locations": [
        ("We've got nine neighborhood Pizza Lucé locations in the Twin Cities and Duluth.", "Pizza Lucé publica nueve sucursales en Twin Cities y Duluth.", "location_structure", "company_wide", "multi_location_context", "direct", "neutral", "company_wide", "Es contexto de escala, no evidencia de un problema operativo."),
    ],
    "https://www.nypienashville.com/": [
        ("The staff is always friendly and welcoming, and the service is quick—even when they’re packed (which they often are because it's THAT good).", "Un testimonio publicado en la página describe el local lleno con frecuencia y servicio rápido.", "demand_peak", "unclear", "demand_peak", "context", "positive", "unclear", "Es un testimonio promocional sin autor o sucursal identificable; señal débil de demanda, no una queja."),
    ],
    "https://www.supertacomex.com/": [
        ("Florin / Franklin 7131 Franklin Blvd, Sacramento, CA 95823 (916) 469-9104 OPEN HOURS Mon - Wed : 10 am - 8:30 pm Thurs - Sat : 9 am - 9 pm Sun : 9 am - 8: 30 pm", "La web identifica la sucursal Franklin con dirección, teléfono y horarios.", "location_structure", "this_location", "multi_location_context", "direct", "neutral", "this_location", "Confirma la sucursal candidata y su información publicada; no ofrece una señal telefónica de demanda."),
    ],
    "http://www.kickinchicken.com": [
        ("across our six Lowcountry locations.", "La web informa seis ubicaciones en Lowcountry.", "location_structure", "company_wide", "multi_location_context", "direct", "neutral", "company_wide", "Confirma la escala de la marca; no describe fallas de atención."),
    ],
    "http://www.sickiesburgers.com": [
        ("13 locations.", "La página de Sickies informa que la cadena tiene 13 ubicaciones.", "location_structure", "company_wide", "multi_location_context", "direct", "neutral", "company_wide", "Confirma la escala publicada; no describe el trabajo del teléfono."),
    ],
}


# Revisión v2: conservar el canal y el contexto operativo como señales útiles,
# sin reclasificarlos como fallas. Una cita puede respaldar temas distintos;
# el puntaje posterior usa presencia de señales, no cantidad de menciones.
CLAIMS["https://www.salvatorestomatopies.com/careers/"].append(
    ("The position involves answering the phones, taking reservations, taking phone orders, and backing up servers when needed.", "El puesto incluye tomar pedidos por teléfono.", "phone_order_channel", "unclear", "phone_order_channel", "direct", "neutral", "unclear", "Confirma pedidos telefónicos en el puesto; la sucursal no está especificada.")
)
CLAIMS["https://katies.com/pages/important-info"].append(
    ("We request you reserve phone ordering for those that do not have computer access.", "Katie's reserva los pedidos por teléfono para quienes no tienen acceso a una computadora.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "El canal existe con restricciones; no implica que todos los pedidos sean telefónicos.")
)
CLAIMS["https://www.hotlipspizza.com/"].append(
    ("we just need to control order times a little more accurately over the phones & have our online ordering temporarily deactivated.", "HOTLIPS usa el teléfono para controlar horarios de pedidos cuando desactiva temporalmente los pedidos online.", "phone_order_channel", "company_wide", "phone_order_channel", "direct", "neutral", "company_wide", "Describe el uso operativo del teléfono; no demuestra llamadas perdidas.")
)
CLAIMS["https://downtownpizzasc.com/contact"].append(
    ("Yes, but online ordering (Toast) is usually faster during busy hours.", "La web indica que Toast suele ser más rápido que el pedido telefónico durante horas concurridas.", "demand_peak", "this_location", "demand_peak", "indirect", "neutral", "this_location", "La comparación entre canales menciona horas concurridas; no cuantifica la demanda ni demuestra fallas. Está en los datos FAQ del HTML y requiere confirmar vigencia.")
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE_DEFAULT)
    parser.add_argument("--companies", type=Path, default=COMPANIES_DEFAULT)
    parser.add_argument("--out-dir", type=Path, default=OUT_DEFAULT)
    args = parser.parse_args()

    source_rows = read_csv(args.source)
    locations = read_analysis_csv(args.companies)
    companies = prepare_companies(locations)
    extraction_prompt = EXTRACTION_PROMPT.read_text(encoding="utf-8")
    classifier_prompt = CLASSIFICATION_PROMPT.read_text(encoding="utf-8")
    extraction_hash = digest(extraction_prompt)
    classifier_hash = hashlib.sha256(classifier_prompt.encode("utf-8")).hexdigest()
    extraction_version = re.search(r"Versión:\s*`([^`]+)`", extraction_prompt).group(1)
    classifier_version = re.search(r"Versión:\s*`([^`]+)`", classifier_prompt).group(1)
    captures, labels_by_company, status_rows = [], defaultdict(list), []
    extraction_cases = []
    counts_by_company = Counter()
    captured_locations = set()
    captured_companies = set()

    for rownum, source in enumerate(source_rows, 1):
        text = (source.get("source_text") or "").strip()
        if not text:
            continue
        url = (source.get("source_url") or "").strip()
        company_id, location_id = source.get("company_id", ""), source.get("location_id", "")
        company_name = source.get("company_name", "")
        if url not in CLAIMS:
            claims = []
        else:
            claims = CLAIMS[url]
        doc_id = (source.get("document_id") or "").strip() or stable_id(
            "doc", company_id, location_id, url, rownum
        )
        source_hash = digest({key: source.get(key, "") for key in ("source_url", "source_text", "published_at", "author")})
        captured_locations.add(location_id)
        captured_companies.add(company_id)
        for ordinal, claim in enumerate(claims, 1):
            quote, description, extract_topic, scope, topic, strength, sentiment, attribution, rationale = claim
            if quote not in text:
                raise ValueError(f"Cita no encontrada literalmente para {company_name} ({url}): {quote}")
            evidence_id = stable_id("evi", doc_id, ordinal, quote)
            counts_by_company[company_id] += 1
            captures.append({
                "evidence_id": evidence_id, "document_id": doc_id, "source_sha256": source_hash,
                "company_id": company_id, "location_id": location_id, "company_name": company_name,
                "location_label": source.get("location_label", ""), "evidence_description": description,
                "source_quote": quote, "topic": extract_topic, "evidence_scope": scope,
                "source_type": source.get("source_type", ""), "source_url": url,
                "captured_at": source.get("captured_at", ""), "published_at": source.get("published_at", ""),
                "author": source.get("author", ""), "model": SIMULATED_MODEL,
                "prompt_version": extraction_version, "prompt_sha256": extraction_hash,
            })
            labels_by_company[company_id].append({
                "evidence_id": evidence_id, "topic": topic, "strength": strength,
                "sentiment": sentiment, "attribution": attribution, "verbatim_quote": quote,
                "rationale": rationale,
            })
        for chunk_number, (chunk_start, chunk_text) in enumerate(extraction_chunks(text), 1):
            chunk_claims = [item for item in claims if item[0] in chunk_text]
            extraction_response = {"claims": [
                {"evidence_description": item[1], "source_quote": item[0], "topic": item[2],
                 "scope": item[3], "location_label": source.get("location_label", "") if item[3] == "this_location" else ""}
                for item in chunk_claims
            ]}
            extraction_input = {
                "document_id": doc_id, "company_name": company_name,
                "location_label": source.get("location_label", ""),
                "source_type": source.get("source_type", ""), "source_url": url,
                "published_at": source.get("published_at", ""), "source_text": chunk_text,
            }
            extraction_cases.append({
                "company_id": company_id, "company_name": company_name,
                "location_id": location_id, "source_url": url, "source_row": rownum,
                "document_id": doc_id, "chunk_number": chunk_number, "chunk_start": chunk_start,
                "request_would_be_sent_if_run": True, "response_is_simulated": True,
                "request_options": {"max_output_tokens": 2000, "store": False},
                "input": extraction_input,
                "simulated_response": extraction_response,
                "response_status": "claims_returned" if chunk_claims else "empty_claims",
            })
        status_rows.append({
            "company_id": company_id, "location_id": location_id, "company_name": company_name,
            "source_url": url, "source_type": source.get("source_type", ""),
            "captured_at": source.get("captured_at", ""), "source_text_chars": len(text),
            "simulation_status": "evidence_extracted_manually" if claims else "reviewed_no_relevant_claim",
            "evidence_count": len(claims), "api_calls": 0, "model": SIMULATED_MODEL,
        })

    # The first script omits documents with no supported signal. In a real run,
    # extraction status is retained separately; include those rows here so the
    # demo can distinguish reviewed/no-signal from genuinely missing source text.
    relevant_rows = [row for row in captures]
    evidence_by_company = prepare_evidence(relevant_rows, companies)
    selected = list(companies.items())
    usage = {cid: {"input_tokens": 0, "output_tokens": 0} for cid in companies}
    cache = {cid: {"cached": 0, "api": 0} for cid in companies}
    build_outputs(
        companies, evidence_by_company, selected, labels_by_company, usage, cache, {},
        SIMULATED_MODEL, classifier_version, classifier_hash, args.out_dir,
    )
    # Replace the script's generic empty-input state with the manual corpus
    # review result: no relevant claim vs. no source captured are distinct.
    result_path = args.out_dir / "resultados_evidencia_llm.csv"
    result_rows = read_analysis_csv(result_path)
    reviewed_ids = captured_companies
    for row in result_rows:
        cid = row["company_id"]
        if cid in reviewed_ids and not counts_by_company[cid]:
            row["analysis_status"] = "complete"
            row["evidence_readiness"] = "no_relevant_public_signal"
            row["evidence_count"] = 0
    write_analysis_csv(result_path, INDICATOR_FIELDS + ["error"], result_rows)
    write_csv(args.out_dir / "evidencia_llm_procesada.csv", OUTPUT_FIELDS, captures)
    write_analysis_csv(args.out_dir / "estado_simulacion.csv", [
        "company_id", "location_id", "company_name", "source_url", "source_type",
        "captured_at", "source_text_chars", "simulation_status", "evidence_count", "api_calls", "model",
    ], status_rows)

    classification_cases, skipped_classification = [], []
    for cid, company in companies.items():
        items = [item for item in evidence_by_company.get(cid, [])
                 if item["content_kind"] in {"source_text", "verified_extraction"}]
        if not items:
            skipped_classification.append({"company_id": cid, "company_name": company["company_name"],
                                           "reason": "No hay afirmaciones extraídas para enviar al clasificador."})
            continue
        payload = {
            "company": {"name": company["company_name"], "locations": list(company["locations"].values()),
                        "apollo_profile": company["profile"]},
            "evidence": [{key: item[key] for key in (
                "evidence_id", "location_id", "location_label", "source_type", "source_url",
                "published_at", "content_kind", "content", "provenance_note"
            )} for item in items],
        }
        classification_cases.append({
            "company_id": cid, "company_name": company["company_name"],
            "request_would_be_sent_if_run": True, "response_is_simulated": True, "input": payload,
            "request_options": {"max_output_tokens": max(1200, 180 * len(items)), "store": False},
            "simulated_response": {"labels": labels_by_company[cid]},
        })
    missing_sources = [row for row in read_csv(args.companies)
                       if row.get("company_name") in {"Bar-Bill Tavern", "Mama's Pizza Omaha"}]
    trace = {
        "provenance": "Simulación manual en conversación; ninguna respuesta proviene de OpenAI API.",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model_label": SIMULATED_MODEL,
        "api_calls_made": 0,
        "hypothetical_extraction_calls": len(extraction_cases),
        "hypothetical_classification_calls": len(classification_cases),
        "instructions": {
            "extraction_prompt_version": extraction_version,
            "extraction_prompt_sha256": extraction_hash,
            "extraction_prompt": extraction_prompt,
            "extraction_response_schema": EXTRACTION_SCHEMA,
            "classification_prompt_version": classifier_version,
            "classification_prompt_sha256": classifier_hash,
            "classification_prompt": classifier_prompt,
            "classification_response_schema": LABEL_SCHEMA,
        },
        "extraction_cases": extraction_cases,
        "classification_cases": classification_cases,
        "classification_skipped": skipped_classification,
        "sources_not_submitted": [
            {"company_id": row.get("company_id", ""), "company_name": row.get("company_name", ""),
             "reason": "No source_text capturado; no se puede simular una extracción respaldada por fuente."}
            for row in missing_sources
        ],
    }
    (args.out_dir / "prompts_y_respuestas_simuladas.json").write_text(
        json.dumps(trace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    totals = Counter(row["simulation_status"] for row in status_rows)
    print(f"Documentos capturados revisados: {len(status_rows)}; sucursales con texto: {len(captured_locations)}")
    print(f"Afirmaciones simuladas: {len(captures)}; estados: {dict(totals)}")
    print(f"Empresas en indicadores: {len(result_rows)}; llamadas API: 0; "
          f"{len(extraction_cases)} solicitudes de extracción y {len(classification_cases)} de clasificación simuladas; créditos: 0")
    print(f"Salidas: {args.out_dir}")


if __name__ == "__main__":
    main()
