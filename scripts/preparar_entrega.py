"""Genera el CSV vigente y su explicación desde los mismos registros. Sin consultas web."""
import csv
import json
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--results', type=Path, help='Indicadores por empresa; por defecto usa la comprobación actual.')
parser.add_argument('--locales', type=Path, help='Modo independiente: locales de entrada, sin fichas históricas.')
parser.add_argument('--evidence', type=Path, help='Modo independiente: afirmaciones extraídas en esta ejecución.')
parser.add_argument('--out-dir', type=Path, help='Modo independiente: carpeta de entrega aislada.')
parser.add_argument('--legacy', action='store_true', help='Reproduce el discovery anterior dentro de historico/reproduccion_inicial, sin reemplazar la entrega oficial.')
args = parser.parse_args()
if args.locales or args.evidence or args.out_dir:
    if not (args.locales and args.evidence and args.out_dir):
        parser.error('Modo independiente requiere --locales, --evidence y --out-dir')
    from priorizar_leads import generate_from_files
    generate_from_files(args.locales, args.results or ROOT/'comprobacion_codex/resultados_evidencia_llm.csv', args.evidence, args.out_dir)
    raise SystemExit(0)
if not args.legacy:
    from priorizar_leads import generate_from_files, publish_final
    execution=ROOT/'comprobacion_codex'
    generate_from_files(execution/'locales.csv',args.results or execution/'resultados_evidencia_llm.csv',execution/'evidencia_llm_procesada.csv',execution)
    publish_final(execution,ROOT)
    raise SystemExit(0)
