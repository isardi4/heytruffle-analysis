# Comprobación nueva de punta a punta con Codex

## Qué se comprobó

**Se completó el recorrido asistido por Codex desde `locales.csv` hasta un CSV nuevo, sin importar evidencia, interpretaciones ni etiquetas históricas.** La ejecución no fue desatendida: Codex leyó las solicitudes y preparó respuestas nuevas en esta conversación. Python validó y procesó esas respuestas.

La prueba no demuestra una conexión con Apollo ni una llamada a OpenAI API. Tampoco garantiza encontrar toda la evidencia de cada restaurante. La adquisición tuvo cobertura parcial y dos webs rechazaron la descarga. La entrega oficial de la raíz se actualiza desde el CSV de esta carpeta y debe ser idéntica. El discovery anterior está preservado en historico/entrega_inicial/.

## Resultado observado

| Etapa | Resultado |
|---|---:|
| Candidatos del único archivo aceptado | 30 |
| Páginas intentadas en la captura útil | 79 |
| Capturas con texto | 76 |
| Empresas con al menos una captura | 28 |
| Solicitudes de extracción interpretadas de nuevo | 76 |
| Afirmaciones y citas validadas | 56 |
| Solicitudes de clasificación interpretadas de nuevo | 26 |
| Empresas evaluadas en el resultado | 30 |
| Prospectos incluidos por perfil en el CSV final | 30 |
| Incluidos con señal telefónica en esta captura | 14 |
| Incluidos con evidencia telefónica pendiente | 16 |
| Excluidos por estar fuera del perfil | 0 |
| Llamadas a APIs de pago | 0 |

Los 30 permanecen en el CSV. Entre los 14 con señal telefónica hay una prioridad alta (Joe’s), seis hipótesis operativas y siete casos exploratorios. Los otros 16 tienen prioridad baja y evidencia telefónica pendiente. Las consultas y reservas telefónicas se identifican por separado de los pedidos de comida: también pueden motivar contacto, con prioridad exploratoria. No se infiere volumen de llamadas ni pérdida de ventas.

Los 16 con evidencia pendiente están incluidos: cumplen el perfil de entrada aunque la captura no aportó evidencia telefónica suficiente. No se completaron sus señales usando las fichas anteriores. Katie’s, por ejemplo, no recuperó en este recorrido limitado la página con la señal que figuraba en la investigación anterior.

## Entrada y archivos de cada etapa

1. `locales.csv`: copia byte a byte de `data/locales.csv`, la única entrada aceptada. Su huella está en `origen.json`. Se acepta el perfil que trae; Apollo remoto queda fuera de esta prueba. `scripts/importar_locales.py` normaliza un export existente, pero no exporta desde la API de Apollo.
2. `evidencia_locales.csv`: captura nueva mediante el recolector. Arranca exclusivamente de `Website` de cada candidato y sigue enlaces publicados del mismo dominio. Guarda URL, fecha, tipo de fuente, estado y pasajes literales. No recibió URLs de las fichas antiguas. Quedan tareas de búsqueda pendientes que no se ejecutaron mediante un buscador de pago.
3. `textos_originales/`: texto completo extraído de cada descarga exitosa. Para el LLM se seleccionan hasta 3.500 caracteres por página mediante palabras clave; la selección es mecánica, no una conclusión. Se conservan cortes visibles y la validación comprueba también la cita contra el texto completo.
4. `solicitudes_extraccion.json`: prompt, esquema y entrada exacta de cada documento. `respuestas_extraccion_codex.json` contiene las respuestas nuevas de esta conversación, separadas del código. Algunas son vacías; capturas duplicadas no se convierten en incidentes adicionales.
5. `evidencia_llm_procesada.csv`: generado por `extraer_evidencias_llm.py --responses ...`. El script valida el esquema y las citas y asigna IDs de evidencia.
6. `solicitudes_clasificacion.json` y `respuestas_clasificacion_codex.json`: segunda lectura de las afirmaciones mediante el prompt de clasificación. Una etiqueta por `evidence_id`, con cita, fuerza y alcance. No se importó una tabla histórica de prioridades.
7. `resultados_evidencia_llm.csv`: generado por `analizar_evidencias_llm.py --responses ...`, con indicadores agregados para las 30 empresas. Las respuestas vacías revisadas se distinguen de la falta de texto fuente.
8. `gtm-lista.csv`: generado por `preparar_entrega.py` en modo independiente. Al reproducir explícitamente esta comprobación guardada, se copia a la raíz como entrega oficial y se genera su explicación desde la misma auditoría. Contiene los 30 prospectos del perfil y las 13 columnas del template. `candidatos_evaluados.csv` conserva todos los candidatos evaluados; también permite revisar exclusiones si otro lote tiene empresas fuera de perfil. `auditoria_prioridad.json` permite seguir cada puntaje hasta sus indicadores y citas.
9. `verificacion.json` y `pruebas.json`: resultado técnico, huellas de archivos y pruebas de rechazo/aislamiento.

