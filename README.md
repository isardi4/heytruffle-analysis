# Restaurantes que podrían necesitar ayuda con sus llamadas

Este trabajo busca cadenas chicas de restaurantes de Estados Unidos que podrían perder pedidos o consultas porque el equipo no llega a atender el teléfono durante el servicio.

La lista permite explicar por qué conviene investigar una empresa. Las fuentes públicas no permiten confirmar cuántas llamadas pierde ni que la causa sea el personal ocupado en el salón.

## Qué hay para revisar

| Documento | Qué explica |
| --- | --- |
| [gtm-lista.csv](gtm-lista.csv) | Los 27 casos priorizados, con las 13 columnas del template. |
| [LISTA-EXPLICADA.md](LISTA-EXPLICADA.md) | Las mismas filas del CSV, sus argumentos, límites, orden y pregunta de validación. |
| [CRITERIO.md](CRITERIO.md) | La explicación breve del criterio, fuentes y trabajo con herramientas. |
| [CASOS.md](CASOS.md) | Los hechos, el motivo de elección y los límites de cada caso; también los pendientes y descartes. |
| [COMENTARIOS.md](COMENTARIOS.md) | La antigüedad de los comentarios y el resultado de revisar las fuentes nuevas para los 29 iniciales y las quince incorporaciones. |
| [FUENTES.md](FUENTES.md) | Qué fuentes se usaron, para qué sirven y qué resultados o usos se dejaron afuera. |
| [TANDAS.md](TANDAS.md) | Los 100 resultados de búsqueda evaluados, agrupados de diez, y por qué se suman quince. |
| Este README | El criterio y las decisiones del trabajo, con sus ventajas y desventajas. |

Corte de la investigación: **14 de octubre de 2026**.

| Estado del control detallado actual | Empresas |
| --- | ---: |
| Preseleccionados con alguna señal de comunicación o presión, incluida evidencia antigua | 12 |
| Preseleccionados por tareas o reglas de funcionamiento, sin falla comprobada | 15 |
| Lista secundaria original para validar | 17 |
| **Total del control detallado** | **44** |

El CSV tiene **27 preseleccionados**: los 12 iniciales más quince incorporaciones después de diez tandas de diez. [TANDAS.md](TANDAS.md) muestra las 100 decisiones; 85 resultados no se incorporaron. Incluye un distribuidor descartado como falso positivo: no son 100 restaurantes con perfil confirmado.

Las primeras seis tandas llevaron la lista a 20; las dos siguientes agregaron cinco y llegaron a 25. Las tandas nueve y diez evaluaron otros 20 candidatos y sumaron **Super Taco Mexican Restaurants** y **Little Chef Chinese**. Sus datos y las 13 columnas exactas del CSV están en [LISTA-EXPLICADA.md](LISTA-EXPLICADA.md). Son hipótesis para validar: no se confirmaron llamadas perdidas.

Los 17 secundarios originales siguen separados. Los 44 del control detallado son 27 seleccionados y 17 secundarios. No se suman a los 100 de las tandas ni a los 110 de la búsqueda inicial como empresas nuevas distintas. Las 18 decisiones de no incorporar de las últimas tandas están en TANDAS; no pasan automáticamente a la lista secundaria original.

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

También se distingue tener cualquier comentario reciente de tener uno útil para el ejercicio. En los 29 iniciales hay 9 casos con algún comentario reciente fechado y 2 con contexto operativo reciente. Las ocho incorporaciones agregan comentarios recientes de comida de Delfina y uno favorable de servicio y entrega de Golden Boy, sin renovar su fila antigua: el control anterior de 37 tenía 11 con algún comentario reciente y conserva los mismos 2 con dificultad o presión reciente pertinente. Una opinión sobre sabor no actualiza una queja telefónica antigua. La fecha desconocida queda visible; una fecha de edición no demuestra que la visita sea reciente. Las cinco incorporaciones siguientes agregan una opinión favorable reciente de Crushed Red: el control anterior de 42 tenía 12 con algún comentario reciente; ocho estaban entre los 25 seleccionados. Little Chef agrega comentarios favorables de comida de junio de 2026: el control vigente de 44 tiene 13 con alguno reciente y nueve están entre los 27 seleccionados. Siguen siendo dos los casos con comentario operativo reciente pertinente. El detalle por cohorte está en [COMENTARIOS.md](COMENTARIOS.md).

