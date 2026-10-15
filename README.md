# Prospección de restaurantes con IA

Identificamos posibles compradores de una solución de atención telefónica: restaurantes de EEUU, con 2–15 sucursales y cocina casual de volumen. **El perfil determina la inclusión; la evidencia determina la prioridad.**

La entrega contiene **30 leads** frente a una meta de 40: tres incorporaciones del export gratuito de Apollo y 27 del discovery con IA. Todos se incluyen por perfil; la evidencia disponible define el orden de contacto.

## Por dónde empezar si estás evaluando el proyecto

| Orden | Documento | Qué permite evaluar |
|---|---|---|
| 1 | [Criterio](CRITERIO.md) | Perfil, selección, prioridad y uso de IA. |
| 2 | [Arquitectura](ARQUITECTURA.md) | Cómo se conectan las etapas y qué genera cada script. |
| 3 | [Guía de ejecución](comprobacion_codex/README.md) | Cómo correr desde cero, usar Codex o reproducir la entrega. |
| 4 | [CSV final](gtm-lista.csv) | Los 30 leads priorizados y sus señales. |
| 5 | [Explicación por lead](LISTA-EXPLICADA.md) | Justificación del puntaje y evidencia pendiente de cada caso. |

La [consigna](EJERCICIO.md) y la [definición del proyecto](DEFINICION-PROYECTO.md) completan el contexto. Para revisar el cálculo en detalle, está la [auditoría de prioridad](comprobacion_codex/auditoria_prioridad.json).

## Cómo llegamos a estos 30

El discovery dejó **154 candidatos con revisión registrada**, con distinta profundidad. La IA ayudó a proponer empresas, buscar y leer fuentes públicas y documentar las decisiones.

| Etapa | Candidatos revisados | Incorporados a la entrega |
|---|---:|---:|
| [Exploración inicial](interno/control-paso-4.json) | 29 | 12 |
| [Ampliación en diez tandas](historico/TANDAS.md) | 100 | 15 |
| [Export gratuito de Apollo](historico/APOLLO-REVISION.md) | 25 | 3 |
| **Total registrado** | **154** | **30** |

Los **27 provenientes del discovery con IA** son los 12 iniciales más las 15 incorporaciones. Se revisaron tamaño de cadena, actividad, identidad de marca y sucursal y señales de operación telefónica en webs, FAQ, empleos y testimonios públicos. En esa etapa se buscaban dos hechos útiles y atribuibles por caso.

Los otros 124 no se incorporaron: algunos excedían el rango de sucursales, estaban cerrados o no eran restaurantes comparables; otros tenían identidad dudosa, fuentes inaccesibles o respaldo operativo insuficiente. No todos quedan descartados como posibles clientes: podrían revisarse con mejores fuentes.

Estos 30 constituyen el lote elegido durante el discovery, no una clasificación exhaustiva de los 154 bajo la regla actual. El pipeline empieza desde ese lote en `locales.csv`: mantiene a quienes cumplen el perfil y usa la evidencia capturada nuevamente para ordenar el contacto. Por eso conserva leads aunque su evidencia telefónica quede pendiente.

## Resultado del piloto

| Indicador | Resultado |
|---|---:|
| Leads incluidos por perfil | 30 |
| Empresas con texto descargado | 28 |
| Páginas capturadas con texto | 76 |
| Afirmaciones respaldadas por citas | 56 |
| Leads con señales telefónicas | 14 |
| Leads con evidencia telefónica pendiente | 16 |
| Llamadas a APIs pagas en la entrega | 0 |

Los 16 pendientes siguen siendo posibles clientes y tienen menor prioridad. Una señal telefónica puede documentar pedidos o consultas; no implica por sí sola un problema de llamadas perdidas.

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

## Alcance comprobado

Se comprobó el flujo asistido con Codex y se probó el modo automático con API simulada; no se hizo una llamada paga real. Las señales ayudan a priorizar, sin afirmar que todos los leads pierdan llamadas. [historico/](historico/README.md) e [interno/](interno/README.md) conservan el discovery y no alimentan las corridas nuevas.