`evidencia_resenas.csv` está vacío: no se usaron reseñas exportadas de Google ni una fuente de reseñas paga. No se fabricaron datos para suplir su ausencia. Algunas categorías de cocina quedan por confirmar; el CSV no debe presentarse como calificación comercial exhaustiva.

## Repetir esta ejecución sin red ni API

Desde la raíz del proyecto:

```sh
python3 scripts/comprobar_pipeline.py --replay --out-dir comprobacion_codex
```

Regenera extracción, clasificación, indicadores y CSV desde las capturas y las respuestas nuevas guardadas en esta carpeta. Después de verificar, actualiza el CSV oficial y LISTA-EXPLICADA.md en la raíz. Una ejecución en otra carpeta no publica automáticamente su resultado como entrega oficial. **Ese comando no interpreta otra vez con un LLM**: reproduce las respuestas registradas y ejecuta la validación y los cálculos. Es el mismo principio que conservar respuestas de API en caché, con procedencia explícita de Codex.

La regla actual es **prioridad-v4: el perfil incluye; la evidencia prioriza**. Perfil sin evidencia telefónica: 10–14 puntos; antecedentes antiguos: 15–24; exploratorio telefónico: 30–49; hipótesis operativa: 50–69; dificultad explícita: 80–99. La falta de evidencia no equivale a una exclusión. Solo se excluye por perfil de entrada, y la causa queda en la auditoría.

Para comprobar solamente las salidas existentes:

```sh
python3 scripts/comprobar_pipeline.py --verify-only --out-dir comprobacion_codex
```

La prueba adicional se ejecutó en una copia aislada sin `data/`, `interno/`, el simulador antiguo, cachés ni salidas calculadas. Se copiaron únicamente los scripts/prompts y las entradas nuevas adquiridas en esta prueba, los textos originales y las respuestas nuevas de Codex. Con la red bloqueada se regeneró un CSV idéntico. Se rechazaron una cita inventada, respuestas que no corresponden a la entrada y una clasificación incompleta. Esa reproducción usa respuestas guardadas; no simula una nueva interpretación en secreto.

## API automática y alternativa con Codex

Sin `--resume` ni `--replay`, cada invocación crea una corrida nueva en una carpeta vacía y vuelve a adquirir e interpretar todo desde locales.csv. El modo predeterminado `--llm-mode auto` intenta la API cuando hay `OPENAI_API_KEY` y `OPENAI_MODEL`. Si funciona, completa extracción, clasificación y CSV en la misma ejecución. Si falla, conserva las respuestas exitosas y exporta únicamente lo pendiente en `solicitudes_*_pendientes_codex.json`; Codex debe agregar las respuestas faltantes al archivo indicado, preservando las existentes. Después se continúa con `--resume --out-dir <carpeta>`. La intervención de Codex sigue siendo manual y limitada a responder los prompts.

`--llm-mode codex` garantiza que el coordinador no llame a APIs pagas, incluso con una clave configurada. Los pasos siguientes usan ese modo. `ejecucion_llm.json` registra intentos y pendientes de la última ejecución; `verificacion.json` contabiliza respuestas guardadas según proveedor. Los nombres históricos de archivos y la etiqueta de contrato no equivalen al modelo real: las nuevas respuestas API guardan proveedor, modelo y uso de tokens en metadata. El camino API y la recuperación se probaron con transporte simulado, sin una llamada paga real.

## Empezar otra comprobación verdaderamente desde locales

Usá una carpeta nueva para no mezclar respuestas de entradas distintas:

```sh
python3 scripts/comprobar_pipeline.py --input data/locales.csv --out-dir comprobacion_nueva --llm-mode codex
```

Este comando requiere que comprobacion_nueva no exista o esté vacía; hace adquisición nueva. Necesita acceso a Internet para las páginas públicas, pero no usa APIs de pago. Puede requerir autorización de red en Codex. En este macOS el orquestador usa el certificado raíz `/etc/ssl/cert.pem` cuando está disponible; no desactiva TLS.

Después de capturar, exporta las solicitudes de extracción y se detiene indicando que espera respuestas de Codex. En ese punto usá este mensaje en Codex:

