# Prospección de restaurantes con IA

Pipeline de prospección para cadenas de restaurantes de Estados Unidos, de 2–15 locales y cocina casual de volumen. **El perfil determina la inclusión; las evidencias determinan la prioridad.** El objetivo comercial es identificar posibles compradores de una solución para atender llamadas de pedidos y consultas durante el servicio.

El piloto tiene 30 prospectos frente a una meta de 40. Tres provienen de la revisión de un export Free de Apollo y 27 del discovery asistido por IA. Los candidatos propuestos por IA se investigaron; el nombre sugerido no es evidencia. No afirmamos que los 30 pierdan llamadas ni que tengan intención de compra confirmada.

## Por dónde empezar si estás evaluando el proyecto

| Orden | Documento | Qué permite evaluar |
|---|---|---|
| 1 | [Criterio](CRITERIO.md) | Perfil, inclusión, prioridades y uso de IA, en una explicación breve. |
| 2 | [Arquitectura](ARQUITECTURA.md) | Componentes, contratos de datos, decisiones y límites. |
| 3 | [Comprobación reproducible](comprobacion_codex/README.md) | Cómo se ejecutó desde locales.csv y cómo repetirla sin APIs. |
| 4 | [CSV oficial](gtm-lista.csv) | Los 30 prospectos, ordenados con evidencia nueva y pendientes explícitos. |
| 5 | [Auditoría de prioridad](comprobacion_codex/auditoria_prioridad.json) | Indicadores y componentes de cada puntaje. |

[Definición del proyecto](DEFINICION-PROYECTO.md) resume el alcance. [EJERCICIO.md](EJERCICIO.md) conserva la consigna. Las fuentes y los respaldos están disponibles para profundizar, sin necesidad de leerlos todos.

## Ejecutar desde cero

Requisitos: Python 3.10 o superior (verificado con Python 3.13), acceso a Internet y `data/locales.csv` con el contrato de entrada del piloto. Se usa la biblioteca estándar, sin paquetes adicionales. La obtención del export de Apollo queda fuera de esta ejecución.

Con `OPENAI_API_KEY` y `OPENAI_MODEL` configurados en el entorno o `.env`:

```sh
python3 scripts/comprobar_pipeline.py
```

**Cada invocación sin opciones de continuación inicia una corrida nueva**, en `ejecuciones/<fecha_id>/`. Copia únicamente `locales.csv`, vuelve a descargar las páginas y solicita nuevas interpretaciones a la API; después genera evidencias, indicadores, prioridad y `gtm-lista.csv`. No lee capturas, respuestas ni cachés de corridas anteriores. El comando informa la ruta del CSV nuevo; la entrega guardada en la raíz no se reemplaza automáticamente.

Si falta la API o falla, la corrida queda explícitamente **incompleta**. Codex solo interpreta las solicitudes pendientes y escribe sus respuestas JSON; no modifica los scripts, las evidencias fuente, los indicadores ni el CSV final. Después se continúa esa misma corrida:

```sh
python3 scripts/comprobar_pipeline.py --resume --out-dir ejecuciones/<fecha_id>
```

Para iniciar desde cero sin permitir llamadas pagas, usar `--llm-mode codex`. La continuación después de cada interpretación usa también `--resume --llm-mode codex`. Una carpeta no vacía se rechaza si no se solicita continuar o reproducir explícitamente. Las corridas tienen IDs propios: respuestas de otra corrida no se aceptan aunque los textos coincidan.

`estado_ejecucion.json` registra etapa, estado y actor; `ejecucion_llm.json`, los intentos de API y pendientes de la invocación; `verificacion.json` existe al completar los controles. El comando termina con código 0 si completa, 2 si espera a Codex y 1 si hay un error. Se registran las huellas del código, prompts y textos capturados; si se modifican durante una corrida nueva, no se permite continuarla como si fuera la misma ejecución.

## Reproducir la entrega guardada sin API

