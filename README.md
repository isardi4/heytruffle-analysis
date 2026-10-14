# Restaurantes que podrían necesitar ayuda con sus llamadas

Este trabajo busca cadenas chicas de restaurantes de Estados Unidos que podrían perder pedidos o consultas porque el equipo no llega a atender el teléfono durante el servicio.

La lista permite explicar por qué conviene investigar una empresa. Las fuentes públicas no permiten confirmar cuántas llamadas pierde ni que la causa sea el personal ocupado en el salón.

## Qué hay para revisar

| Documento | Qué explica |
| --- | --- |
| [gtm-lista.csv](gtm-lista.csv) | Los 12 casos priorizados, con las 13 columnas del template. |
| [LISTA-EXPLICADA.md](LISTA-EXPLICADA.md) | Las mismas filas del CSV, sus argumentos, límites, orden y pregunta de validación. |
| [CRITERIO.md](CRITERIO.md) | La explicación breve del criterio, fuentes y trabajo con herramientas. |
| [CASOS.md](CASOS.md) | Los hechos, el motivo de elección y los límites de cada caso; también los pendientes y descartes. |
| [COMENTARIOS.md](COMENTARIOS.md) | La antigüedad de los comentarios y el resultado de revisar las fuentes nuevas para los 29 casos. |
| [FUENTES.md](FUENTES.md) | Qué fuentes se usaron, para qué sirven y qué resultados o usos se dejaron afuera. |
| Este README | El criterio y las decisiones del trabajo, con sus ventajas y desventajas. |

Corte de la investigación: **14 de octubre de 2026**.

| Estado del control actual | Empresas |
| --- | ---: |
| Preselección provisional con dificultad de comunicación, actividad concreta o límite de capacidad | 7 |
| Preselección provisional por su forma de trabajar; respaldo menor | 5 |
| Lista secundaria para validar: respaldo insuficiente | 17 |
| **Candidatos únicos en el control** | **29** |

Los doce de la preselección son Bar-Bill, Black’s, Joe’s Kansas City, Litza’s, Pappy’s, Pequod’s, Glass Nickel, Pizza Lucé, Downtown Pizza, NY Pie, Prime Pizza y Salvatore’s. Se conserva la diferencia entre sus argumentos: una línea ocupada reconocida por el restaurante es más directa que una descripción de tareas o una reseña antigua.

La lista conserva doce casos en preselección provisional, con respaldo desigual. Glass Nickel y Pizza Lucé se mantienen como antecedentes históricos de menor prioridad. Los otros 17 quedan en una lista secundaria para preguntar por su operación y buscar respaldo antes de ofrecer una solución. No están descartados definitivamente. La versión preparada está en [gtm-lista.csv](gtm-lista.csv) y mantiene visibles las hipótesis y los límites; no se confirmaron problemas telefónicos.

## Cómo se eligieron los casos

### 1. Comprobar primero el perfil

Se buscó Estados Unidos, comida casual con takeout y entre 2 y 15 locales publicados como activos. Pizza, alitas, comida china y barbacoa sirvieron para encontrar candidatos; la cocina no se tomó como prueba de llamadas perdidas.

Se contaron puntos bajo la marca, sin agregar aperturas futuras ni negocios hermanos con otros nombres. Cuando había concesiones, ventanillas o dudas de alcance, se registraron para revisar el conteo. Un directorio oficial es respaldo de lo publicado, no una llamada de comprobación de apertura.

**A favor:** concentra el trabajo en el tamaño pedido. **En contra:** las webs pueden estar desactualizadas y deja afuera negocios con el problema que no cumplen el perfil.

### 2. Usar una fila por cadena y un local identificado

Una empresa ocupa una fila. Ciudad, estado y teléfono corresponden a una sucursal concreta; el total de locales corresponde a la cadena. Una queja de una sede no se atribuye a todas.

Bar-Bill muestra por qué importa: el argumento telefónico corresponde a East Aurora. Su FAQ dice que Clarence y Rochester no aceptan esos pedidos de takeout. En The Pizza Company se eligió Munhall por su invitación a pedir por teléfono, sin trasladarle una queja de West Mifflin.

**A favor:** evita duplicados y argumentos dirigidos al local equivocado. **En contra:** investigar una sede no permite describir toda la empresa.

### 3. Separar el hecho de la hipótesis

“El cajero toma pedidos telefónicos y también cobra” es una responsabilidad publicada. “Esas tareas podrían competir por su tiempo” es nuestra interpretación. “Hoy pierde llamadas por falta de personal” requeriría información que no tenemos.

Se buscaron dos hechos útiles para explicar cada elección. Pueden compartir una página si describen cosas distintas; no se presentan como fuentes independientes. Una queja copiada en dos sitios sigue siendo una experiencia.

**A favor:** permite discutir el argumento y ver qué falta confirmar. **En contra:** una hipótesis razonable todavía puede resultar equivocada al hablar con el negocio.

### 4. Aceptar varias formas de respaldo, conservando sus diferencias