```text
Ejecutá la comprobación de este proyecto usando solamente locales.csv como
entrada validada y una carpeta nueva comprobacion_nueva. No leas las fichas de
interno/, la evidencia anterior ni CLAIMS del simulador. No llames a APIs de pago.
Si no se capturaron fuentes todavía, ejecutá:
python3 scripts/comprobar_pipeline.py --input data/locales.csv --out-dir comprobacion_nueva --llm-mode codex

Limitá tu intervención a interpretar solicitudes y escribir respuestas JSON. No edites scripts, textos capturados, indicadores ni CSV de salida para completar la corrida. Leé las instrucciones, el esquema y TODAS las entradas de
comprobacion_nueva/solicitudes_extraccion_pendientes_codex.json. Interpretalas desde esta
conversación por lotes manejables y guardá las respuestas en
comprobacion_nueva/respuestas_extraccion_codex.json. Si ya hay respuestas parciales de esta corrida, preservalas y agregá solo las faltantes. Incluí metadata.provider=codex_conversacion. No copies respuestas de
otra corrida ni generes conclusiones con reglas de palabras clave. Cada cita
debe ser literal. Registrá sin evidencia o pendientes cuando corresponda.

Ejecutá python3 scripts/comprobar_pipeline.py --resume --out-dir comprobacion_nueva --llm-mode codex.
Se exportarán las solicitudes de clasificación pendientes. Leelas, aplicá el prompt desde
esta conversación y guardá respuestas_clasificacion_codex.json con una etiqueta
por evidencia. Incluí la misma procedencia en metadata. Continuá siempre con --resume hasta generar y verificar el CSV. No uses --run,
no inventes datos para obtener 30 leads y no modifiques el puntaje para forzar
un resultado. Separá el éxito técnico del flujo de la cobertura de las fuentes.
```

Formato de ambos archivos de respuestas (lista JSON, no diccionario por URL):

```json
[
  {
    "request_id": "copiar exactamente de la solicitud",
    "provenance": "Interpretación nueva de Codex en conversación; sin API",
    "response": {"claims": []}
  }
]
```

En clasificación, `response` contiene `labels` en lugar de `claims`. Debe respetarse el esquema incluido en cada archivo de solicitudes. Los `request_id` dependen de la entrada y del prompt: si cambian, las respuestas anteriores no sirven automáticamente.

## Cambios necesarios que reveló esta prueba

- El recolector no podía partir de un archivo de evidencia inexistente ni descubrir páginas por sí mismo sin un buscador configurado. Se agregó adquisición desde `Website` y sus enlaces, con fallos registrados.
- Las etapas LLM no aceptaban respuestas nuevas por archivo. Se añadieron `--requests` y `--responses`, con esquema, huella de entrada y validación literal; las llamadas de API no se habilitan en este modo.
- El generador final dependía de fichas y etiquetas históricas. Se agregó un modo independiente que consume únicamente locales, evidencia e indicadores de la carpeta elegida.
- Se separaron consultas telefónicas de pedidos y se corrigió el estado de documentos revisados sin afirmaciones.

Por eso la conclusión precisa es: **el flujo asistido por Codex se ejecutó y se pudo repetir con datos nuevos; la adquisición y la calificación comercial siguen siendo parciales. La integración remota con Apollo y OpenAI API permanece sin probar.**

## Protección contra la pérdida de prospectos

La primera versión de esta comprobación filtraba el CSV por presencia de evidencia telefónica y dejaba 14 filas. Ese filtro se corrigió: la evidencia cambia la prioridad y el estado de investigación, no la inclusión de los candidatos que cumplen el perfil.

El verificador compara el conjunto de empresas del CSV con el perfil de `locales.csv`. Si se pierde un prospecto válido, falla. No impone 30 a cualquier entrada: un candidato fuera de EE. UU. o del rango de 2–15 sucursales queda excluido, con causa en la auditoría. Para este archivo, las 30 empresas cumplen ese perfil.

Antes de mostrar el proceso:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/comprobar_pipeline.py --replay --out-dir comprobacion_codex
python3 scripts/comprobar_pipeline.py --verify-only --out-dir comprobacion_codex
```

Las pruebas cubren inclusión sin evidencia, fallo total de fuentes, orden por fuerza de señales, exclusión por perfil y mayor prioridad de un problema repetido sobre un pico de demanda. No requieren red ni API.

La corrida nueva escribe `estado_ejecucion.json`: `pendiente_codex` significa que no terminó; `completada` requiere generación y verificación. El proceso devuelve código 2 mientras espera interpretación y no genera un CSV final ficticio. Para empezar de cero otra vez, usar otra carpeta sin --resume; para continuar las mismas capturas, usar --resume.