Esto permite inspeccionar el piloto entregado, pero **no es una adquisición ni una interpretación nueva**:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/comprobar_pipeline.py --replay --out-dir comprobacion_codex
python3 scripts/comprobar_pipeline.py --verify-only --out-dir comprobacion_codex
```

`--replay` reutiliza únicamente los archivos de la carpeta elegida y no llama APIs pagas. Reconstruye los CSV desde esas capturas y respuestas guardadas. `--verify-only` comprueba los archivos sin ejecutar las etapas.

Resultado de la corrida actual:

| Indicador | Resultado |
|---|---:|
| Candidatos evaluados y prospectos incluidos | 30 |
| Empresas con texto descargado | 28 |
| Capturas con texto | 76 |
| Afirmaciones con cita literal | 56 |
| Prospectos con señal telefónica | 14 |
| Prospectos con evidencia telefónica pendiente, incluidos con prioridad baja | 16 |
| Llamadas a APIs de pago | 0 |

La verificación falla si desaparece del CSV un candidato que cumple el perfil. Las pruebas incluyen pérdida total de evidencia: los prospectos válidos permanecen, sin inventar señales. También se verificó la regeneración en una copia aislada sin datos históricos, cachés ni salidas previas y con la red bloqueada.

## Cómo hacer una interpretación nueva con Codex

Para adquirir fuentes nuevas desde el mismo listado, en otra carpeta:

```sh
python3 scripts/comprobar_pipeline.py --input data/locales.csv --out-dir comprobacion_nueva --llm-mode codex
```

Necesita Internet para las páginas públicas, pero no una API paga. El orquestador exporta las solicitudes y se detiene para que Codex interprete los documentos desde la conversación. Después recibe los JSON de respuestas y continúa usando `--resume --out-dir comprobacion_nueva --llm-mode codex`. La [guía completa](comprobacion_codex/README.md#empezar-otra-comprobación-verdaderamente-desde-locales) contiene el prompt que se puede copiar en Codex, los formatos y el procedimiento. No se reutilizan interpretaciones de otra entrada sin validar su huella.

## Una sola entrega oficial

[gtm-lista.csv](gtm-lista.csv) es el resultado oficial. Se genera desde la comprobación actual y es idéntico a su CSV interno. [LISTA-EXPLICADA.md](LISTA-EXPLICADA.md) explica esos mismos puntajes y pendientes.

La cocina se toma de un campo explícito `cuisine` o `project_cuisine` de `locales.csv`, si existe. En su ausencia, se infiere del nombre, descripción o palabras clave del perfil mediante términos completos; la procedencia y la necesidad de validación quedan en las notas y la auditoría. No se deduce de las citas sobre atención telefónica. Los casos ambiguos quedan como “Por confirmar”; la categoría no modifica el puntaje.

La [entrega inicial del discovery](historico/entrega_inicial/README.md) queda como respaldo histórico. Su investigación fue más dirigida y profunda que la captura acotada de la comprobación; por eso puede tener otras señales y prioridades. No se mezcla con la entrega actual ni se restaura al ejecutar los comandos principales.

```sh
# Solo regenerar el último paso y actualizar la entrega oficial
python3 scripts/preparar_entrega.py
```

## Estructura del repositorio

```text
scripts/                  Adquisición, etapas LLM, prioridad y orquestación
tests/                    Pruebas de inclusión y prioridad
prompts/                  Instrucciones versionadas de extracción/clasificación
data/locales.csv          Entrada de candidatos aceptada para el piloto
comprobacion_codex/        Corrida guardada de la entrega evaluada
ejecuciones/              Corridas nuevas, separadas por fecha e ID
interno/                  Registros del discovery y export original de Apollo
historico/                Decisiones y fuentes de la investigación anterior
```

`company_id` y `location_id` relacionan empresas, sucursales y evidencias. El enlace de Google Maps en locales.csv es una referencia manual y no alimenta los indicadores. La entrada opcional de reseñas está vacía en esta comprobación.

Las claves y archivos `.env`, cachés, logs locales y el respaldo comprimido de investigación no se publican. Todos los datos y scripts necesarios para reproducir la comprobación están versionados. El export de Apollo conserva metadatos de cuenta; no se obtuvieron contactos personales de prospectos.

## Alcance comprobado

Se probó un flujo asistido por Codex con adquisición pública acotada, citas verificadas y prioridad calculada por Python. No se probó la exportación por API de Apollo, una llamada real al modelo por API ni una ejecución desatendida sobre miles de candidatos. El recolector sigue hasta tres páginas por candidato en esta corrida y selecciona pasajes: puede omitir fuentes útiles y encontrar bloqueos. Cocina, volumen de llamadas y necesidad comercial requieren validación adicional.

El coordinador usa `--llm-mode auto` por defecto: en una corrida nueva interpreta desde cero; al continuar la misma corrida, conserva el progreso y para las pendientes intenta la API si están configurados `OPENAI_API_KEY` y `OPENAI_MODEL` en el entorno o `.env`. La conexión usa [Structured Outputs de OpenAI](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses). Si la API falla o falta configuración, guarda el progreso, exporta `solicitudes_*_pendientes_codex.json` y termina sin publicar resultados parciales. Codex interpreta esas solicitudes desde la conversación y agrega sus respuestas al JSON indicado; después se continúa con `--resume`. No se invoca Codex automáticamente.

Para permitir la API y completar las dos etapas sin intervención si funciona:

```sh
python3 scripts/comprobar_pipeline.py --input data/locales.csv --out-dir comprobacion_api --llm-mode auto
```

Este modo puede consumir créditos; cada respuesta exitosa se guarda inmediatamente para evitar repetirla al reanudar. Si una llamada falla antes de guardarse, no se puede garantizar que el proveedor no la haya facturado. Para garantizar cero llamadas pagas, usar `--llm-mode codex`. El camino automático y su recuperación se prueban con API simulada; no se hizo una llamada paga real. También se prueba cambiar locales.csv: el resultado contiene únicamente las empresas de la nueva entrada, con su cantidad de sucursales y categoría, sin arrastrar empresas anteriores.

Las respuestas son datos, no decisiones incrustadas en el coordinador: contienen `request_id`, `response` y, para respuestas API, `metadata` con proveedor, modelo real, identificador y uso de tokens. Las respuestas históricas sin metadata corresponden a Codex. El nombre `respuestas_*_codex.json` se conserva por compatibilidad. Las corridas nuevas usan una etiqueta de contrato `respuestas_externas_<run_id>`; la etiqueta antigua solo se usa al reproducir el piloto guardado. El campo `model` de los CSV intermedios identifica ese contrato; el modelo API real se registra en metadata, no en esa etiqueta. La procedencia efectiva se consulta en metadata y en `verificacion.json`.

## Respaldo del desarrollo

La documentación de `historico/` y los registros de `interno/` permiten auditar el discovery. El ensayo anterior de `scripts/simular_llm_conversacion.py` conserva respuestas preparadas dentro del código; no alimenta el proceso actual. El recorrido histórico se solicita explícitamente con `python3 scripts/preparar_entrega.py --legacy` y escribe sus salidas dentro de `historico/reproduccion_inicial/`.
