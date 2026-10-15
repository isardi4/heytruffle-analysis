# Definición del proyecto

Queremos identificar y priorizar posibles compradores de una solución de atención telefónica para restaurantes. El perfil objetivo es una cadena de EE. UU., con 2–15 locales y cocina casual de volumen. La meta del ejercicio es 40 casos; el piloto conserva 30 investigados y explica esa diferencia.

## Reglas de negocio

- El perfil determina inclusión. En la comprobación aceptamos `locales.csv` como entrada validada; el código controla país y rango de sucursales, no vuelve a certificar toda la información comercial.
- La evidencia determina prioridad. Pedidos y consultas por teléfono, tareas compartidas y picos ayudan a elegir el orden de contacto. Una dificultad telefónica explícita aumenta la prioridad.
- Falta de captura significa evidencia pendiente. No implica ausencia de necesidad ni elimina un prospecto del perfil.
- El puntaje no estima ganancia, intención de compra ni llamadas perdidas. Las menciones no representan cantidades de incidentes.

## Flujo actual

```text
locales.csv → captura de páginas → evidencia_locales.csv
                                  ↓
                        LLM: extracción con citas
                                  ↓
                      evidencia_llm_procesada.csv
                                  ↓
                     LLM: clasificación por evidencia
                                  ↓
                       Python: indicadores por empresa
                                  ↓
                      resultados_evidencia_llm.csv
                                  ↓
                       Python: inclusión y prioridad
                                  ↓
                              gtm-lista.csv
```

La adquisición arranca de Website y sigue enlaces publicados del mismo dominio. Cada fuente conserva URL, fecha de captura y texto. En este piloto Codex interpreta las solicitudes desde la conversación y guarda respuestas JSON externas; Python valida esquema, identidad y citas. Repetir el procesamiento usa esas respuestas registradas, sin un modelo nuevo ni una API.

## Estado comprobado

La ejecución independiente está en [comprobacion_codex/](comprobacion_codex/README.md). Evaluó 30 candidatos, capturó texto para 28 empresas y produjo 56 afirmaciones. Incluye 30 prospectos: 14 con señales telefónicas y 16 con evidencia pendiente. La cobertura de adquisición es parcial. La prueba se pudo regenerar sin fichas históricas y sin red desde los archivos guardados.

El origen de candidatos combina tres incorporaciones del export gratuito de Apollo y 27 propuestas con IA e investigadas. La exportación remota de Apollo y el uso del modelo por API permanecen fuera de lo comprobado. El importador actual normaliza un CSV existente; no descarga cuentas desde Apollo.

La entrega oficial de la raíz se copia del resultado independiente actual. El discovery inicial tiene fuentes e interpretaciones anteriores y se conserva en historico/entrega_inicial/; no alimenta la comprobación nueva. Su investigación fue más profunda y dirigida que la captura acotada de esta prueba.

Para evaluar la implementación, seguí [README.md](README.md), [ARQUITECTURA.md](ARQUITECTURA.md) y la [guía de comprobación](comprobacion_codex/README.md).