- **Problema de comunicación publicado:** Joe’s reconoce líneas ocupadas. El evento de Glass Nickel aporta un antecedente antiguo, con menor prioridad y sin confirmar vigencia.
- **Canal más actividad concreta:** Pequod’s publica teléfono y pico de 18 a 20; Litza’s describe noches concurridas en Midvale.
- **Reparto de tareas:** Prime, NY Pie y Salvatore’s describen funciones que combinan teléfono con trabajo presencial. Es un argumento más débil, sin llamada perdida observada.
- **Antecedente histórico:** Pizza Lucé conserva sus fuentes de 2022–2024, incluida una buena experiencia telefónica, como hipótesis histórica de menor prioridad. No se afirma una situación actual.

No se confunde un límite de cocina con un problema de atención. Black’s puede restringir pedidos porque no puede preparar más comida. Contestar más llamadas no aumenta esa capacidad. En Downtown, comparar teléfono con web no demuestra por qué uno es más lento.

**A favor:** aprovecha hechos concretos aunque no todos publiquen quejas. **En contra:** las formas de respaldo no son equivalentes; requieren leer la ficha, no solo el número de puntos.

### 5. Usar un puntaje simple, sin dejar que el puntaje elija

| Señal | Puntos |
| --- | --- |
| Pedidos telefónicos | 0 sin respaldo; 20 como opción explícita; 40 si se presentan como vía principal o única del local. |
| Dificultad para comunicarse | 0 sin respaldo; 20 por un relato concreto o admisión oficial de líneas ocupadas; 40 por varios clientes distintos. |
| Presión durante el servicio | 0 sin respaldo; 20 por presión concreta publicada, con contexto de servicio. |

La suma usa una escala de 0 a 100. No es un porcentaje de probabilidad ni está calibrada con resultados comerciales. No encontrar quejas tampoco demuestra que no haya un problema.

Un teléfono de contacto, una vacante, un tiempo normal de preparación o una apertura no suman por sí solos. Las tareas compartidas solo aportan puntos por el uso del teléfono, sin puntos adicionales por pico o falta de empleados. Un episodio no se vuelve a puntuar en varias categorías: Glass Nickel recibe 20 por el relato histórico de comunicación, sin sumar de nuevo el mismo episodio como canal y pico.

La restricción explícita de Black’s con mucha carga se consideró señal de capacidad. La posible restricción de delivery de Five Points no ubica un incidente u horario concreto y conserva cero en pico. Esta es una decisión de criterio, no una frontera comprobada con datos.

Katrina II tiene 40 por canal y sigue sin seleccionar porque falta otra señal. Glass Nickel conserva 20 por un episodio antiguo y queda en la preselección con menor prioridad por su fecha. El puntaje cuenta evidencia; la elección también considera relación con el problema, fecha, local y calidad de la fuente. Los puntajes de candidatos pendientes son exploratorios, no una recomendación automática de contacto.

**A favor:** la suma es fácil de comprobar. **En contra:** los pesos son decisiones de trabajo y un mismo resultado puede representar argumentos muy distintos.

### 6. Explicar tanto la elección como el motivo para dejar afuera

Se distinguen tres situaciones:

- **Fuera del perfil:** por ejemplo, solo una sede publicada.
- **Fuera de esta hipótesis o selección:** por ejemplo, Punch atiende mediante una central, o la fuente histórica de Flying Pie también describe una prueba de solución.
- **En la lista secundaria por falta de evidencia actual:** encaja o podría encajar, pero falta una segunda señal, fecha, local u original legible. Una conversación puede aclarar esos puntos; hace falta respaldo suficiente para pasar a la preselección.

Los 17 de respaldo insuficiente quedan en la lista secundaria. Glass Nickel y Pizza Lucé se conservan en la preselección como antecedentes históricos. Venezia’s, WingBasket y Brent’s tienen límites de fecha o fuente. La queja de Prince’s del 05/10/2025 se conserva como antecedente, con 20 puntos; sigue secundario porque falta otra señal. Los motivos individuales están en [CASOS.md](CASOS.md).

**A favor:** permite defender por qué una empresa no entra. **En contra:** algunos pendientes podrían ser buenas oportunidades; la investigación pública no alcanza para saberlo.

### 7. Evaluar la fuente según la afirmación

Se usaron webs oficiales para perfil y formas de pedir, avisos del empleador para tareas, y relatos individuales para experiencias. Noticias y publicaciones oficiales aportaron contexto de cambios. El buscador sirvió para encontrar páginas, no para reemplazar su lectura.

Los resúmenes automáticos, fragmentos cuya página no abrió, homónimos y experiencias de otras sucursales no se aceptaron como prueba del hecho buscado. Una copia legible conserva el límite de copia; un formulario de empleo no se convierte en falta de personal. Los ejemplos y motivos están en [FUENTES.md](FUENTES.md).

**A favor:** cada afirmación vuelve a una fuente adecuada. **En contra:** un bloqueo puede dejar una pista útil sin resolver y una fuente oficial también puede estar equivocada o desactualizada.