args.results=args.results or ROOT/'data/simulacion_conversacion/resultados_evidencia_llm.csv'
LEGACY_OUT=ROOT/'historico/reproduccion_inicial'
LEGACY_OUT.mkdir(parents=True,exist_ok=True)
I = ROOT / 'interno'
CONTROL = json.loads((I / 'control-paso-4.json').read_text())
BY_NAME = {r['company_name']: r for r in CONTROL if r['selected_for_working_list']}
# Orden editorial: cercanía al problema, claridad del respaldo y vigencia.
ARGUMENTS = [
    ("Joe's Kansas City Bar-B-Que", 'Primera revisión',
     'Es el argumento publicado más directo sobre dificultad para comunicarse: la empresa pide reintentar si las líneas están ocupadas.',
     'Si parte de esas llamadas busca pedir o consultar, podría servir una atención que responda cuando el equipo no puede. Falta saber cuántas quedan sin atender y por qué.',
     'Cuando las líneas están ocupadas, ¿cuántas llamadas quedan sin atender y quién se encarga de ellas?',
     'Sin novedad fechada. La instrucción oficial de volver a llamar permite preguntar por las llamadas que no llegan a atender.',
     'No se midieron llamadas perdidas ni su causa. La web enlaza pickup online aunque el texto de contacto diga que no recibe pedidos online: no se afirma exclusividad telefónica.'),
    ("Pequod's Pizza", 'Primera revisión',
     'La empresa identifica un pico concreto de 18 a 20 y permite anticipar pedidos por teléfono; se puede plantear una pregunta operativa específica.',
     'Los pedidos telefónicos podrían competir con la atención presencial durante ese horario. No se comprobó que eso ocurra.',
     'Entre las 18 y las 20, ¿quién atiende los pedidos por teléfono y qué pasa si ya está atendiendo a otra persona?',
     'Sin novedad telefónica fechada. Revisar cobertura del pico publicado de 18 a 20; la demora de entrega de agosto de 2026 no se atribuye al teléfono.',
     'Los dos hechos principales provienen de la misma FAQ. Usan Whale Tale para ciertos retiros, lo que puede aliviar trabajo. Emily W relata demora de entrega el 26/08/2026 y Jasmine G entrega a tiempo el 26/09/2026; no se conoce la causa ni se suman puntos nuevos.'),
    ("Litza's Pizza", 'Primera revisión',
     'Hay una descripción oficial de mayo de 2026 del salón de Midvale lleno en noches de fin de semana, junto con la opción de pedir por teléfono.',
     'El salón concurrido y los pedidos telefónicos podrían pedir atención al mismo tiempo. La publicación no informa llamadas perdidas.',
     'Los viernes y sábados por la noche, ¿la misma persona atiende el salón y las llamadas? ¿Qué ocurre cuando coinciden?',
     'La nota oficial del 06/05/2026 permite preguntar por la cobertura telefónica de las noches de fin de semana en Midvale.',
     'Dos hechos de la misma página oficial. Comparte edificio con Hires Big H, que no cuenta como otra sede. La reseña de esperas de repartidores es del 27/05/2023: antecedente antiguo, sin llamada perdida comprobada.'),
    ("Bar-Bill Tavern", 'Primera revisión',
     'East Aurora admite pedidos por teléfono y publica mayor espera en fines de semana y un cierre del canal online al agotar capacidad.',
     'Podrían acumularse consultas mientras el equipo atiende el servicio. No sabemos si el cierre online hace aumentar las llamadas.',
     'Cuando se cierra el pedido online por capacidad, ¿aumentan las llamadas? ¿Las pueden atender o el límite es la cocina?',
     'Sin novedad fechada. Preguntar cómo cubren llamadas en fines de semana y al agotarse la capacidad del pedido online.',
     'El argumento es de East Aurora; no se traslada a Clarence o Rochester, que no aceptan esos pedidos telefónicos/online. El retiro de East Aurora no es una cuarta sede. Contestar más llamadas no aumenta la capacidad de cocina.'),
    ("Pappy's Smokehouse", 'Primera revisión',
     'Combina pedidos telefónicos oficiales con una experiencia presencial reciente que describe una hora de fila.',
     'Conviene preguntar si quienes atienden esa fila también responden pedidos remotos. La fila por sí sola no demuestra un problema telefónico.',
     'En los días con más fila, ¿los pedidos por teléfono los toma el mismo equipo? ¿Quedan llamadas sin atender?',
     'Reseña publicada el 17/08/2026 sobre una visita de julio: preguntar por cobertura telefónica en días concurridos.',
     'Una sola reseña sobre fila presencial. La misma autora dice que la comida llegó en menos de cinco minutos tras pedir: se conserva ese dato favorable. No se midieron llamadas perdidas.'),
    ("Black's Barbecue", 'Primera revisión, con límite de capacidad',
     'Publica una restricción concreta de pedidos cuando tiene mucho trabajo. Es una oportunidad condicionada a entender la causa.',
     'Podría necesitar ayuda para responder consultas o explicar límites. Si el único problema es que la cocina no puede preparar más comida, atender más pedidos no lo resuelve.',
     'Cuando solo aceptan pedidos presenciales, ¿es por capacidad de cocina o porque no pueden atender llamadas? ¿Se pierden también consultas que podrían responder?',
     'Sin novedad fechada. Distinguir un problema de atención de un límite de cocina antes de proponer una solución.',
     'Política oficial, no relato de llamada perdida. También hay pedidos online. No confundir con Terry Black’s. Si solo falta capacidad de cocina, este argumento no justifica vender atención telefónica.'),
    ("Glass Nickel Pizza", 'Validar antecedente antiguo',
     'El evento de Fitchburg relaciona dificultad telefónica y actividad adicional, pero es de marzo de 2025 y el organizador transmite relatos ajenos.',
     'Ese episodio puede servir para preguntar si vuelve a pasar durante promociones. No se presenta como una dificultad actual de la cadena.',
     'En la recaudación de marzo de 2025 hubo dificultades telefónicas reportadas: ¿volvieron a ocurrir en eventos posteriores y cómo las cubren hoy?',
     'Antecedente del 11/03/2025, fuera de los últimos 12 meses. Confirmar repetición y cambios en la atención; sin urgencia actual comprobada.',
     'Un evento y un organizador que transmite relatos de terceros. Los dos hechos salen del mismo episodio: suma una vez en comunicación, sin sumar de nuevo canal o pico. Hay comentarios favorables de entrega de 2026; no actualizan la queja telefónica ni se traslada a otras sedes.'),
    ("Prime Pizza", 'Validar funcionamiento',
     'El puesto de Brea combina teléfono, mostrador, cobro y empaquetado. Es una descripción local concreta, sin evidencia de falla.',
     'Compartir esas tareas puede hacer difícil responder en algún momento. Falta comprobar cómo se reparten por turno y si hay llamadas sin atender.',
     'En Brea, ¿el cajero sigue tomando llamadas mientras cobra y empaqueta? ¿Cómo cubren las llamadas cuando se juntan esas tareas?',
     'Sin novedad fechada. El aviso de cajero permite preguntar por el reparto actual de tareas en Brea; confirmar su vigencia.',
     'Aviso sin fecha de publicación comprobable: no se afirma contratación vigente ni falta de personal. Dos tareas del mismo puesto no son dos pruebas de llamadas perdidas. El directorio publica 13 sedes con datos de atención; se excluyen tres anunciadas. Los comentarios de comida de 2026 no prueban el problema.'),
    ("NY Pie Nashville", 'Validar funcionamiento',
     'El anuncio de Franklin asigna a caja llamadas, ingreso de pedidos, cobro y preparación de otros productos.',
     'La atención telefónica podría competir con esas tareas. La descripción del puesto no muestra una dificultad real ni falta de empleados.',
     'En Franklin, ¿caja atiende las llamadas mientras cobra y prepara productos? ¿Hay alguien que la cubra cuando se acumula trabajo?',
     'El anuncio de Franklin sirve para preguntar por la organización del puesto. Su fecha aparece de forma relativa; confirmar vigencia sin inventar una urgencia.',
     'Los dos hechos provienen del mismo anuncio. No hay una queja aceptada ni se suman puntos por contratar. El sitio también publica testimonios favorables sin fecha; no se toman como reseñas recientes verificadas.'),
    ("Salvatore's Tomato Pies", 'Validar funcionamiento y sucursal',
     'La descripción Host/Phone combina pedidos telefónicos, reservas y apoyo a camareros. Falta atribuir ese puesto a Madison.',
     'El reparto de tareas coincide con la hipótesis del ejercicio a nivel de cadena. No se comprobó que se aplique al contacto elegido.',
     'En Madison North Livingston, ¿el puesto Host/Phone también toma reservas y ayuda a los camareros? ¿Quién cubre las llamadas mientras lo hace?',
     'Sin novedad fechada. Confirmar primero que el puesto general Host/Phone corresponda a Madison y describa su operación actual.',
     'Aviso general sin sucursal ni fecha indicadas. Teléfono y dirección corresponden a Madison North Livingston; las tareas todavía no están confirmadas para esa sede. Sin llamada perdida ni falta de personal comprobadas.'),
    ("Downtown Pizza", 'Validar funcionamiento publicado en el código',
     'El código de la página oficial dice que se puede pedir por teléfono y que Toast suele ser más rápido cuando hay más trabajo. Es un respaldo menos visible.',
     'Puede haber una diferencia operativa entre canales. La comparación no demuestra llamadas perdidas ni permite identificar la causa.',
     'En Spartanburg, ¿por qué recomiendan Toast frente al teléfono cuando hay más trabajo? ¿La diferencia está en atender, tomar el pedido o prepararlo?',
     'Sin novedad fechada. Confirmar la vigencia de la comparación teléfono/Toast publicada en los datos de la web.',
     'Las respuestas están en los datos FAQ del código HTML, no visibles en el formulario: menor confianza y vigencia pendiente. No se suman puntos de falla ni presión. Spartanburg e Inman tienen sistemas separados. Las reseñas recientes de comida no prueban dificultad telefónica.'),
    ("Pizza Luce", 'Validar antecedente antiguo, menor prioridad',
     'Hay antecedentes de uso del teléfono y actividad en noches de partido en Downtown, pero son de 2022–2024 y la atención telefónica fue buena.',
     'Es una hipótesis histórica sobre coincidencia de tareas y demanda. Requiere confirmar canal y funcionamiento actuales antes de usarla comercialmente.',
     'En Downtown, ¿siguen tomando pedidos por teléfono y aumenta esa demanda en noches de partido? ¿Cómo cubren esas llamadas hoy?',
     'Antecedentes de 2022–2024, fuera de los últimos 12 meses. Sin disparador actual; confirmar primero canal y funcionamiento.',
     'La reseña telefónica del 14/10/2022 es favorable. Los relatos de actividad son de 2023–2024, de autores distintos. No se comprobó un comentario operativo reciente de Downtown ni llamadas perdidas. Puntaje histórico de 40, con menor prioridad comercial por antigüedad y relación indirecta con el problema.'),
]
assert len(ARGUMENTS) == len(BY_NAME) == 12  # Cohorte histórica preservada.
NEW = json.loads((I / 'ampliacion-seleccionados.json').read_text()) + json.loads((I / 'incorporaciones-25.json').read_text()) + json.loads((I / 'incorporaciones-tandas-09-10.json').read_text()) + json.loads((I / 'apollo/incorporacion-01.json').read_text())
BY_NAME.update({r['company_name']:r for r in NEW})
ARGUMENTS += [tuple(r['arguments']) for r in NEW]
ORDER = ["Joe's Kansas City Bar-B-Que", "Katie's Pizza & Pasta Osteria", "Pequod's Pizza", "Litza's Pizza", 'Bar-Bill Tavern', "Pappy's Smokehouse", "Mama's Pizza Omaha", "Black's Barbecue", 'Glass Nickel Pizza', 'Home Run Inn', 'SPIN! Pizza', 'Prime Pizza', 'NY Pie Nashville', 'V Pizza', "Salvatore's Tomato Pies", 'Pizzeria Delfina', "Zachary's Chicago Pizza", 'Downtown Pizza', 'Pizza Luce', 'Golden Boy Pizza']
ORDER.insert(7, 'HOTLIPS Pizza')
ORDER.insert(11, 'Crushed Red')
ORDER.insert(15, "Billy G's")
ORDER.insert(17, 'Holland Farms Bakery & Deli')
ORDER.insert(18, 'Birria LES')
ORDER.insert(16, 'Super Taco Mexican Restaurants')
ORDER.insert(20, 'Little Chef Chinese')
ORDER.append("The Kickin' Chicken")
ORDER.extend(["Sickies Garage Burgers & Brews", "Dallas BBQ"])
arguments_by_name={a[0]:a for a in ARGUMENTS}
ARGUMENTS=[arguments_by_name[name] for name in ORDER]
N=len(ARGUMENTS)
assert N == len(BY_NAME) == len(set(ORDER)) == 30
with (ROOT / 'gtm-lista-template.csv').open(newline='', encoding='utf-8') as f:
    columns = next(csv.reader(f))
