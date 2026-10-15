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

## Ejecución rápida sin API

Requisitos: Python 3; verificado con Python 3.13. Se usa la biblioteca estándar, sin paquetes adicionales. Desde un clon completo del repositorio:

```sh
git clone https://github.com/isardi4/heytruffle-analysis.git
cd heytruffle-analysis
python3 -m unittest discover -s tests -v
python3 scripts/comprobar_pipeline.py
python3 scripts/comprobar_pipeline.py --verify-only
```

No se requiere `.env`, saldo ni conexión a Apollo/OpenAI. El procesamiento se reproduce desde textos y respuestas de Codex guardadas. **Repetir estos comandos no invoca un LLM nuevo:** valida las respuestas registradas y vuelve a calcular los indicadores y el CSV. La captura inicial sí se hizo por Internet y la interpretación nueva se hizo en la conversación de Codex; ambas quedan documentadas.

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
python3 scripts/comprobar_pipeline.py --input data/locales.csv --out-dir comprobacion_nueva --collect
```

Necesita Internet para las páginas públicas, pero no una API paga. El orquestador exporta las solicitudes y se detiene para que Codex interprete los documentos desde la conversación. Después recibe los JSON de respuestas y continúa. La [guía completa](comprobacion_codex/README.md#empezar-otra-comprobación-verdaderamente-desde-locales) contiene el prompt que se puede copiar en Codex, los formatos y el procedimiento. No se reutilizan interpretaciones de otra entrada sin validar su huella.

## Una sola entrega oficial

[gtm-lista.csv](gtm-lista.csv) es el resultado oficial. Se genera desde la comprobación actual y es idéntico a su CSV interno. [LISTA-EXPLICADA.md](LISTA-EXPLICADA.md) explica esos mismos puntajes y pendientes.

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
comprobacion_codex/        Capturas nuevas, solicitudes, respuestas y resultados
interno/                  Registros del discovery y export original de Apollo
historico/                Decisiones y fuentes de la investigación anterior
```

`company_id` y `location_id` relacionan empresas, sucursales y evidencias. El enlace de Google Maps en locales.csv es una referencia manual y no alimenta los indicadores. La entrada opcional de reseñas está vacía en esta comprobación.

Las claves y archivos `.env`, cachés, logs locales y el respaldo comprimido de investigación no se publican. Todos los datos y scripts necesarios para reproducir la comprobación están versionados. El export de Apollo conserva metadatos de cuenta; no se obtuvieron contactos personales de prospectos.

## Alcance comprobado

Se probó un flujo asistido por Codex con adquisición pública acotada, citas verificadas y prioridad calculada por Python. No se probó la exportación por API de Apollo, una llamada real al modelo por API ni una ejecución desatendida sobre miles de candidatos. El recolector sigue hasta tres páginas por candidato en esta corrida y selecciona pasajes: puede omitir fuentes útiles y encontrar bloqueos. Cocina, volumen de llamadas y necesidad comercial requieren validación adicional.

Las etapas LLM también tienen un modo `--run` para APIs, con configuración local; ese modo no es necesario para evaluar este piloto y no se ejecuta en los comandos anteriores. La arquitectura describe ambos caminos y sus límites.

## Respaldo del desarrollo

La documentación de `historico/` y los registros de `interno/` permiten auditar el discovery. El ensayo anterior de `scripts/simular_llm_conversacion.py` conserva respuestas preparadas dentro del código; no alimenta el proceso actual. El recorrido histórico se solicita explícitamente con `python3 scripts/preparar_entrega.py --legacy` y escribe sus salidas dentro de `historico/reproduccion_inicial/`.
