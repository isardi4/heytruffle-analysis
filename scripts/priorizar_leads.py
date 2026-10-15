"""Regla de prioridad compartida por el generador de entrega. Sin red ni LLM."""


def score_final(signals):
    """Regla v4: el perfil incluye; la evidencia ordena, sin exigir una queja."""
    phone_evidence = any(signals.get(key, False) for key in (
        'phone_orders', 'phone_inquiries', 'shared_workload',
        'explicit_phone_issue', 'dedicated_phone_role'))
    if not phone_evidence:
        level, base = "Baja: perfil válido; evidencia telefónica pendiente", 10
    elif signals["historical_only"]:
        level, base = "Revalidar antecedente antiguo", 15
    elif signals["explicit_phone_issue"]:
        level, base = "Alta: dificultad telefónica publicada", 80
    elif signals["shared_workload"] or (signals["phone_orders"] and (signals["demand_peak"] or signals["capacity_constraint"])):
        level, base = "Media: hipótesis operativa respaldada", 50
    else:
        level, base = "Exploratoria: encaje y operación telefónica", 30
    # Señales distintas, presencia binaria: 20 citas no equivalen a 20 problemas.
    parts = {"base": base, "canal_pedidos": 5 * signals["phone_orders"],
             "tareas_compartidas": 5 * signals["shared_workload"],
             "demanda": 5 * signals["demand_peak"],
             "atribucion_local": 3 * signals["location_specific"],
             "texto_fuente_disponible": 3 * signals["source_text_available"],
             "publicacion_operativa_reciente": 3 * signals["recent_operational_publication"]}
    # Mantener bandas separadas: perfil 10–14, histórico 15–24, exploratorio 30–49,
    # hipótesis 50–69, dificultad explícita 80–99.
    cap = 4 if base == 10 else (9 if signals['historical_only'] else 19)
    bonus = min(cap, sum(v for k, v in parts.items() if k != "base"))
    repeated_locations = signals.get("verified_problem_locations", 0)
    if not signals["historical_only"] and signals["explicit_phone_issue"] and repeated_locations >= 2:
        bonus = min(19, bonus + min(15, 5 * (repeated_locations - 1)))
    return {"version": "prioridad-v4", "level": level, "score": base + bonus,
            "components": parts, "bonus_applied": bonus,
            "cross_location_bonus_available": repeated_locations >= 2}