assert len(columns) == 13
# La selección fue revisada con IA; Python calcula la prioridad y el orden.
import sys
from datetime import date
from urllib.parse import urlsplit
sys.path.insert(0, str(ROOT / 'scripts'))
from priorizar_leads import score_final

AS_OF = date(2026, 10, 15)
annotations = {r['company_name']: r for r in json.loads((I / 'indicadores-seleccion.json').read_text())}
assert set(annotations) == set(ORDER)
with args.results.open(newline='', encoding='utf-8-sig') as f:
    simulated_results = {r['company_name']: r for r in csv.DictReader(f)}
assert set(ORDER) <= set(simulated_results), 'Faltan empresas del piloto en el archivo de indicadores; completar el análisis del lote antes de generar la entrega.'
with (ROOT / 'data/evidencia_locales.csv').open(newline='', encoding='utf-8-sig') as f:
    captured = list(csv.DictReader(f))
def url_key(url):
    u = urlsplit(url)
    return u.netloc.lower().removeprefix('www.') + u.path.rstrip('/') + ('?' + u.query if u.query else '')
texts = {(r['company_name'], url_key(r['source_url'])) for r in captured if r.get('source_text', '').strip()}
age_labels = {'reciente':'Comentario operativo reciente', 'antiguo':'Comentario antiguo', 'sin_fecha':'Fecha pendiente', 'sin_comentario_pertinente_verificado':'Sin comentario pertinente verificado'}
export=[]
for name,group,reason,hypothesis,question,why_now,limit in ARGUMENTS:
    source = BY_NAME[name]
    indicators = dict(annotations[name])
    captured_result = simulated_results[name]
    indicators['captured_llm_indicators'] = {k: captured_result[k] for k in (
        'company_id', 'analysis_status', 'evidence_count', 'direct_phone_problem_mentions',
        'phone_order_channel_mentions', 'shared_workload_mentions', 'peak_demand_mentions',
        'phone_problem_locations_count', 'model', 'input_sha256')}
    # Solo sucursales con una dificultad atribuida, nunca total de la cadena.
    indicators['verified_problem_locations'] = int(captured_result['phone_problem_locations_count'] or 0)
    indicators['source_text_available'] = all((name, url_key(source[key])) in texts for key in ('source_url', 'signal_2_url'))
    published = indicators['operational_publication_date']
    indicators['recent_operational_publication'] = bool(published and 0 <= (AS_OF - date.fromisoformat(published)).days <= 365)
    priority = score_final(indicators)
    indicators['priority'] = priority
    # Los indicadores nuevos no convierten resúmenes anteriores en citas.
    analysis_origin = 'respuestas LLM simuladas' if captured_result['model'] == 'simulacion_chatgpt_no_api' else 'indicadores del archivo de resultados indicado; consultar su modelo y estado'
    provenance = (f'Texto de ambas fuentes disponible en la captura; {analysis_origin}.' if indicators['source_text_available'] else 'Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.')
    digits = ''.join(c for c in source['phone'] if c.isdigit())
    if len(digits)==11:
        assert digits.startswith('1'); digits=digits[1:]
    assert len(digits)==10
    notes = f"Sucursal: {source['branch']}. {limit} {indicators['limitation']} Por qué se elige: {reason} Qué validar: {question} Prioridad: {priority['level']}; regla {priority['version']}. Procedencia: {provenance} Fuente de señal 2: {source['signal_2_url']} Perfil y contacto: {source['profile_source']} Fuentes investigadas al 14/10/2026; cálculo al {AS_OF.isoformat()}."
    row={k:source[k] for k in columns if k in source}
    row.update(phone='+1'+digits,why_now=why_now,notes=notes,priority_score=priority['score'])
    if name=="Salvatore's Tomato Pies":
        row['signal_1']='La descripción general Host/Phone de la cadena incluye tomar pedidos por teléfono; confirmar que corresponda a Madison.'
    assert set(row)==set(columns)
    export.append(dict(group=priority['level'],reason=reason,hypothesis=hypothesis,question=question,
        indicators=indicators,comment_age=age_labels[source['comment_age_group']],
        has_recent_comment=source['has_recent_comment'],source_2=source['signal_2_url'],
        profile_source=source['profile_source'],provenance=provenance,row=row))
