# Prospección de restaurantes

Buscamos cadenas de Estados Unidos de 2–15 locales, con cocina casual de volumen y operación telefónica. Las señales públicas permiten elegir a quién contactar; una dificultad telefónica explícita aumenta la prioridad. No afirmamos que todos pierdan llamadas ni medimos su volumen telefónico.

## Entrega

- [gtm-lista.csv](gtm-lista.csv): lista final de 30 prospectos priorizados, con fuentes y motivos.
- [CRITERIO.md](CRITERIO.md): explicación breve del criterio, las fuentes y el uso de IA.
- [LISTA-EXPLICADA.md](LISTA-EXPLICADA.md): justificación por empresa y fórmula oficial de prioridad.
- [DEFINICION-PROYECTO.md](DEFINICION-PROYECTO.md): flujo de datos y alcance del piloto.

La meta era 40. Conservamos 30 casos investigados, sin agregar nombres solo para completar la cantidad; la consigna permite menos filas justificadas. Tres provienen de la revisión del export Free de Apollo de 25 cuentas; los otros 27 se propusieron con IA y se investigaron con fuentes públicas.

## Guía para la entrevista: ejecutar sin API

Este es el recorrido preparado para el viernes. No requiere una clave de API, saldo, Apollo conectado ni volver a descargar páginas. Sí requiere tener el proyecto completo y Python 3; en este entorno se probó con Python 3.13. Los comandos usan la biblioteca estándar, sin instalar paquetes.

### 1. Abrir el proyecto

Abrí esta carpeta en Codex y una terminal en su raíz. En esta computadora:

```sh
cd /Users/isardi4/Documents/GitHub/heytruffle-analysis
python3 --version
```

Si lo abrís en otra computadora, usá la ruta donde hayas copiado el proyecto. Conservá `data/`, `prompts/`, `scripts/` e `interno/`: sus entradas necesarias están versionadas para que un clon del repositorio pueda reproducir la entrega. `.env` no es necesario para este ensayo.

### 2. Mostrar las entradas ya preparadas

Abrí `data/locales.csv` y `data/evidencia_locales.csv`. El primero contiene los 30 candidatos; el segundo relaciona cada página y su texto con la empresa/sucursal mediante IDs. Hay 30 documentos con texto para 28 candidatos; dos descargas quedaron pendientes. No ejecutes el importador ni el recolector para repetir este ensayo: usamos la misma entrada guardada.

Explicación para acompañar la pantalla:

> “Apollo aporta candidatos. Como el plan Free limitó la exportación, completamos el piloto con candidatos propuestos por IA e investigados con fuentes públicas. Guardamos los textos para poder repetir el análisis sin depender de que una página cambie o deje de responder”.

### 3. Reproducir extracción, clasificación e indicadores

```sh
python3 scripts/simular_llm_conversacion.py
```

Este comando reproduce respuestas preparadas en la conversación, valida que las citas estén literalmente en las fuentes y ejecuta la agregación Python. No hace llamadas a servicios ni ejecuta un LLM nuevo. Si termina con un error, resolvelo antes de avanzar al siguiente comando.

Resultados esperados para el corpus actual:

- 30 documentos revisados, correspondientes a 28 candidatos con texto.
- 42 afirmaciones extraídas y validadas.
- Indicadores para los 30 candidatos; dos quedan sin texto fuente.
- Cero llamadas a la API.

Las salidas quedan en `data/simulacion_conversacion/`:

| Archivo | Qué mostrar |
|---|---|
| `evidencia_llm_procesada.csv` | Hechos, citas literales y URLs. |
| `resultados_evidencia_llm.csv` | Indicadores y etiquetas por empresa. |
| `estado_simulacion.csv` | Qué documentos produjeron evidencia. |
| `prompts_y_respuestas_simuladas.json` | Prompts exactos, entradas y respuestas simuladas de cada caso. |

Para explicar una empresa, por ejemplo Pequod’s, buscá su nombre en la traza. `instructions` contiene los prompts y esquemas; `extraction_cases` contiene cada texto recibido y la respuesta de extracción; `classification_cases` muestra cómo se etiquetaron los hechos. Separa pedidos por teléfono y picos de demanda de una falla telefónica explícita.

### 4. Generar el CSV final

```sh
python3 scripts/preparar_entrega.py
```

