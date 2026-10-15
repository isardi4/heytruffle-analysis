# Prospección de restaurantes con IA

Identificamos posibles compradores de una solución de atención telefónica: restaurantes de EEUU, con 2–15 sucursales y cocina casual de volumen. **El perfil determina la inclusión; la evidencia determina la prioridad.**

La entrega contiene **30 leads** frente a una meta de 40: tres incorporaciones del export gratuito de Apollo y 27 del discovery con IA. Hay 14 con señales telefónicas y 16 con evidencia telefónica pendiente; todos se incluyen por perfil.

## El proceso

1. Partimos de [locales.csv](data/locales.csv), equivalente a una entrada de Apollo.
2. Python descarga páginas oficiales y guarda sus textos en `evidencia_locales.csv`.
3. Un LLM extrae afirmaciones con citas y las clasifica; Python genera los indicadores.
4. Python calcula la prioridad y genera `gtm-lista.csv`.

La obtención del export de Apollo queda fuera del piloto. El recolector consulta hasta tres páginas por empresa; las búsquedas externas y reseñas no están conectadas en el recorrido predeterminado.

## Ejecutar desde cero

Requiere Python 3.10+, Internet y `data/locales.csv` con el formato incluido. No necesita instalar paquetes. Configurá `OPENAI_API_KEY` y `OPENAI_MODEL` en el entorno o en `.env`, siguiendo [.env.example](.env.example), y ejecutá:

```sh
python3 scripts/comprobar_pipeline.py
```

Cada ejecución crea una carpeta nueva en `ejecuciones/`, vuelve a capturar e interpretar las fuentes y genera allí el CSV. No reutiliza resultados anteriores ni reemplaza automáticamente la entrega de la raíz. Las llamadas a la API pueden consumir créditos.

Si la API no está disponible, se detiene para interpretar las solicitudes con Codex. Para trabajar siempre sin API paga, usá `--llm-mode codex`. La [guía de ejecución con Codex](comprobacion_codex/README.md) incluye los pasos y un mensaje listo para copiar.

## Reproducir la entrega guardada

Sin API ni interpretación nueva:

```sh
python3 scripts/comprobar_pipeline.py --replay --out-dir comprobacion_codex
```

Este modo reconstruye la entrega desde las capturas y respuestas registradas. Las pruebas se ejecutan con `python3 -m unittest discover -s tests -v`.

## Qué revisar

- [CSV final](gtm-lista.csv): los 30 leads priorizados.
- [Criterio](CRITERIO.md): selección, prioridad y uso de IA.
- [Arquitectura](ARQUITECTURA.md): componentes, archivos y controles técnicos.
- [Explicación por lead](LISTA-EXPLICADA.md): señales y motivos del puntaje.

Se comprobó el flujo asistido con Codex y se probó el modo automático con API simulada; no se hizo una llamada paga real. Las señales ayudan a priorizar, sin afirmar que todos los leads pierdan llamadas. [historico/](historico/README.md) e [interno/](interno/README.md) conservan el discovery y no alimentan las corridas nuevas.
