# Definición del proyecto

El proyecto identifica posibles compradores de una solución de atención telefónica para restaurantes. Buscamos cadenas de EE. UU., de 2–15 locales y cocina de volumen. El uso del teléfono justifica investigar; las tareas compartidas, los picos o una dificultad publicada ayudan a priorizar el contacto. El puntaje no estima ganancia ni demuestra llamadas perdidas.

## Flujo diseñado

```text
Apollo / otra fuente → locales.csv
Páginas públicas → evidencia_locales.csv ──┐
Reseñas autorizadas → evidencia_resenas.csv ┴→ LLM: extracción de hechos
                                             ↓
                              evidencia_llm_procesada.csv
                                             ↓
                                     LLM: clasificación
                                             ↓
                                  Python: indicadores
                                             ↓
                              resultados_evidencia_llm.csv
                                             ↓
                               Revisión de elegibilidad
                                             ↓
                               Python: prioridad y orden
                                             ↓
                                      gtm-lista.csv
```

`locales.csv` identifica las empresas y sucursales. Las entradas de evidencia conservan URLs y texto original. El primer LLM separa hechos y aporta citas literales; Python verifica que estén en el texto. El segundo LLM clasifica las señales sin inventar incidentes. Python agrega indicadores por empresa y sucursal. La etapa final aplica reglas de selección y prioridad, y genera las 13 columnas solicitadas.

Se usan `company_id` y `location_id` para relacionar los archivos. Varias sucursales con el mismo problema son una señal relevante; no se cuentan varias citas de un mismo episodio como incidentes distintos. Una fuente faltante significa desconocimiento, no ausencia de problemas.

## Cómo ejecutamos este piloto

Tenemos 30 candidatos: tres incorporados desde Apollo y 27 propuestos con IA e investigados. Hay 30 documentos capturados para 28 candidatos; Bar-Bill Tavern y Mama's Pizza Omaha rechazaron la descarga con HTTP 403. La entrada de reseñas está vacía. Los enlaces de Google Maps son referencias para revisión manual y no alimentan el análisis.

Para evitar llamadas a la API, las respuestas de extracción y clasificación se prepararon en la conversación. `scripts/simular_llm_conversacion.py` reproduce esas respuestas, valida 42 citas y genera los indicadores en `data/simulacion_conversacion/`. La traza conserva los prompts, entradas y respuestas por caso. No ejecuta un LLM nuevo en cada corrida.

La captura actual no incluye todas las fuentes de la investigación original. Por eso el generador integra los indicadores simulados con las fichas previas y `interno/indicadores-seleccion.json`, etiquetas revisadas con IA. Esa procedencia se declara en cada caso; los resúmenes previos no se convierten en citas verificadas. Para que todos los casos recorran íntegramente el flujo diseñado falta recapturar esas fuentes.

`scripts/preparar_entrega.py` hace esa unión, calcula el puntaje mediante `scripts/priorizar_leads.py` y genera la entrega final. La fórmula y la explicación de cada empresa están en `LISTA-EXPLICADA.md`. `interno/entrega-actual.json` conserva los indicadores y componentes de cálculo.

Para ejecutar los dos pasos sin API, seguí [README.md](README.md). El proceso conectado a servicios está implementado por etapas; todavía requiere supervisión y no se validó como ejecución automática sobre miles de candidatos.