def generate_from_files(locales_path, results_path, evidence_path, out_dir):
    """Entrega independiente: únicamente locales, evidencia y resultados nuevos."""
    import csv
    import json
    from datetime import date
    from pathlib import Path
    def read(path):
        with path.open(encoding='utf-8-sig', newline='') as f:
            return list(csv.DictReader(f))
    def write(path, fields, rows):
        with path.open('w', encoding='utf-8', newline='') as f:
            writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore',lineterminator='\n')
            writer.writeheader();writer.writerows(rows)
    locales, results, evidence = read(locales_path), read(results_path), read(evidence_path)
    by_company = {r['company_id']:r for r in results}
    by_evidence = {r['evidence_id']:r for r in evidence}
    columns=['company_name','city','state','locations_count','cuisine','phone','website','source_url','signal_1','signal_2','priority_score','why_now','notes']
    all_rows, audit = [], []
    for local in locales:
        cid=local.get('company_id') or local.get('project_company_id')
        result=by_company[cid]
        labels=json.loads(result['evidence_labels_json'] or '[]')
        usable=[r for r in labels if r['strength'] in {'direct','indirect'} and r['attribution'] != 'other_location']
        has=lambda topic:any(r['topic']==topic for r in usable)
        phone,shared,issue=has('phone_order_channel'),has('shared_staff_workload'),has('phone_service_issue')
        inquiries=has('phone_inquiry_channel')
        operator=any(r['topic']=='other' and 'phone operator' in r['verbatim_quote'].lower() for r in usable)
        operational=[r for r in usable if r['topic'] in {'phone_order_channel','phone_inquiry_channel','shared_staff_workload','phone_service_issue','demand_peak','wait_or_capacity'} or (operator and 'phone operator' in r['verbatim_quote'].lower())]
        signals={'phone_orders':phone,'shared_workload':shared,'explicit_phone_issue':issue,
                 'demand_peak':has('demand_peak'),'capacity_constraint':has('wait_or_capacity'),
                 'dedicated_phone_role':operator,'historical_only':False,
                 'phone_inquiries':inquiries,
                 'location_specific':any(r['attribution']=='this_location' for r in operational),
                 'source_text_available':bool(operational),'recent_operational_publication':False,
                 'verified_problem_locations':int(result['phone_problem_locations_count'] or 0)}
        dates=[by_evidence[r['evidence_id']].get('published_at','')[:10] for r in operational]
        valid_dates=[]
        for value in dates:
            try: valid_dates.append(date.fromisoformat(value))
            except ValueError: pass
        signals['recent_operational_publication']=any(0<=(date.today()-d).days<=365 for d in valid_dates)
        signals['historical_only']=bool(valid_dates) and len(valid_dates)==len(operational) and all((date.today()-d).days>365 for d in valid_dates)
        try: count=int(local.get('project_verified_location_count') or local.get('Number of Retail Locations') or 0)
        except ValueError: count=0
        country=(local.get('Company Country') or '').strip().lower()
        profile_ok=2<=count<=15 and country in {'united states','usa','us'}
        has_phone_evidence=bool(phone or inquiries or shared or issue or operator)
        # Elegibilidad y evidencia son dos ejes distintos. La falta de captura
        # nunca elimina una empresa que cumple el perfil de entrada.
        included=profile_ok
        evidence_status='con_senal_telefonica' if has_phone_evidence else 'evidencia_telefonica_pendiente'
        priority=score_final(signals) if included else {'version':'prioridad-v4','level':'Fuera del perfil de entrada','score':0,'components':{}}
        order={'phone_service_issue':0,'shared_staff_workload':1,'phone_order_channel':2,'phone_inquiry_channel':3,'demand_peak':4,'wait_or_capacity':5,'other':6}
        ordered=sorted(operational,key=lambda r:order[r['topic']])
        claims=[]
        for label in ordered:
            description=by_evidence[label['evidence_id']]['evidence_description']
            if description not in claims: claims.append(description)
        fallback='Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.'
        texts=[r['verbatim_quote'] for r in ordered]
        # Es una inferencia de categoría y queda explícita si solo viene del nombre.
        name=local.get('company_name') or local.get('Company Name')
        category_text=' '.join(r['verbatim_quote'] for r in usable).lower()
        cuisine=next((label for pattern,label in [('pizza','Pizza'),('barbecue','Barbacoa'),('bbq','Barbacoa'),('taco','Tacos / mexicana'),('burger','Hamburguesas'),('chicken','Pollo'),('deli','Deli / panadería')] if pattern in category_text),'Por confirmar')
        digits=''.join(c for c in (local.get('phone') or local.get('Company Phone') or '') if c.isdigit())
        if len(digits)==10:digits='1'+digits
        sources=list(dict.fromkeys(r['source_url'] for r in ordered))
        if not included:
            explanation='No cumple el perfil de entrada: revisar país y rango de 2–15 sucursales.'
        elif has_phone_evidence:
            explanation='Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. '+priority['level']
        else:
            explanation='Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente.'
        row={'company_name':name,'city':local.get('city') or local.get('Company City',''),'state':local.get('state') or local.get('Company State',''),
             'locations_count':count,'cuisine':cuisine,'phone':'+'+digits if digits else '', 'website':local.get('Website',''),
             'source_url':sources[0] if sources else local.get('Website',''),
             'signal_1':claims[0] if claims else f'Perfil según locales.csv: {count} sucursales en {local.get("Company Country", "país por confirmar")}; operación telefónica por validar.',
             'signal_2':claims[1] if len(claims)>1 else fallback,'priority_score':priority['score'],'why_now':explanation+' Sin novedad fechada confirmada.',
             'notes':f"Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: {local.get('location_label','')}. Fuentes operativas: {' | '.join(sources) if sources else 'ninguna en esta captura; source_url es la web de perfil, no una prueba de problema'}. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: {'prospecto_por_perfil' if included else 'fuera_de_perfil'}. Evidencia: {evidence_status}. Regla: {priority['version']}."}
        all_rows.append(row)
        audit.append({'company_id':cid,'company_name':name,'status':'prospecto_por_perfil' if included else 'fuera_de_perfil',
            'included_in_final':included,'evidence_status':evidence_status,'profile_fit_from_locales':profile_ok,
            'signals':signals,'priority':priority,'evidence_ids':[r['evidence_id'] for r in ordered],'analysis_status':result['analysis_status']})
    all_rows.sort(key=lambda r:(-r['priority_score'],r['company_name']))
    names={r['company_name'] for r in audit if r['included_in_final']}
    out_dir.mkdir(parents=True,exist_ok=True)
    write(out_dir/'candidatos_evaluados.csv',columns,all_rows)
    write(out_dir/'gtm-lista.csv',columns,[r for r in all_rows if r['company_name'] in names])
    (out_dir/'auditoria_prioridad.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    evidence_pending=sum(r['included_in_final'] and r['evidence_status']=='evidencia_telefonica_pendiente' for r in audit)
    print(f'Entrega independiente: {len(all_rows)} candidatos evaluados; {len(names)} incluidos por perfil, de los cuales {evidence_pending} tienen evidencia telefónica pendiente; {len(all_rows)-len(names)} fuera de perfil. Sin datos históricos.')
    return audit


def publish_final(execution_dir, project_root):
    """Publica una única entrega oficial desde el resultado comprobado."""
    import csv
    import json
    import shutil
    with (execution_dir/'gtm-lista.csv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    audit={r['company_name']:r for r in json.loads((execution_dir/'auditoria_prioridad.json').read_text())}
    assert len(rows)==len({r['company_name'] for r in rows})
    assert {r['company_name'] for r in rows}=={name for name,r in audit.items() if r['included_in_final']}
    for row in rows:
        assert int(row['priority_score'])==score_final(audit[row['company_name']]['signals'])['score']
    shutil.copyfile(execution_dir/'gtm-lista.csv',project_root/'gtm-lista.csv')
    def cell(value): return str(value).replace('|','\\|').replace('\n',' ')
    lines=['# Lista oficial y prioridad por empresa','',
        'Este documento se genera desde el CSV y la auditoría de la comprobación actual. La entrega de la raíz es una copia exacta de ese resultado; no mezcla puntajes históricos.',
        '',f'Se incluyen {len(rows)} prospectos por perfil. El perfil determina inclusión; la evidencia determina prioridad. Una fuente faltante o sin señales deja evidencia pendiente, sin descartar al prospecto ni inventar un problema.',
        '', '## Regla prioridad-v4','',
        'Perfil sin evidencia telefónica: 10–14. Antecedentes antiguos: 15–24. Canal exploratorio: 30–49. Hipótesis operativa: 50–69. Dificultad explícita: 80–99. Las bonificaciones usan presencia de señales, alcance, texto y recencia; varias citas no se convierten en varios incidentes. El puntaje no estima probabilidad de compra ni ganancia.',
        '', '[Arquitectura](ARQUITECTURA.md) · [Guía de ejecución](comprobacion_codex/README.md) · [Componentes de puntaje](comprobacion_codex/auditoria_prioridad.json)',
        '', '| Empresa | Prioridad | Evidencia | Puntos |','|---|---|---|---:|']
    for row in rows:
        entry=audit[row['company_name']]
        status='Señal telefónica' if entry['evidence_status']=='con_senal_telefonica' else 'Pendiente'
        lines.append(f"| {cell(row['company_name'])} | {cell(entry['priority']['level'])} | {status} | {row['priority_score']} |")
    for row in rows:
        entry=audit[row['company_name']];priority=entry['priority']
        lines += ['',f"## {row['company_name']}",'',
            f"**Argumento o dato de perfil:** {row['signal_1']}",'',
            f"**Segunda señal o pendiente:** {row['signal_2']}",'',
            f"**Prioridad:** base {priority['components']['base']} + bonificación aplicada {priority['bonus_applied']} = {priority['score']}.",'',
            f"**Validación comercial:** {row['why_now']}",'',
            f"**Trazabilidad y límites:** {row['notes']}"]
    (project_root/'LISTA-EXPLICADA.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'Entrega oficial actualizada: gtm-lista.csv y LISTA-EXPLICADA.md; {len(rows)} prospectos.')