Se distingue fecha del hecho, fecha de publicación y fecha de consulta. Un año ausente o una antigüedad relativa no se completa por intuición. Una página sin fecha no se presenta como una novedad.

El motivo de contacto puede ser operativo sin ser reciente: entender cómo cubren cierto horario o una distribución de tareas. Si no hay un hecho nuevo, se dice. Ningún caso permite asegurar ventas perdidas actuales a partir de esta investigación.

**A favor:** evita vender una historia que las fuentes no sostienen. **En contra:** varios casos necesitan confirmación antes de usarlos en un contacto comercial.

## Cómo conseguimos el listado inicial

No se recibió una base de restaurantes de HeyTruffle, no se compró una lista de contactos y no se exportó un directorio completo de Google Maps. **El punto de partida fueron nombres de posibles cadenas regionales propuestos por la IA. Primero se propusieron nombres y después se buscó información sobre ellos.** Esos nombres sirvieron para buscar; no se consideraron verdaderos ni adecuados por haber sido sugeridos. Los primeros nombres se propusieron a partir del conocimiento previo del modelo, antes de consultar sus fuentes en este trabajo. No se puede identificar qué dato de entrenamiento originó cada sugerencia. La IA se usó para proponer candidatos; la evidencia se buscó después en publicaciones accesibles.

Conviene distinguir **elegir nombres para investigar** de **obtener el listado de sucursales**. Los nombres iniciales no salieron de una consulta que devolviera automáticamente todos los restaurantes adecuados. La IA propuso negocios que podían encajar. Después, las páginas oficiales permitieron comprobar las direcciones y cantidades de sucursales. Una propuesta podía resultar equivocada y quedar afuera.

