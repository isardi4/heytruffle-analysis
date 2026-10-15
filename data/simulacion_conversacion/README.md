# Ensayo LLM sin API

Las respuestas de este ensayo se prepararon manualmente en la conversación. No son salidas de la API. El script valida las citas contra el texto capturado y usa las funciones Python del pipeline para calcular indicadores. Cero llamadas y cero créditos.

```sh
python3 scripts/simular_llm_conversacion.py
python3 scripts/preparar_entrega.py
```

El primer comando escribe en esta carpeta:

- `evidencia_llm_procesada.csv`: 42 afirmaciones extraídas de los textos guardados.
- `resultados_evidencia_llm.csv`: indicadores para los 30 candidatos.
- `estado_simulacion.csv`: revisión de los 30 documentos capturados, correspondientes a 28 candidatos.
- `prompts_y_respuestas_simuladas.json`: prompts, esquemas, entradas y respuestas simuladas; incluye respuestas vacías y casos sin fuente. Describe 31 solicitudes de extracción y 20 de clasificación hipotéticas; las llamadas reales fueron cero.

El segundo comando genera la única entrega final, `gtm-lista.csv`, en la raíz. Combina estos indicadores con las fichas previas y etiquetas revisadas; las fuentes pendientes de recaptura se identifican en la entrega. El resultado del corpus capturado por sí solo no reemplaza la revisión completa de esos antecedentes. No hay otro CSV final ni una fórmula alternativa dentro de esta carpeta.