El script combina los indicadores anteriores con las fichas de investigación previa y sus etiquetas revisadas en `interno/indicadores-seleccion.json`. Algunas fuentes originales todavía no están en el corpus capturado; cada caso identifica esa procedencia y la recaptura pendiente. Ese paso de revisión asistida está guardado y no se presenta como una extracción automática nueva.

Python aplica la regla oficial de `scripts/priorizar_leads.py`, calcula los puntos y ordena. Actualiza:

- `gtm-lista.csv`: entrega final, 30 empresas y las 13 columnas solicitadas.
- `CRITERIO.md`: explicación breve del criterio.
- `LISTA-EXPLICADA.md`: motivos y cálculo por empresa.
- `interno/entrega-actual.json`: indicadores y componentes del puntaje para auditoría.

La salida esperada es **2 prioridades altas, 23 hipótesis operativas, 2 exploratorias y 3 antecedentes antiguos a revalidar**. Son posibles compradores con distintos niveles de respaldo, no 30 pérdidas de llamadas comprobadas. Repetir los comandos con las mismas entradas conserva la entrega final; la fecha de generación de la traza puede cambiar.

### 5. Pedirle a Codex que lo ejecute

Podés copiar este mensaje en una conversación nueva con el proyecto abierto:

```text
Necesito ensayar la entrega de este proyecto sin usar ninguna API.
Leé README.md y DEFINICION-PROYECTO.md. Usá los archivos locales existentes;
no vuelvas a consultar Apollo ni a descargar fuentes y no uses --run.
Ejecutá primero python3 scripts/simular_llm_conversacion.py.
Si termina bien, ejecutá python3 scripts/preparar_entrega.py.
Verificá 30 empresas únicas, las 13 columnas del template, puntajes calculados
y ordenados, y citas presentes en los textos fuente. Mostrame el resultado
resumido y explicame un caso siguiendo texto → hecho → indicador → prioridad.
No muestres .env ni claves. Si falla algo, diagnosticá el error y conservá
la evidencia original; no inventes hechos para obtener el resultado esperado.
```

### Si quiero que Codex haga una interpretación nueva en vivo

Lo anterior reproduce el ensayo guardado. Para mostrar una interpretación nueva del modelo, podemos usar la conversación de Codex como reemplazo manual de las dos llamadas LLM. No hace falta una clave de API del proyecto. Para que sea fácil de explicar y revisar, empezá con una empresa:

```text
Quiero simular en esta conversación las dos etapas LLM para Pequod's Pizza,
sin llamar a la API ni navegar. Leé prompts/extraer_evidencias.md y
prompts/clasificar_evidencias.md, y los esquemas JSON de sus scripts.
Leé solo sus documentos con source_text en data/evidencia_locales.csv y sus
IDs en data/locales.csv. Aplicá el prompt de extracción al texto original,
mostrame la respuesta estructurada y verificá cada cita literal con Python.
Después aplicá el prompt de clasificación a esas afirmaciones y mostrame
las etiquetas con el mismo esquema. No calcules prioridad con el LLM.
Compará tus respuestas con las guardadas en la traza de la simulación.
Si hay diferencias justificadas, explicalas y actualizá las respuestas
manuales correspondientes de scripts/simular_llm_conversacion.py, manteniendo
los IDs de empresa/sucursal, URLs, esquemas y procedencia simulada.
Regenerá la simulación y la entrega con los scripts y reportá qué cambió.
No cambies el criterio comercial ni las etiquetas históricas para forzar
un resultado. No muestres claves ni uses --run.
```

Para revisar todos los candidatos, pedí continuar por lotes pequeños con el mismo procedimiento. El simulador actual tiene respuestas manuales preparadas por URL: no genera respuestas nuevas para un export desconocido. Si cambian los textos o las empresas, hay que revisar esas respuestas y las fichas/etiquetas de selección antes de prometer una entrega completa. La conversación puede producir otra interpretación válida; lo reproducible es conservar sus entradas, prompts y respuestas, y volver a calcular con Python.

### Si algo falla durante la demostración