Por ejemplo, **Pequod’s** fue una sugerencia basada en el conocimiento previo del modelo, no un restaurante descubierto primero en una página consultada durante esta investigación. Se ejecutó la búsqueda `Pequods locations official` y se consultó su [web oficial](https://pequodspizza.com/), donde se identificaron Chicago y Morton Grove. Eso permitió comprobar el tamaño publicado. Más adelante se leyó su [FAQ](https://pequodspizza.com/faqs/) para investigar pedidos telefónicos y horarios de mayor actividad. Proponer el nombre, comprobar sus sedes y justificar la selección fueron tres pasos separados.

El recorrido fue este:

1. **Proponer nombres para investigar.** Se empezó por pizza, alitas y comida china: cocinas prácticas para buscar negocios de comida para llevar. Esto orientó la búsqueda, pero no demuestra que tengan mucho volumen telefónico.
2. **Encontrar la web del negocio.** Se buscaron nombres concretos junto con palabras como `official`, `locations`, `menu` y `phone`. Por ejemplo: `Marions Piazza locations official`, `Venezias pizza Arizona locations official` y `Pequods locations official`. Se descartaron resultados de negocios con el mismo nombre en otras ciudades.
3. **Pasar el filtro de perfil.** Se leyeron los directorios oficiales para identificar Estados Unidos, comida casual y entre 2 y 15 sedes publicadas. Se contaron direcciones distintas, sin sumar anuncios futuros o marcas hermanas. Esta primera tanda reunió diez candidatos; todavía no eran diez oportunidades comprobadas.
4. **Ampliar y buscar señales.** Se armó otra lista de cien nombres y se hicieron búsquedas por empresa sobre web oficial, pedidos telefónicos, reseñas, empleo y aperturas. Un ejemplo registrado es `"Champion Wings & Fish" official locations menu phone`. Luego se abrieron las páginas encontradas cuando fue posible. Que un resultado apareciera en el buscador no bastaba para aceptarlo.
5. **Profundizar y seleccionar.** Se comprobaron sucursal, contenido, fecha y relación con el problema. Se guardaron argumentos y límites, y quedaron 12 preseleccionados. Después se revisaron seis tandas y se incorporaron ocho para llegar a 20; otras dos tandas aportaron cinco y llevaron la lista a 25; dos tandas más agregaron dos y cerraron esta versión en 27. Diez de los candidatos de esas tandas se retomaron de la búsqueda anterior; no son 100 empresas necesariamente nuevas frente a las 110.

Los diez del primer filtro fueron Marion’s Piazza, Venezia’s Pizzeria, WingBasket, The Wing Dome, PizzaPapalis, Cloverleaf Pizza, Pequod’s Pizza, Golden Wok, Han Dynasty y Chengdu Impression. **Es una lista histórica de candidatos, no la selección actual ni una confirmación de sus datos actuales.** En aquella etapa, algunos conteos eran provisionales y después se revisaron.

Los registros conservan los nombres propuestos, consultas, páginas encontradas y resultados del filtro. No permiten atribuir a cada nombre una primera página de descubrimiento anterior a la propuesta inicial. Por eso no se afirma que todo el listado haya salido de un único directorio o de una búsqueda general reproducible con idénticos resultados.

**A favor:** permite empezar rápido y comprobar cada candidato con fuentes públicas. **En contra:** la propuesta de nombres puede dejar afuera cadenas menos conocidas y sobrerrepresenta pizzerías. No es una muestra representativa de todos los restaurantes de Estados Unidos. Los datos y decisiones guardados permiten reconstruir el trabajo; una búsqueda repetida puede devolver otros resultados.

## Qué hizo la persona, qué hizo la IA y qué hicieron los scripts

La persona responsable definió criterios, dirigió la investigación, revisó los resultados y argumentos de los primeros 20 casos e indicó ajustes durante el trabajo. La IA realizó la búsqueda y lectura inicial de fuentes y preparó propuestas para esa revisión. Python resolvió las tareas repetitivas de archivos. Revisar los casos presentados y volver a abrir cada enlace son tareas distintas; aquí se describe la primera como revisión manual.

| Parte del trabajo | Cómo se hizo | Qué resultado produjo | Qué no demuestra |
| --- | --- | --- | --- |
| Definición del alcance y ajustes de criterio | Intervención humana: decidir qué priorizar, distinguir comentarios recientes de antiguos, mantener secundarios y ampliar esta versión a 27. | Reglas que guiaron la investigación. | No equivale a abrir y comprobar personalmente cada fuente. |
| Propuesta de candidatos y consultas | IA: sugerir nombres y búsquedas por negocio y sucursal. | Una lista de candidatos y consultas para buscar fuentes. | Una sugerencia no confirma que el negocio exista, tenga el tamaño pedido o pierda llamadas. |
| Búsqueda, lectura y extracción | IA mediante buscador, lector web y, en algunos casos, recuperación de HTML público con curl. | Datos, enlaces, fechas y límites de acceso. | Leer un fragmento no equivale a leer todas las reseñas; una respuesta de IA no reemplaza la fuente. |
| Evaluación de argumentos | La IA comparó sucursal, fecha y contenido y propuso selección, descarte y puntos. La persona responsable revisó los primeros 20 casos y ajustó el trabajo. Las siete altas posteriores quedan preparadas para revisión. | Fichas con hechos, hipótesis y preguntas; revisión humana confirmada para los primeros 20. | La revisión de resultados no se presenta como una segunda lectura individual de todos los enlaces. |
| Preparación y controles de archivos | Scripts de Python: unir registros, detectar duplicados, sumar puntos asignados, normalizar teléfonos y generar CSV y Markdown juntos. | Archivos consistentes y controles de formato y sumas. | Un script no certifica que una reseña sea cierta ni que la interpretación comercial sea correcta. |
| Revisión manual de los casos seleccionados | La persona responsable examinó los primeros 20 casos, revisó sus argumentos e indicó cambios en los criterios y resultados. | Selección y explicaciones ajustadas durante la revisión. | No mide llamadas reales ni equivale a una auditoría independiente de cada publicación original. |
| Validación con los negocios | No realizada. | Cada ficha propone qué preguntar. | No hay volumen medido de llamadas, pérdidas de ventas ni causa confirmada. |

Para ver el procedimiento en un caso concreto, en **Home Run Inn** la búsqueda encontró un puesto de caja; se siguió el enlace de empleo oficial hasta Paylocity y se leyó su HTML público. El anuncio asigna pedidos telefónicos y atención de mesas al mismo puesto. Esa comparación dio una hipótesis y 20 puntos por canal, sin inventar falta de personal. Después Python llevó los datos ya registrados al CSV y a su ficha Markdown. La elección del caso y el significado del anuncio no fueron calculados por ese script.

No se usaron herramientas pagas ni se contactó a los negocios. **A favor:** la IA y los scripts permiten buscar, ordenar y preparar archivos con menos trabajo repetitivo. **En contra:** la lectura e interpretación pueden contener errores; la revisión manual de los resultados y los controles de archivos ayudan a detectarlos, pero no certifican la veracidad de cada publicación ni la existencia de llamadas perdidas.

## Archivos de la versión de 27 casos

[gtm-lista.csv](gtm-lista.csv) contiene 27 filas, sin los ejemplos, con las 13 columnas de `gtm-lista-template.csv` y en el mismo orden: `company_name`, `city`, `state`, `locations_count`, `cuisine`, `phone`, `website`, `source_url`, `signal_1`, `signal_2`, `priority_score`, `why_now`, `notes`.

El orden de las filas indica la prioridad sugerida de revisión: primero el respaldo más directo del problema y luego los argumentos condicionados, las tareas compartidas y los antecedentes de menor confianza. La fecha ayuda a ordenar argumentos comparables. El puntaje sigue contando señales, por eso un antecedente con 40 puede ir después de una hipótesis con 20; no se inventa una probabilidad ni se cambia el peso de las señales para forzar el orden.

Cada fila identifica la sucursal, explica por qué se conserva, enlaza las dos señales y el perfil publicado, y propone una pregunta para confirmar o rechazar la hipótesis. Los teléfonos usan +1 y diez dígitos. Los locales anunciados no se suman a los publicados con datos de atención.

[LISTA-EXPLICADA.md](LISTA-EXPLICADA.md) se genera con los mismos registros: reproduce cada valor del CSV y desarrolla el argumento. Esto evita que la explicación diga algo distinto del archivo. **A favor:** permite revisar las decisiones sin interpretar una planilla. **En contra:** se debe regenerar la pareja de archivos cuando cambia una fila, para mantenerlos iguales.

[CRITERIO.md](CRITERIO.md) reúne la explicación breve pedida en la consigna. Se detuvo la ampliación al terminar diez tandas con 27 casos documentados, con respaldo desigual. No se continuó hasta 40. Los 17 secundarios originales quedan para validar.

Se comprobaron las columnas, el orden, 27 empresas únicas, sucursales y teléfonos registrados, el rango de locales, dos señales por fila y las sumas. Se volvieron a leer fuentes oficiales y avisos disponibles; el blog de Litza’s y los datos de Downtown se comprobaron en HTML público. La lectura confirma lo publicado, no una operación real sin fallas. No se contactó a los restaurantes.

## Decisiones de la ampliación

Se mantuvieron los mismos puntos: los avisos de tareas compartidas suman 20 por canal, sin agregar presión por decir “ambiente rápido” ni falta de personal por publicar una vacante. El aviso de Home Run Inn sí tiene fecha registrada del 21/09/2026; el de Delfina, del 06/10/2026. Esas fechas describen publicaciones, no incidentes ni urgencias.

Katie’s reconoce muchas llamadas y pocas líneas en una política sin fecha, que todavía habla de dos sedes. Se conserva el argumento, pero se pregunta primero si sigue vigente en Rock Hill y si ya tienen una solución. Mama’s publica picos en una FAQ de reservas de grupos: no se convierte en una queja telefónica ni se atribuye automáticamente a Midtown. V Pizza publica un puesto general: falta comprobarlo en San Marco.

Zachary’s se conserva por una restricción concreta del canal telefónico después de las 16 y su coordinación de pedidos con mesas; suma solo 20. Blue Line no se incorpora porque una espera posible para sentarse y el tiempo de horno, sin restricción telefónica ni tareas compartidas comprobadas, no aportan un argumento igual de específico.

Pizzeria Delfina tiene encaje condicionado: el pedido por teléfono probado es catering con 24 horas de anticipación. El aviso local combina recepción, caja y llamadas, pero no dice que tome pedidos individuales inmediatos por teléfono. Antes de proponer ese uso hay que confirmarlo. No se trasladó a la pizzería el anuncio de Delfina Restaurant Mission.

Golden Boy queda al final: el teléfono está publicado para pedir, pero la fila comprobada es de julio de 2025 y trabaja solo para llevar. La hipótesis es teléfono más ventanilla, sin salón. Su comentario favorable de entrega de junio de 2026 se conserva y no hace reciente aquella fila.

Para contar sedes se prefirieron fichas actuales con contacto a textos generales antiguos: seis de Zachary’s frente al texto de cinco, 13 de V Pizza frente al aviso de 12, cuatro fichas de Katie’s frente al texto antiguo de tres y seis restaurantes de Home Run Inn frente a directorios con nueve. Se excluyen futuras aperturas, fábricas, supermercados y otras marcas. Son conteos de lo publicado, sin llamadas de comprobación de apertura.

**A favor:** cada alta tiene un argumento que se puede revisar y una pregunta que puede refutarlo. **En contra:** varios casos siguen siendo hipótesis, algunas políticas pueden estar viejas y no se midieron llamadas. El registro conserva esos límites; llegar a 27 no los elimina.

## Decisiones de las cinco altas de las tandas siete y ocho

HOTLIPS publica picos de actividad y un paso concreto desde pedidos online hacia llamadas cuando necesita controlar tiempos. Suma 40: canal y presión. **A favor:** permite preguntar por una situación específica. **En contra:** ya tiene herramientas y puede estar limitando la cocina; responder más no crea capacidad.

Crushed Red, Billy G’s, Holland Farms y Birria LES suman 20 cada uno por pedidos telefónicos. Sus puestos también incluyen atención presencial, cobro o empaquetado. **A favor:** la hipótesis se apoya en tareas de una sede identificada. **En contra:** un puesto con varias tareas no demuestra que falte gente ni que pierdan llamadas. Las dos tareas de un aviso no son dos fuentes independientes.

Holland Farms entra como deli con panadería: antes de ofrecer el producto hay que distinguir pedidos de comida de encargos de pastelería. Birria LES usa como `website` su ficha comercial de DoorDash porque no se confirmó un dominio propio. Sus cinco direcciones publicadas prevalecen sobre las dos mencionadas en el aviso; se deja visible la diferencia. El contacto proviene de directorios públicos y debe confirmarse al llamar. **A favor:** permite revisar el caso sin inventar una web. **En contra:** el perfil y contacto tienen menor respaldo que una web propia.

La revisión humana de resultados está confirmada para los primeros 20; las siete altas posteriores quedan documentadas para revisión final. No se atribuye esa revisión como ya realizada.

## Decisiones de las tandas nueve y diez

Se eligieron los 20 candidatos a partir de resultados de búsquedas de avisos y pedidos telefónicos. Primero se comprobó el perfil; si fallaba el tamaño o no se podía identificar la marca, no se dedicó el mismo tiempo a reseñas. No se inventó un origen en un directorio ni se presentaron todos como negocios ya verificados.

**Super Taco, Franklin:** el aviso original del empleador en Snagajob asigna pedidos telefónicos, cobro, empaquetado y atención de mesas al mismo puesto. **A favor:** la relación con la hipótesis está descrita para una sede. **En contra:** no muestra turnos reales ni llamadas perdidas. Se cuentan cuatro sedes con horario; Mack Road figura en remodelación y se excluye del total activo.

**Little Chef, Ocean Beach:** el aviso original de Indeed combina teléfono, caja y apoyo de cocina. **A favor:** la sucursal está identificada y el canal es explícito. **En contra:** trabaja principalmente para llevar, con encaje parcial frente a un salón tradicional; falta conocer quién cubre el teléfono. Los comentarios de junio de 2026 elogian comida y no agregan puntos.

Ambos suman 20 por canal, sin puntos por presión ni por publicar una vacante. No se usa la fecha relativa del aviso para inventar una urgencia. La tanda nueve aportó dos; la diez, ninguna. Mantener las reglas puede dar una tanda sin altas. La revisión humana confirmada sigue siendo la de los primeros 20; los siete posteriores están preparados para revisión.
