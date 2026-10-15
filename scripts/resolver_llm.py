"""Resuelve solicitudes exportadas por API o deja pendientes para Codex.

No contiene decisiones comerciales ni respuestas de restaurantes.
"""
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from llm_archivos import load_responses, validate


def validate_answer(answer, request_input, schema):
    validate(answer, schema)
    if 'claims' in answer:
        for claim in answer['claims']:
            if not claim['source_quote'] or claim['source_quote'] not in request_input['source_text']:
                raise ValueError('Cita de extracción ausente del texto fuente')
    else:
        expected = {item['evidence_id']: item['content'] for item in request_input['evidence']}
        labels = answer['labels']
        if len(labels) != len(expected) or {r['evidence_id'] for r in labels} != set(expected):
            raise ValueError('La clasificación debe cubrir cada evidencia exactamente una vez')
        for label in labels:
            quote = label['verbatim_quote']
            if label['strength'] in {'direct', 'indirect'} and label['topic'] != 'none' and not quote:
                raise ValueError('Una señal requiere cita')
            if quote and quote not in expected[label['evidence_id']]:
                raise ValueError('Cita de clasificación ausente de su evidencia')


def api_answer(bundle, request_input, api_key, model, timeout):
    payload = {'model': model, 'instructions': bundle['instructions'],
        'input': json.dumps(request_input, ensure_ascii=False), 'store': False,
        'max_output_tokens': 6000,
        'text': {'format': {'type': 'json_schema', 'name': 'evidence_response',
                           'strict': True, 'schema': bundle['response_schema']}}}
    request = Request('https://api.openai.com/v1/responses', data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}, method='POST')
    with urlopen(request, timeout=timeout) as response:
        result = json.load(response)
    if result.get('status') != 'completed':
        raise ValueError('Respuesta API incompleta')
    output = ''.join(c.get('text', '') for o in result.get('output', []) if o.get('type') == 'message'
                     for c in o.get('content', []) if c.get('type') == 'output_text')
    answer = json.loads(output)
    validate_answer(answer, request_input, bundle['response_schema'])
    return answer, {'provider': 'openai_api', 'model': model, 'response_id': result.get('id', ''),
                    'usage': result.get('usage', {})}


def resolve(request_path, response_path, mode='auto', api_key='', model='', timeout=60):
    bundle = json.loads(request_path.read_text(encoding='utf-8'))
    records = json.loads(response_path.read_text(encoding='utf-8')) if response_path.exists() else []
    answers = load_responses(response_path if response_path.exists() else None)
    requests = {r['request_id']: r for r in bundle['requests']}
    if set(answers) - set(requests):
        raise ValueError('Respuestas de otra entrada o prompt: usar otra carpeta de ejecución')
    for key, answer in answers.items():
        validate_answer(answer, requests[key]['input'], bundle['response_schema'])
    attempts = 0
    reason = ''
    for key, item in requests.items():
        if key in answers:
            continue
        if mode == 'codex' or not api_key or not model:
            reason = 'Modo Codex o falta OPENAI_API_KEY / OPENAI_MODEL'
            break
        attempts += 1
        try:
            answer, metadata = api_answer(bundle, item['input'], api_key, model, timeout)
        except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError) as exc:
            # Nunca registrar cuerpos de error, claves ni textos de excepciones de red.
            reason = f'API no disponible o respuesta inválida ({type(exc).__name__}'
            reason += f', HTTP {exc.code})' if isinstance(exc, HTTPError) else ')'
            break
        records.append({'request_id': key, 'response': answer, 'metadata': metadata})
        answers[key] = answer
        response_path.write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    pending = [r for key, r in requests.items() if key not in answers]
    pending_path = request_path.with_name(request_path.stem+'_pendientes_codex.json')
    if pending:
        pending_path.write_text(json.dumps({**bundle, 'requests': pending}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(f'PENDIENTE CODEX: {len(pending)} solicitudes en {pending_path.name}. {reason}. '
              f'Agregar sus respuestas a {response_path.name} conservando las existentes y repetir el comando.')
    else:
        pending_path.unlink(missing_ok=True)
        if not response_path.exists():
            response_path.write_text('[]\n', encoding='utf-8')
    return {'complete': not pending, 'api_attempts': attempts, 'pending': len(pending), 'reason': reason}
