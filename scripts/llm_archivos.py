"""Contrato para ejecutar los mismos prompts mediante Codex y archivos JSON."""
import json


def validate(value, schema, path='$'):
    kind = schema['type']
    expected = {'object': dict, 'array': list, 'string': str}[kind]
    if not isinstance(value, expected):
        raise ValueError(f'{path}: se esperaba {kind}')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{path}: valor fuera del esquema')
    if kind == 'object':
        if set(schema.get('required', [])) - set(value):
            raise ValueError(f'{path}: faltan campos requeridos')
        if schema.get('additionalProperties') is False and set(value) - set(schema['properties']):
            raise ValueError(f'{path}: campos no permitidos')
        for key, item in value.items():
            if key in schema['properties']:
                validate(item, schema['properties'][key], f'{path}.{key}')
    elif kind == 'array':
        for index, item in enumerate(value):
            validate(item, schema['items'], f'{path}[{index}]')


def load_responses(path):
    if path is None:
        return {}
    records = json.loads(path.read_text(encoding='utf-8'))
    result = {}
    for record in records:
        key = record['request_id']
        if key in result:
            raise ValueError('request_id duplicado en respuestas externas')
        result[key] = record['response']
    return result


def save_requests(path, instructions, schema, requests):
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({'provenance': 'Entrada para interpretación NUEVA en Codex; sin llamada API',
            'instructions': instructions, 'response_schema': schema, 'requests': requests}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