### 8. No inventar urgencia

Se distingue entre **comentarios recientes** —últimos 12 meses, del 14/10/2025 al 14/10/2026 en esta revisión—, **comentarios antiguos**, **fecha o verificación pendiente** y **sin comentario pertinente verificado**. Los antiguos conservan su valor como antecedentes y sus puntos aceptados; no se presentan como problemas actuales. Entre casos con respaldo parecido, se revisa primero el comentario pertinente más reciente. No se inventó un descuento numérico por edad.

También se distingue tener cualquier comentario reciente de tener uno útil para el ejercicio. Hay 9 casos con algún comentario reciente fechado y 2 con contexto operativo reciente. Una opinión sobre sabor no actualiza una queja telefónica antigua. La fecha desconocida queda visible; una fecha de edición no demuestra que la visita sea reciente. El detalle de los 29 está en [COMENTARIOS.md](COMENTARIOS.md).

Se distingue fecha del hecho, fecha de publicación y fecha de consulta. Un año ausente o una antigüedad relativa no se completa por intuición. Una página sin fecha no se presenta como una novedad.

El motivo de contacto puede ser operativo sin ser reciente: entender cómo cubren cierto horario o una distribución de tareas. Si no hay un hecho nuevo, se dice. Ningún caso permite asegurar ventas perdidas actuales a partir de esta investigación.

**A favor:** evita vender una historia que las fuentes no sostienen. **En contra:** varios casos necesitan confirmación antes de usarlos en un contacto comercial.

## Qué trabajo se hizo y con qué herramientas

Se empezó con diez candidatas y se hizo una primera pasada de otras cien. Esa evaluación registró 60 perfiles inicialmente compatibles, 45 pendientes y cinco descartes. Son datos de aquella etapa; no se suman a los 29 actuales. Después se profundizaron casos y se consolidó el control por nombre de empresa. El control pasó de 19 con alguna señal a 29 distintos, sin contar dos veces las fichas repetidas.

Se usó IA para proponer búsquedas, ayudar a leer y organizar información y redactar a partir de los registros. Se usaron buscador y navegador web; en algunos casos curl permitió recuperar HTML público. Python ayudó a leer texto estructurado, juntar registros, detectar duplicados y comprobar sumas, teléfonos y formatos. Los programas no certifican reseñas ni deciden por sí solos la selección.

La revisión de páginas y decisiones tuvo asistencia de IA. Se conservaron consultas, enlaces, límites y motivos para mostrar el proceso. No se usaron herramientas pagas ni se contactó a los restaurantes. La revisión humana final sigue pendiente.

**A favor:** las herramientas reducen tareas repetitivas. **En contra:** pueden interpretar mal una página; por eso se conserva la fuente y se distingue lo leído de lo inferido.

## Archivos de la versión de 12 casos

[gtm-lista.csv](gtm-lista.csv) contiene 12 filas, sin los ejemplos, con las 13 columnas de `gtm-lista-template.csv` y en el mismo orden: `company_name`, `city`, `state`, `locations_count`, `cuisine`, `phone`, `website`, `source_url`, `signal_1`, `signal_2`, `priority_score`, `why_now`, `notes`.

El orden de las filas indica la prioridad sugerida de revisión: primero el respaldo más directo del problema y luego los argumentos condicionados, las tareas compartidas y los antecedentes de menor confianza. La fecha ayuda a ordenar argumentos comparables. El puntaje sigue contando señales, por eso un antecedente con 40 puede ir después de una hipótesis con 20; no se inventa una probabilidad ni se cambia el peso de las señales para forzar el orden.

Cada fila identifica la sucursal, explica por qué se conserva, enlaza las dos señales y el perfil publicado, y propone una pregunta para confirmar o rechazar la hipótesis. Los teléfonos usan +1 y diez dígitos. Los locales anunciados no se suman a los publicados con datos de atención.

[LISTA-EXPLICADA.md](LISTA-EXPLICADA.md) se genera con los mismos registros: reproduce cada valor del CSV y desarrolla el argumento. Esto evita que la explicación diga algo distinto del archivo. **A favor:** permite revisar las decisiones sin interpretar una planilla. **En contra:** se debe regenerar la pareja de archivos cuando cambia una fila, para mantenerlos iguales.

[CRITERIO.md](CRITERIO.md) reúne la explicación breve pedida en la consigna. Se presentan menos de 40 casos porque estos 12 tienen argumentos documentados para esta selección, con respaldo desigual; los otros 17 quedan como secundarios para validar.

Se comprobaron las columnas, el orden, 12 empresas únicas, sucursales y teléfonos registrados, el rango de locales, dos señales por fila y las sumas. Se volvieron a leer fuentes oficiales y avisos disponibles; el blog de Litza’s y los datos de Downtown se comprobaron en HTML público. La lectura confirma lo publicado, no una operación real sin fallas. No se contactó a los restaurantes.
