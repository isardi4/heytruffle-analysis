#!/usr/bin/env python3
"""Comprobación independiente desde locales.csv; Codex responde por archivos.

Sin --collect reproduce la prueba desde las capturas y respuestas de su carpeta.
Con --collect vuelve a adquirir páginas (las respuestas anteriores pueden caducar).
Nunca habilita llamadas de API ni usa fichas históricas o el simulador CLAIMS.
"""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]


def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(folder, check_saved=False):
    from llm_archivos import validate
    from priorizar_leads import score_final
    from extraer_evidencias_llm import SCHEMA as EXTRACTION_SCHEMA
    from analizar_evidencias_llm import LABEL_SCHEMA
    if check_saved and (folder/'verificacion.json').exists():
        previous=json.loads((folder/'verificacion.json').read_text())
        for name,expected in previous.get('hashes',{}).items():
            assert (folder/name).exists() and sha(folder/name)==expected, f'Archivo modificado desde la verificación: {name}'
        if folder == ROOT/'comprobacion_codex':
            assert sha(ROOT/'gtm-lista.csv')==sha(folder/'gtm-lista.csv'), 'La entrega oficial difiere de la comprobación; regenerar el proceso'
    origin=json.loads((folder/'origen.json').read_text())
    assert origin['sha256']==sha(folder/'locales.csv'), 'La entrada validada cambió'
    source=rows(folder/'locales.csv')
    documents=rows(folder/'evidencia_locales.csv')
    evidence=rows(folder/'evidencia_llm_procesada.csv')
    indicators=rows(folder/'resultados_evidencia_llm.csv')
    final=rows(folder/'gtm-lista.csv')
    audit=json.loads((folder/'auditoria_prioridad.json').read_text())
    expected_ids={r['company_id'] for r in source}
    assert len(audit)==len(expected_ids)==len(indicators)
    assert {r['company_id'] for r in audit}==expected_ids
    assert all(r['analysis_status'] in {'complete','awaiting_source_text'} for r in indicators)
    assert all(r['model']=='codex_conversacion_nueva' and int(r['api_chunks'])==0 for r in indicators)
    by_url={(r['company_id'],r['source_url']):r for r in documents if r['source_text']}
    for item in evidence:
        doc=by_url[(item['company_id'],item['source_url'])]
        assert item['source_quote'] in doc['source_text']
        raw=folder/'textos_originales'/(doc['evidence_id']+'.txt')
        assert item['source_quote'] in raw.read_text(encoding='utf-8')
    classified=[label for r in indicators for label in json.loads(r['evidence_labels_json'])]
    assert {r['evidence_id'] for r in classified}=={r['evidence_id'] for r in evidence}
    assert len(classified)==len(evidence)
    for kind,schema in [('extraccion',EXTRACTION_SCHEMA),('clasificacion',LABEL_SCHEMA)]:
        request_file=folder/f'solicitudes_{kind}.json'
        response_file=folder/f'respuestas_{kind}_codex.json'
        requests=json.loads(request_file.read_text())['requests']
        responses=json.loads(response_file.read_text())
        assert {r['request_id'] for r in requests}=={r['request_id'] for r in responses}
        for response in responses:
            validate(response['response'],schema)
    expected_fields=['company_name','city','state','locations_count','cuisine','phone','website','source_url','signal_1','signal_2','priority_score','why_now','notes']
    with (folder/'gtm-lista.csv').open() as f:
        assert next(csv.reader(f))==expected_fields
    by_name={r['company_name']:r for r in audit}
    # Contrato de negocio: el CSV incluye todos los candidatos del perfil,
    # incluso si la descarga o la interpretación no aportaron señales.
    profile_names=set()
    for local in source:
        try: count=int(local.get('project_verified_location_count') or local.get('Number of Retail Locations') or 0)
        except ValueError: count=0
        country=(local.get('Company Country') or '').strip().lower()
        if 2<=count<=15 and country in {'united states','usa','us'}:
            profile_names.add(local.get('company_name') or local.get('Company Name'))
    assert {r['company_name'] for r in final}==profile_names, 'Se perdieron prospectos válidos o se incluyeron empresas fuera de perfil'
    assert len({r['company_name'] for r in final})==len(final)
    assert [int(r['priority_score']) for r in final]==sorted([int(r['priority_score']) for r in final],reverse=True)
    for r in final:
        item=by_name[r['company_name']]
        assert item['status']=='prospecto_por_perfil' and item['included_in_final']
        assert int(r['priority_score'])==score_final(item['signals'])['score']
    capture_count=sum(bool(r['source_text']) for r in documents)
    captured_ids={r['company_id'] for r in documents if r['source_text']}
    summary={'completed_at':datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'verdict':'PASS flujo asistido por Codex sobre las fuentes capturadas; cobertura de adquisición parcial',
        'trusted_input':'locales.csv','input_sha256':sha(folder/'locales.csv'),
        'candidates':len(expected_ids),'captured_documents':capture_count,'companies_with_text':len(captured_ids),
        'claims':len(evidence),'classified_claims':len(classified),'final_prospects':len(final),
        'prospects_with_phone_evidence':sum(r['included_in_final'] and r['evidence_status']=='con_senal_telefonica' for r in audit),
        'prospects_pending_phone_evidence':sum(r['included_in_final'] and r['evidence_status']=='evidencia_telefonica_pendiente' for r in audit),
        'excluded_by_profile':len(expected_ids)-len(final),'selection_rule':'perfil incluye; evidencia prioriza (prioridad-v4)','api_calls':0,
        'llm_execution':'Interpretaciones NUEVAS de Codex guardadas como respuestas externas; no se importó CLAIMS ni fichas históricas.',
        'limitations':['No se probó exportación remota de Apollo ni llamada OpenAI API.',
            'Adquisición acotada a Website y enlaces del mismo dominio (máximo 3 páginas por candidato en esta corrida).',
            'Pasajes seleccionados por palabras clave: el análisis no cubre el sitio completo.',
            'No es ejecución desatendida: Codex interpreta y guarda los JSON entre etapas.',
            'Perfil de locales se acepta como entrada; cocina y volumen telefónico requieren validación comercial.'],
        'script_hashes':{p.name:sha(p) for p in (ROOT/'scripts').glob('*.py') if p.name!='simular_llm_conversacion.py'},
        'hashes':{str(p.relative_to(folder)):sha(p) for p in folder.rglob('*') if p.is_file() and p.name not in {'verificacion.json','README.md'} and p.suffix!='.log' and '.pipeline' not in p.parts}}
    (folder/'verificacion.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k!='hashes'},ensure_ascii=False,indent=2))
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=ROOT/'data/locales.csv')
    parser.add_argument('--out-dir',type=Path,default=ROOT/'comprobacion_codex')
    parser.add_argument('--collect',action='store_true')
    parser.add_argument('--verify-only',action='store_true')
    args=parser.parse_args()
    out=args.out_dir.resolve()
    if args.verify_only:
        verify(out,check_saved=True);return
    out.mkdir(parents=True,exist_ok=True)
    if not (out/'locales.csv').exists():
        shutil.copyfile(args.input,out/'locales.csv')
    elif sha(out/'locales.csv')!=sha(args.input):
        raise ValueError('locales.csv difiere de --input. Elegir otra carpeta para otra entrada.')
    if not (out/'origen.json').exists():
        (out/'origen.json').write_text(json.dumps({'only_trusted_input':'locales.csv',
            'sha256':sha(out/'locales.csv'),'llm_execution':'Codex en conversación; respuestas nuevas separadas del código; sin API',
            'excluded':['interno/','data/evidencia_locales.csv','data/simulacion_conversacion/','CLAIMS del simulador']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    reviews=out/'evidencia_resenas.csv'
    if not reviews.exists():reviews.write_text('evidence_id,company_id,location_id,company_name,source_url,source_text\n')
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
    if Path('/etc/ssl/cert.pem').exists():env.setdefault('SSL_CERT_FILE','/etc/ssl/cert.pem')
    def run(script,*arguments):
        cmd=[sys.executable,str(ROOT/'scripts'/script),*map(str,arguments)]
        completed=subprocess.run(cmd,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        with (out/'ejecucion.log').open('a',encoding='utf-8') as f:
            f.write('\nCOMANDO: '+json.dumps(cmd,ensure_ascii=False)+'\n'+completed.stdout)
        if completed.returncode:
            print(completed.stdout)
            raise RuntimeError(f'Falló {script}; revisar ejecucion.log')
    if args.collect:
        run('recolectar_evidencias.py','--locations',out/'locales.csv','--evidence',out/'evidencia_locales.csv',
            '--output-dir',out,'--discover-official','--max-pages',3,'--workers',6,'--timeout',12,'--delay',0)
    if not (out/'evidencia_locales.csv').exists():
        raise ValueError('Falta captura nueva; ejecutar con --collect para obtenerla desde locales.csv.')
    responses=out/'respuestas_extraccion_codex.json'
    command=['--documents',out/'evidencia_locales.csv','--reviews',reviews,'--out-dir',out,'--model','codex_conversacion_nueva',
        '--max-documents',1000,'--requests',out/'solicitudes_extraccion.json']
    if responses.exists():command+=['--responses',responses]
    run('extraer_evidencias_llm.py',*command)
    if not responses.exists():
        print('PENDIENTE CODEX: interpretar solicitudes_extraccion.json y guardar respuestas_extraccion_codex.json. Luego repetir sin --collect.');return
    responses=out/'respuestas_clasificacion_codex.json'
    command=['--companies',out/'locales.csv','--evidence',out/'evidencia_llm_procesada.csv','--out-dir',out,'--model','codex_conversacion_nueva',
        '--max-companies',1000,'--requests',out/'solicitudes_clasificacion.json']
    if responses.exists():command+=['--responses',responses]
    run('analizar_evidencias_llm.py',*command)
    if not responses.exists():
        print('PENDIENTE CODEX: interpretar solicitudes_clasificacion.json y guardar respuestas_clasificacion_codex.json. Luego repetir sin --collect.');return
    run('preparar_entrega.py','--locales',out/'locales.csv','--results',out/'resultados_evidencia_llm.csv',
        '--evidence',out/'evidencia_llm_procesada.csv','--out-dir',out)
    verify(out)
    if out == ROOT/'comprobacion_codex':
        from priorizar_leads import publish_final
        publish_final(out,ROOT)


if __name__=='__main__':
    try:main()
    except (OSError,ValueError,AssertionError,RuntimeError) as exc:
        print(f'ERROR DE COMPROBACIÓN: {exc}',file=sys.stderr);raise SystemExit(1)
