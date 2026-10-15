# Ejecutar y reproducir el pipeline

Esta carpeta conserva la corrida de la entrega: 30 leads, 76 capturas con texto y 56 afirmaciones con citas. La interpretación se hizo con Codex, sin API paga. El detalle técnico está en [Arquitectura](../ARQUITECTURA.md).

## Corrida nueva con API

Desde la raíz, con `data/locales.csv`, `OPENAI_API_KEY` y `OPENAI_MODEL` configurados:

```sh
python3 scripts/comprobar_pipeline.py
```

Obtiene las páginas, solicita extracción y clasificación al LLM y genera indicadores, prioridad y CSV. Cada corrida empieza desde cero en `ejecuciones/<fecha_id>/`. La API real permanece sin probar; el recorrido automático y su recuperación se verificaron con conexiones simuladas.

## Corrida nueva con Codex, sin API paga

Elegí una carpeta que no exista o esté vacía:

```sh
python3 scripts/comprobar_pipeline.py --out-dir ejecuciones/demo --llm-mode codex
```

El proceso captura fuentes y se detiene en dos momentos:

| Momento | Codex lee | Codex guarda |
|---|---|---|
| Extracción | `solicitudes_extraccion_pendientes_codex.json` | `respuestas_extraccion_codex.json` |
| Clasificación | `solicitudes_clasificacion_pendientes_codex.json` | `respuestas_clasificacion_codex.json` |

Después de cada intervención, continuá la misma corrida:

```sh
python3 scripts/comprobar_pipeline.py --resume --out-dir ejecuciones/demo --llm-mode codex
```

Podés copiar este mensaje en Codex:

```text
Continuá la corrida de ejecuciones/demo, sin usar APIs pagas.
Leé las solicitudes *_pendientes_codex.json de la etapa pendiente y aplicá
sus instrucciones y esquema a cada entrada. Guardá las respuestas como una
lista de objetos con request_id, response y metadata.provider=codex_conversacion
en el archivo respuestas_*_codex.json correspondiente. Conservá las respuestas
parciales de esta misma corrida y agregá solo las faltantes.
No uses fichas, respuestas ni capturas de otras corridas. No modifiques scripts,
prompts, textos fuente, indicadores ni el CSV final para completar la ejecución.
Después ejecutá:
python3 scripts/comprobar_pipeline.py --resume --out-dir ejecuciones/demo --llm-mode codex
Repetí para la clasificación hasta completar y verificar la entrega. Si hay
un error de software, informalo en vez de fabricar una salida.
```

Python valida las respuestas y genera los CSV. `estado_ejecucion.json` indica `pendiente_codex` o `completada`; el comando devuelve 2 mientras espera intervención, 1 ante error y 0 al completar. El CSV nuevo queda en `ejecuciones/demo/gtm-lista.csv`. Para empezar otra vez desde cero, elegí otra carpeta sin `--resume`.

## Reproducir o verificar la entrega existente

```sh
python3 scripts/comprobar_pipeline.py --replay --out-dir comprobacion_codex
python3 scripts/comprobar_pipeline.py --verify-only --out-dir comprobacion_codex
```

`--replay` reutiliza capturas y respuestas guardadas sin llamar a la API; reconstruye el CSV y actualiza la copia oficial de la raíz. `--verify-only` solo controla los archivos existentes. Ninguno obtiene fuentes ni interpretaciones nuevas.

La corrida guardada incluye los 30 leads del perfil: 14 con señales telefónicas y 16 pendientes. La cobertura fue parcial y dos webs bloquearon las descargas; las ausencias de evidencia reducen la prioridad, sin eliminar al lead.
