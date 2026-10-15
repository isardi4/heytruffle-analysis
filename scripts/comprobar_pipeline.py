#!/usr/bin/env python3
"""Por defecto inicia una corrida nueva, desde locales.csv, en una carpeta vacía.

--resume continúa esa misma corrida después de una intervención de Codex.
--replay reproduce una corrida guardada; --verify-only solo la verifica.
No usa fichas históricas ni el simulador CLAIMS.
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
from uuid import uuid4
from datetime import datetime, timezone

from load_local_env import load_local_env
from resolver_llm import resolve

ROOT = Path(__file__).resolve().parents[1]


def save_state(folder, state, stage, status, actor='python'):
    state['status']=status
    state['current_stage']=stage
    state['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
    state.setdefault('events',[]).append({'stage':stage,'status':status,'actor':actor,
                                        'at':state['updated_at']})
    (folder/'estado_ejecucion.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def collect_sources(folder, env):
    """Solo adquisición por el script: no recibe datos ni capturas anteriores."""
    command=[sys.executable,str(ROOT/'scripts/recolectar_evidencias.py'),
        '--locations',str(folder/'locales.csv'),'--evidence',str(folder/'evidencia_locales.csv'),
        '--output-dir',str(folder),'--discover-official','--max-pages','3','--workers','6',
        '--timeout','12','--delay','0']
    result=subprocess.run(command,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    with (folder/'ejecucion.log').open('a',encoding='utf-8') as stream:
        stream.write('\nCOMANDO: '+json.dumps(command,ensure_ascii=False)+'\n'+result.stdout)
    if result.returncode:
        raise RuntimeError('Falló la adquisición; revisar ejecucion.log')


def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_run_integrity(folder, origin):
    for name, expected in origin.get('implementation_hashes',{}).items():
        if not (ROOT/name).is_file() or sha(ROOT/name)!=expected:
            raise ValueError(f'El código o prompt cambió durante esta corrida: {name}. Iniciar otra corrida.')
    for name, expected in origin.get('acquisition_hashes',{}).items():
        if not (folder/name).is_file() or sha(folder/name)!=expected:
            raise ValueError(f'Se modificó una fuente capturada de esta corrida: {name}. Iniciar otra corrida.')


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
    check_run_integrity(folder,origin)
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
    assert all(int(r['api_chunks'])==0 for r in indicators)  # Transporte por archivos; procedencia real abajo.
    by_url={(r['company_id'],r['source_url']):r for r in documents if r['source_text']}
    for item in evidence:
        doc=by_url[(item['company_id'],item['source_url'])]
        assert item['source_quote'] in doc['source_text']
        raw=folder/'textos_originales'/(doc['evidence_id']+'.txt')
        assert item['source_quote'] in raw.read_text(encoding='utf-8')
    classified=[label for r in indicators for label in json.loads(r['evidence_labels_json'])]
    assert {r['evidence_id'] for r in classified}=={r['evidence_id'] for r in evidence}
    assert len(classified)==len(evidence)
    provenance=[]
    for kind,schema in [('extraccion',EXTRACTION_SCHEMA),('clasificacion',LABEL_SCHEMA)]:
        request_file=folder/f'solicitudes_{kind}.json'
        response_file=folder/f'respuestas_{kind}_codex.json'
        requests=json.loads(request_file.read_text())['requests']
        responses=json.loads(response_file.read_text())
        assert {r['request_id'] for r in requests}=={r['request_id'] for r in responses}
        for response in responses:
            validate(response['response'],schema)
            metadata=response.get('metadata',{})
            provenance.append({'provider':metadata.get('provider','codex_conversacion'),
                               'model':metadata.get('model') or 'no registrado'})
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
    execution_state=json.loads((folder/'estado_ejecucion.json').read_text()) if (folder/'estado_ejecucion.json').exists() else {}
    summary={'completed_at':datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'verdict':'PASS procesamiento desde respuestas registradas; cobertura de adquisición parcial',
        'trusted_input':'locales.csv','input_sha256':sha(folder/'locales.csv'),
        'run_origin':origin.get('execution_mode','historical_saved_run'),
        'run_id':origin.get('run_id','historical_saved_run'),
        'processing_mode':execution_state.get('invocation_mode','legacy_saved_run'),
        'code_and_prompts_unchanged_during_run':True if origin.get('implementation_hashes') else None,
        'captured_sources_unchanged_during_run':True if origin.get('acquisition_hashes') else None,
        'candidates':len(expected_ids),'captured_documents':capture_count,'companies_with_text':len(captured_ids),
        'claims':len(evidence),'classified_claims':len(classified),'final_prospects':len(final),
        'prospects_with_phone_evidence':sum(r['included_in_final'] and r['evidence_status']=='con_senal_telefonica' for r in audit),
        'prospects_pending_phone_evidence':sum(r['included_in_final'] and r['evidence_status']=='evidencia_telefonica_pendiente' for r in audit),
        'excluded_by_profile':len(expected_ids)-len(final),'selection_rule':'perfil incluye; evidencia prioriza (prioridad-v4)',
        'api_responses_saved':sum(r['provider']=='openai_api' for r in provenance),
        'codex_responses_saved':sum(r['provider']=='codex_conversacion' for r in provenance),
        'llm_providers':sorted({r['provider'] for r in provenance}),
        'llm_models':sorted({r['model'] for r in provenance}),
        'llm_execution':'Respuestas externas trazables por request_id; API o Codex según metadata. Sin CLAIMS ni fichas históricas.',
        'limitations':['No se probó exportación remota de Apollo; una respuesta guardada no demuestra disponibilidad actual de API.',
            'Adquisición acotada a Website y enlaces del mismo dominio (máximo 3 páginas por candidato en esta corrida).',
            'Pasajes seleccionados por palabras clave: el análisis no cubre el sitio completo.',
            'Con respuestas pendientes y API no disponible, requiere intervención manual de Codex.',
            'Perfil de locales se acepta como entrada; cocina y volumen telefónico requieren validación comercial.'],
        'script_hashes':{p.name:sha(p) for p in (ROOT/'scripts').glob('*.py') if p.name!='simular_llm_conversacion.py'},
        'hashes':{str(p.relative_to(folder)):sha(p) for p in folder.rglob('*') if p.is_file() and p.name not in {'verificacion.json','README.md','estado_ejecucion.json'} and p.suffix!='.log' and '.pipeline' not in p.parts}}
    (folder/'verificacion.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k!='hashes'},ensure_ascii=False,indent=2))
    return summary


def main():
    load_local_env()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=ROOT/'data/locales.csv')
    parser.add_argument('--out-dir',type=Path,help='Carpeta vacía para corrida nueva; existente solo con --resume/--replay/--verify-only.')
    parser.add_argument('--collect',action='store_true',help='Compatibilidad: la corrida nueva siempre adquiere fuentes.')
    action=parser.add_mutually_exclusive_group()
    action.add_argument('--resume',action='store_true',help='Continúa la misma corrida; no inicia otra ni vuelve a capturar.')
    action.add_argument('--replay',action='store_true',help='Reproduce artefactos guardados; no es una corrida nueva.')
    action.add_argument('--verify-only',action='store_true')
    parser.add_argument('--llm-mode', choices=['auto','codex'], default='auto', help='auto usa API para pendientes; codex nunca llama API.')
    parser.add_argument('--model', default=os.environ.get('OPENAI_MODEL',''))
    parser.add_argument('--api-timeout', type=int, default=60)
    args=parser.parse_args()
    existing=args.resume or args.replay or args.verify_only
    if existing and args.collect:
        parser.error('--collect no se combina con continuar/reproducir/verificar; iniciar otra corrida para adquirir fuentes nuevas.')
    if existing:
        if not args.out_dir:
            parser.error('Indicar --out-dir para elegir explícitamente la corrida existente.')
        out=args.out_dir.resolve()
        if not (out/'origen.json').is_file():
            raise ValueError('Falta origen.json: no es una corrida identificada.')
        if args.verify_only:
            verify(out,check_saved=True);return
        if args.resume and not (out/'estado_ejecucion.json').exists():
            raise ValueError('La corrida antigua no tiene estado; usar --replay explícitamente.')
        origin=json.loads((out/'origen.json').read_text())
        check_run_integrity(out,origin)
        if origin['sha256']!=sha(out/'locales.csv'):
            raise ValueError('Cambió locales.csv de esta corrida; iniciar otra.')
        state=json.loads((out/'estado_ejecucion.json').read_text()) if (out/'estado_ejecucion.json').exists() else {
            'run_id':origin.get('run_id','historical_saved_run'),'events':[]}
        if args.resume and state.get('status')=='completada':
            raise ValueError('Esta corrida ya terminó. Ejecutar sin --resume en otra carpeta para regenerar todo, o usar --replay.')
        print(f"{'CONTINUACIÓN de la misma corrida' if args.resume else 'REPRODUCCIÓN de archivos guardados'}: {out}")
    else:
        run_id=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'_'+uuid4().hex[:8]
        out=args.out_dir.resolve() if args.out_dir else ROOT/'ejecuciones'/run_id
        if out.exists() and any(out.iterdir()):
            raise ValueError('Una corrida nueva requiere una carpeta vacía. No se reutilizó ni borró ningún archivo. Usar otra carpeta o --resume/--replay explícitamente.')
        if args.input.resolve().is_relative_to(out):
            raise ValueError('El archivo de entrada debe estar fuera de la carpeta de salida nueva.')
        out.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(args.input,out/'locales.csv')
        origin={'only_trusted_input':'locales.csv','sha256':sha(out/'locales.csv'),
                'execution_mode':'fresh','run_id':run_id,
                'started_at':datetime.now(timezone.utc).isoformat(timespec='seconds'),
                'implementation_hashes':{str(p.relative_to(ROOT)):sha(p)
                    for base in ('scripts','prompts') for p in (ROOT/base).glob('*')
                    if p.suffix in {'.py','.md'} and p.name!='simular_llm_conversacion.py'},
                'llm_execution':'API o interpretación manual de Codex; sin archivos de otras corridas',
                'excluded':['capturas previas','respuestas previas','cachés previas','CLAIMS del simulador']}
        (out/'origen.json').write_text(json.dumps(origin,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        state={'run_id':run_id,'events':[]}
        print(f'CORRIDA NUEVA, solo locales.csv como entrada: {out}')
    state['invocation_mode']='resume' if args.resume else ('replay' if args.replay else 'fresh')
    save_state(out,state,'inicio','en_curso')
    reviews=out/'evidencia_resenas.csv'
    if not reviews.exists():reviews.write_text('evidence_id,company_id,location_id,company_name,source_url,source_text\n')
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
    if Path('/etc/ssl/cert.pem').exists():
        os.environ.setdefault('SSL_CERT_FILE','/etc/ssl/cert.pem')
        env.setdefault('SSL_CERT_FILE','/etc/ssl/cert.pem')
    def run(script,*arguments):
        cmd=[sys.executable,str(ROOT/'scripts'/script),*map(str,arguments)]
        completed=subprocess.run(cmd,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        with (out/'ejecucion.log').open('a',encoding='utf-8') as f:
            f.write('\nCOMANDO: '+json.dumps(cmd,ensure_ascii=False)+'\n'+completed.stdout)
        if completed.returncode:
            save_state(out,state,script,'error')
            print(completed.stdout)
            raise RuntimeError(f'Falló {script}; revisar ejecucion.log')
    if not existing:
        save_state(out,state,'adquisicion','en_curso')
        try:
            collect_sources(out,env)
        except Exception:
            save_state(out,state,'adquisicion','error')
            raise
        save_state(out,state,'adquisicion','etapa_completada')
        source_paths=[out/'evidencia_locales.csv',reviews]
        source_paths.extend((out/'textos_originales').glob('*.txt'))
        origin['acquisition_hashes']={str(p.relative_to(out)):sha(p) for p in source_paths if p.is_file()}
        (out/'origen.json').write_text(json.dumps(origin,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if not (out/'evidencia_locales.csv').exists():
        save_state(out,state,'adquisicion','error')
        raise ValueError('Falta evidencia_locales.csv de esta corrida. Iniciar otra corrida para adquirir fuentes nuevas.')
    # Contrato único por corrida nueva: una respuesta de otra corrida no coincide,
    # incluso cuando la web devuelve exactamente el mismo texto.
    # El proveedor y modelo efectivos se guardan por respuesta en metadata.
    contract_model='respuestas_externas_'+origin['run_id'] if origin.get('execution_mode')=='fresh' else 'codex_conversacion_nueva'
    stage_outcomes={}
    for kind, script, input_args in [
        ('extraccion','extraer_evidencias_llm.py',
         ['--documents',out/'evidencia_locales.csv','--reviews',reviews,'--max-documents',1000000]),
        ('clasificacion','analizar_evidencias_llm.py',
         ['--companies',out/'locales.csv','--evidence',out/'evidencia_llm_procesada.csv','--max-companies',1000000])]:
        responses=out/f'respuestas_{kind}_codex.json'
        requests=out/f'solicitudes_{kind}.json'
        command=[*input_args,'--out-dir',out,'--model',contract_model,'--requests',requests]
        # Exportar siempre las entradas de ESTA corrida antes de interpretar.
        save_state(out,state,kind,'en_curso')
        # El dry-run solo prepara solicitudes dentro de .pipeline; no reemplaza
        # los CSV de etapas interpretadas por salidas vacías o pendientes.
        export_command=[*input_args,'--out-dir',out/'.pipeline'/('preparacion_'+kind),
                        '--model',contract_model,'--requests',requests]
        run(script,*export_command)
        try:
            outcome=resolve(requests,responses,mode='codex' if args.replay else args.llm_mode,
                            api_key=os.environ.get('OPENAI_API_KEY',''),model=args.model,timeout=args.api_timeout)
        except Exception:
            save_state(out,state,kind,'error')
            raise
        stage_outcomes[kind]=outcome
        (out/'ejecucion_llm.json').write_text(json.dumps(stage_outcomes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        if not outcome['complete']:
            save_state(out,state,kind,'pendiente_codex','codex_manual')
            print(f'CORRIDA INCOMPLETA. Continuar después de interpretar: python3 scripts/comprobar_pipeline.py --resume --out-dir {out} --llm-mode {args.llm_mode}')
            return 2
        run(script,*command,'--responses',responses)
        save_state(out,state,kind,'etapa_completada','respuestas_externas_validadas')
    save_state(out,state,'entrega','en_curso')
    run('preparar_entrega.py','--locales',out/'locales.csv','--results',out/'resultados_evidencia_llm.csv',
        '--evidence',out/'evidencia_llm_procesada.csv','--out-dir',out)
    save_state(out,state,'verificacion','en_curso')
    try:
        verify(out)
    except Exception:
        save_state(out,state,'verificacion','error')
        raise
    save_state(out,state,'fin','completada')
    print(f'CORRIDA COMPLETADA: {out / "gtm-lista.csv"}')
    if out == ROOT/'comprobacion_codex':
        from priorizar_leads import publish_final
        publish_final(out,ROOT)


if __name__=='__main__':
    try:raise SystemExit(main() or 0)
    except (OSError,ValueError,AssertionError,RuntimeError) as exc:
        print(f'ERROR DE COMPROBACIÓN: {exc}',file=sys.stderr);raise SystemExit(1)