export.sort(key=lambda e: (-e['row']['priority_score'],e['row']['company_name']))
for rank, e in enumerate(export, 1): e['rank']=rank
with (LEGACY_OUT/'gtm-lista.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=columns,lineterminator='\n');writer.writeheader();writer.writerows(e['row'] for e in export)
(I/'entrega-actual.json').write_text(json.dumps(export,ensure_ascii=False,indent=2)+'\n')
def cell(value):return str(value).replace('|','\\|').replace('\n','<br>')
lines=['# Los 30 prospectos del CSV, explicados','','La lista contiene posibles compradores, priorizados para validar la necesidad. Todos tienen encaje de perfil y una señal de operación telefónica en la investigación previa. No se exige una queja para incluirlos. No se comprobó que los 30 pierdan llamadas.','','## Selección y procedencia','','Se revisaron cadenas de 2–15 locales en EE. UU., cocina casual de volumen y pedidos para llevar. Se conservaron las que tenían pedidos telefónicos, tareas que incluyen llamadas o un rol telefónico explícito, junto con contexto para formular una pregunta comercial. Dos señales pueden provenir de la misma publicación; no representan dos incidentes independientes. Los 27 candidatos de IA y tres de Apollo se revisaron con fuentes públicas; el nombre sugerido por IA no es evidencia.','','Se integra la investigación original con el reproceso sobre texto capturado. Una captura sin señal o una descarga fallida no anula una fuente revisada anteriormente. Cuando no está el texto en el corpus actual, se declara pendiente de recaptura; no se lo presenta como una extracción LLM nueva.','','## Prioridad calculada por Python','','Regla prioridad-v4: base 10–14 para perfil válido sin evidencia telefónica; base 80 para dificultad telefónica explícita; 50 para tareas compartidas con el teléfono o pedidos telefónicos junto con demanda/límite de capacidad; 30 para evidencia exploratoria de canal u operación telefónica; 15 si el argumento depende de antecedentes antiguos. Antigüedad se aplica antes que las otras bandas.','','Bonificaciones por presencia de señales: canal de pedidos +5, tareas compartidas +5, demanda +5, atribución a la sucursal +3, texto de ambas fuentes disponible +3, publicación operativa fechada en los últimos 365 días +3. El total de bonificaciones se limita a 4 puntos para perfil sin evidencia telefónica, 19 para señales telefónicas, o 9 para antecedentes antiguos. Si una dificultad explícita estuviera atribuida a varias sucursales, +5 por sucursal adicional, máximo +15 dentro del mismo límite de 19; hoy no hay cobertura para aplicar ese bono. Varias citas no se cuentan como incidentes. El número de locales de la cadena no es el número de locales afectados.','','El puntaje ordena la investigación y el contacto; no estima ingresos, disposición de compra ni porcentaje de llamadas perdidas. El volumen telefónico no está medido. Las políticas de espera, las vacantes y las colas presenciales se explican como señales indirectas. La fecha de captura no se usa como fecha de publicación. Empates: nombre de empresa. Cálculo reproducible con fecha de corte 2026-10-15.','','| Orden | Empresa | Prioridad | Puntos |','|---|---|---|---:|']
for e in export:
    lines.append(f"| {e['rank']} | {cell(e['row']['company_name'])} | {e['group']} | {e['row']['priority_score']} |")
for e in export:
    r=e['row']; p=e['indicators']['priority']
    lines += ['',f"## {e['rank']}. {r['company_name']}",'',f"**Motivo de inclusión:** {e['reason']}",'',f"**Utilidad posible:** {e['hypothesis']}",'',f"**Qué validar:** {e['question']}",'',f"**Procedencia:** {e['provenance']}",'',f"**Cálculo:** base {p['components']['base']} + bono aplicado {p['bonus_applied']} = {p['score']}. Componentes: {json.dumps(p['components'],ensure_ascii=False)}.",'','| Campo | Valor |','|---|---|']
    for key in columns: lines.append(f"| `{key}` | {cell(r[key])} |")
lines += ['','## Alcance de la entrega','','30 filas frente a una meta de 40. Se conserva la selección investigada y no se agregan empresas sin argumento para completar la cantidad. El ejercicio permite menos filas con una explicación. Apollo aportó tres incorporaciones de su export de 25; los otros 27 nombres se propusieron con IA y se investigaron. Ver historico/APOLLO-REVISION.md y los respaldos de historico/. No se contactó a los restaurantes.']
(LEGACY_OUT/'LISTA-EXPLICADA.md').write_text('\n'.join(lines)+'\n')
criterion = """# Criterio de selección

Seleccionamos **30 cadenas de Estados Unidos, con 2–15 locales, cocina casual de volumen y pedidos para llevar**. Las tratamos como posibles compradores: no afirmamos que todas pierdan llamadas. El argumento de inclusión es uso del teléfono para pedidos, llamadas dentro de un puesto que también atiende clientes o un rol telefónico explícito, con contexto para validar una necesidad. Picos publicados, tareas compartidas, esperas y restricciones de pedidos aumentan el interés; una dificultad telefónica explícita eleva la prioridad. No se midió el volumen de llamadas.

**Obtención y selección.** Apollo Free permitió exportar 25 cuentas; tres pasaron la revisión de perfil y señales. Los otros 27 casos proceden del discovery con IA y búsquedas públicas. Se descartaron identidades dudosas, empresas inactivas, cadenas fuera de rango y candidatos sin argumento operativo suficiente. La entrega quedó en 30 frente a la meta de 40: se priorizó justificar los casos y la consigna admite menos filas. No es una muestra representativa ni toda la lista procede de Apollo.

**Fuentes.** Webs oficiales para sedes, canales y políticas; publicaciones del empleador para tareas; testimonios públicos fechados para experiencias. Un puesto de trabajo no demuestra una vacante urgente ni falta de personal; una cola no prueba llamadas perdidas. Cada fila enlaza sus fuentes y explica límites. Los antecedentes antiguos y las atribuciones a cadena se identifican. No se inventan cantidades de quejas ni sucursales afectadas.

**IA y automatización.** La IA propuso candidatos, ayudó a investigar y a estructurar señales. En el ensayo sin presupuesto, las respuestas de extracción/clasificación se simularon y sus citas se validaron contra texto guardado. La entrega integra además fichas de investigación previa con enlaces: si el texto no está en la captura, se declara pendiente de recaptura. Python une los registros, aplica una fórmula explícita a indicadores revisados, ordena y genera el CSV y las fichas. La persona definió el objetivo, dirigió las decisiones y debe validar el criterio comercial. Las reglas, los componentes de cada puntaje y cómo regenerar la entrega están en LISTA-EXPLICADA.md y README.md. El puntaje expresa prioridad de contacto, no probabilidad de compra ni ganancia esperada.
"""
(LEGACY_OUT/'CRITERIO.md').write_text(criterion)

if __name__ == '__main__':
    with (LEGACY_OUT/'gtm-lista.csv').open(newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f);actual=list(reader);assert reader.fieldnames==columns
    assert len(actual)==N and len({r['company_name'] for r in actual})==N
    scores=[int(r['priority_score']) for r in actual]
    assert scores==sorted(scores,reverse=True)
    md=(LEGACY_OUT/'LISTA-EXPLICADA.md').read_text()
    for row,e in zip(actual,export):
        assert int(row['priority_score']) == score_final(e['indicators'])['score']
        for key in columns:
            assert row[key]==str(e['row'][key])
            assert f"| `{key}` | {cell(row[key])} |" in md
        assert 2<=int(row['locations_count'])<=15
        assert row['phone'].startswith('+1') and len(row['phone'])==12
        assert row['signal_1'] and row['signal_2'] and e['reason']
        assert not row['company_name'].startswith('EXAMPLE')
    from collections import Counter
    print('Generados y verificados: gtm-lista.csv, LISTA-EXPLICADA.md, CRITERIO.md y entrega-actual.json; 30 empresas únicas, 13 columnas, prioridad calculada y ordenada.')
    print(dict(Counter(e['group'] for e in export)))