| Situación | Cómo continuar |
|---|---|
| No hay clave o saldo de API | Usar los dos comandos del ensayo; no agregar `--run`. |
| Falta un archivo de `interno/` | Recuperar la carpeta completa del proyecto; sus entradas no se reconstruyen inventando datos. |
| Una cita no aparece en el texto | Revisar texto y respuesta guardada con Codex; corregir o retirar la afirmación, no desactivar la validación. |
| Una página no responde | Usar el texto ya guardado; si nunca se capturó, conservar el estado pendiente. |
| Un dry-run no devuelve análisis | Es esperable sin caché: un dry-run no sustituye al LLM. Para el ensayo usar `simular_llm_conversacion.py`. |

## Archivos de entrada

- `data/locales.csv`: candidatos con IDs estables de empresa y sucursal.
- `data/evidencia_locales.csv`: URLs, texto original capturado y estado de descarga.
- `data/evidencia_resenas.csv`: entrada opcional, actualmente vacía, para reseñas de una fuente que permita exportarlas y analizarlas.

Los archivos se relacionan mediante `company_id` y `location_id`. El enlace `google_maps_url` de cada candidato sirve para revisión manual; no consulta Maps ni extrae reseñas y no va en la entrega final.

## Recorrido completo con adquisición y servicios

Esta sección muestra cómo se obtendrían entradas nuevas; no es necesaria para demostrar el piloto el viernes. Para otro export, trabajá en una copia del proyecto para conservar el caso preparado.

1. Exportar candidatos desde Apollo con el perfil acordado: EE. UU., cocina de volumen, empleados como aproximación inicial (15–300). Verificar después las 2–15 sucursales; los empleados no garantizan ese rango.
2. Normalizar el export y generar IDs estables.
3. Preparar búsquedas, revisar identidad y URLs, y capturar páginas originales. La búsqueda automática opcional usa Brave y requiere su propia configuración; no viene incluida por tener acceso a Codex.
4. Incorporar reseñas solo si la fuente permite exportación y análisis; este piloto no depende de ellas.
5. Extraer afirmaciones y clasificar con los dos scripts LLM.
6. Revisar elegibilidad, indicadores y procedencia, y generar el CSV con Python.

```sh
# Pasos 2 y 3: nuevas entradas; reemplazan archivos de trabajo
python3 scripts/importar_locales.py export-apollo.csv
python3 scripts/recolectar_evidencias.py

# Después de completar/revisar las URLs en evidencia_locales.csv
python3 scripts/recolectar_evidencias.py --results data/evidencia_locales.csv
```

El recolector no garantiza búsqueda ni captura completas. Si en este entorno macOS la descarga falla por certificados raíz, se puede usar `SSL_CERT_FILE=/etc/ssl/cert.pem` al ejecutar el recolector. Los dos scripts LLM no navegan: leen texto guardado.

Para las etapas LLM reales se necesita una clave con acceso y saldo, y un modelo disponible configurado localmente. `python3 scripts/configurar_openai.py` permite guardar la configuración; `.env` no debe compartirse. Estos comandos habilitan llamadas y **no son los del ensayo sin créditos**:

```sh
# Extracción real; procesa por defecto hasta 30 documentos con texto
python3 scripts/extraer_evidencias_llm.py --run

# Clasificación real; procesa por defecto hasta 30 empresas
python3 scripts/analizar_evidencias_llm.py --run
```

Generan `data/evidencia_llm_procesada.csv` y `data/resultados_evidencia_llm.csv`. Para continuar lotes, usar `--offset 30`, `--offset 60`, etc.; la caché y los estados quedan en `data/.pipeline/`. Revisar errores y completar el lote antes de generar la entrega. Los límites se aplican a documentos o empresas, respectivamente, no necesariamente a la misma cantidad de restaurantes.

Para los mismos 30 casos del piloto, una vez completos los indicadores reales, el generador permite elegirlos explícitamente:

```sh
python3 scripts/preparar_entrega.py --results data/resultados_evidencia_llm.csv
```

Este comando sigue integrando las fichas y etiquetas revisadas del piloto. No convierte el flujo en calificación automática de un export distinto: para empresas nuevas hay que preparar/revisar esas entradas y adaptar la selección del generador. No se validó una ejecución automática de miles de cuentas.

## Respaldo

`historico/` conserva decisiones y fuentes, incluida la revisión de Apollo. `interno/` contiene los registros de investigación necesarios para regenerar la entrega, el export original. El archivo comprimido de investigaciones anteriores es un respaldo local, excluido de Git y no necesario para ejecutar el flujo. No hace falta leerlos para seguir la ejecución principal.
