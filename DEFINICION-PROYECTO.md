# Definición del proyecto

Identificar y priorizar posibles compradores de una solución de atención telefónica para restaurantes de EEUU, con 2–15 sucursales y cocina casual de volumen. La meta del ejercicio es 40 leads; la entrega del piloto conserva 30 investigados.

## Las partes del proceso

| Parte | Entrada → salida | Responsable |
|---|---|---|
| Obtener candidatos | Export de Apollo → `locales.csv` | Fuente externa; aceptamos el archivo del piloto. |
| Capturar fuentes | Webs de locales → `evidencia_locales.csv` | Python. |
| Extraer evidencia | Documentos → `evidencia_llm_procesada.csv` | LLM, con validación de citas por Python. |
| Generar indicadores | Afirmaciones → `resultados_evidencia_llm.csv` | Clasificación del LLM y agregación de Python. |
| Priorizar leads | Perfil e indicadores → `gtm-lista.csv` | Reglas de Python. |

**El perfil determina inclusión; la evidencia determina prioridad.** No exigimos demostrar un problema para considerar una empresa como posible cliente. Las señales ayudan a decidir a quién contactar primero.

Una ejecución nueva regenera las etapas desde `locales.csv`. Con API disponible se completa automáticamente; sin ella, Codex responde las solicitudes exportadas y Python continúa. Reproducir archivos guardados es un modo separado y explícito.

El [README](README.md) presenta la entrega; [Criterio](CRITERIO.md) explica la selección, [Arquitectura](ARQUITECTURA.md) detalla la implementación y la [guía](comprobacion_codex/README.md) indica cómo ejecutarla.
