# Índice de trabajo interno

Para entender el proyecto no hace falta abrir esta carpeta. Seguí README.md y DEFINICION-PROYECTO.md en la raíz.

## Archivos activos

- El generador de entrega está en `scripts/preparar_entrega.py`, junto con los otros scripts del flujo.
- indicadores-seleccion.json: etiquetas revisadas con IA sobre las fichas previas. Distingue canal, tareas, demanda, antecedentes antiguos y límites; no son respuestas nuevas de la API. El generador las une con los resultados del ensayo y conserva su procedencia en entrega-actual.json.
- control-paso-4.json, ampliacion-seleccionados.json, incorporaciones-25.json e incorporaciones-tandas-09-10.json: registros fuente del generador.
- apollo/apollo-accounts-export.csv: export original de 25 cuentas.
- apollo/revision-25-decisiones.json y revision-25.csv: decisiones y motivos de revisión.
- apollo/incorporacion-01.json: registro estructurado de las incorporaciones de Apollo.
- entrega-actual.json: salida de auditoría del generador, con indicadores y componentes de prioridad por empresa.

Para reproducir estos registros históricos, desde la raíz del proyecto ejecutá:
python3 scripts/preparar_entrega.py --legacy

Las salidas van en historico/reproduccion_inicial/. La entrega oficial se genera con la comprobación actual, sin leer estas fichas.

El cálculo usa `score_final` de `scripts/priorizar_leads.py`, regla prioridad-v4 (el perfil incluye; la evidencia prioriza). No usa los puntajes antiguos ni un orden manual. `entrega-actual.json` permite revisar los indicadores y componentes de cada puntaje. Los resultados de `data/simulacion_conversacion/` describen solo el corpus capturado; las fichas previas conservan fuentes adicionales pendientes de recaptura.

## Archivo histórico

El respaldo local archivo-investigacion-20261014.tar.gz (excluido de Git y no requerido para ejecutar el flujo) contiene 366 archivos de búsquedas, tandas, evaluaciones, borradores, scripts anteriores y notas de continuidad. Se agruparon para que el trabajo vigente sea fácil de encontrar; no se borraron. Si una revisión histórica necesita un archivo, se puede extraer desde este paquete conservando sus rutas internas.
