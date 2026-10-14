# Los 27 casos del CSV, explicados

Este documento acompaña a [gtm-lista.csv](gtm-lista.csv). Presenta las mismas 27 empresas, en el mismo orden, con los mismos datos, señales, puntos y límites. Es una selección de hipótesis para validar, no una lista de llamadas perdidas confirmadas. Corte: **14/10/2026**.

## Cómo leer la prioridad

El orden de las filas es el orden sugerido para revisar o validar los casos. Se considera primero qué tan directo es el argumento, si corresponde a la sucursal elegida y qué falta confirmar. Entre argumentos parecidos, se prefiere evidencia más reciente. Las descripciones de tareas y los antecedentes antiguos quedan identificados.

`priority_score` cuenta señales aceptadas; no es una probabilidad ni mide ventas perdidas. Canal: 0/20/40; comunicación: 0/20/40; presión de servicio: 0/20. La antigüedad se muestra aparte, sin un descuento numérico inventado. Por eso un caso histórico con 40 puede ir después de una hipótesis de funcionamiento con 20. El orden comercial no se obtiene ordenando solo ese número.

**Ventaja:** no se equipara una queja con un anuncio de empleo o con una experiencia antigua. **Límite:** el orden requiere criterio; cada elección puede cambiar al confirmar cómo trabaja el negocio.

## Resumen de la lista

| Orden | Empresa | Sucursal | Puntos | Motivo para ubicarla aquí |
| --- | --- | --- | ---: | --- |
| 1 | Joe's Kansas City Bar-B-Que | Gas Station · 3002 W 47th | 40 | Primera revisión |
| 2 | Katie's Pizza & Pasta Osteria | Rock Hill · 9568 Manchester Road | 40 | Primera revisión, confirmar vigencia de la política |
| 3 | Pequod's Pizza | Chicago · 2207 N Clybourn | 40 | Primera revisión |
| 4 | Litza's Pizza | 835 East Fort Union Boulevard | 40 | Primera revisión |
| 5 | Bar-Bill Tavern | East Aurora · 185 Main St; retiros en 191 Main St Rear | 40 | Primera revisión |
| 6 | Pappy's Smokehouse | St. Louis · 3106 Olive St | 40 | Primera revisión |
| 7 | Mama's Pizza Omaha | Midtown · 715 N Saddle Creek Road | 40 | Primera revisión, confirmar alcance de la FAQ |
| 8 | HOTLIPS Pizza | Pearl · 721 NW 9th Ave, Suite 150 | 40 | Revisar cobertura en horas pico |
| 9 | Black's Barbecue | 215 N Main St | 40 | Primera revisión, con límite de capacidad |
| 10 | Glass Nickel Pizza | 3191 Muir Field Rd | 20 | Validar antecedente antiguo |
| 11 | Home Run Inn | Hillside · 60 S Mannheim Rd | 20 | Validar funcionamiento |
| 12 | Crushed Red | Kirkwood · 140 S Kirkwood Rd | 20 | Validar funcionamiento |
| 13 | SPIN! Pizza | Richardson · 348 W Campbell Rd | 20 | Validar funcionamiento |
| 14 | Prime Pizza | 235 E Imperial Highway | 20 | Validar funcionamiento |
| 15 | NY Pie Nashville | 1441 New Highway 96 West | 20 | Validar funcionamiento |
| 16 | Billy G's | Kirkwood · 131 W Argonne Dr | 20 | Validar funcionamiento |
| 17 | Super Taco Mexican Restaurants | Franklin · 7131 Franklin Blvd | 20 | Validar reparto de tareas en la sucursal |
| 18 | V Pizza | San Marco · 1406 Hendricks Ave | 20 | Validar funcionamiento |
| 19 | Holland Farms Bakery & Deli | Manlius · 343 Fayette St | 20 | Validar funcionamiento |
| 20 | Birria LES | Astoria · 31-27 Ditmars Blvd | 20 | Validar funcionamiento |
| 21 | Little Chef Chinese | Ocean Beach · 4910 Newport Ave | 20 | Validar reparto de tareas en la sucursal |
| 22 | Salvatore's Tomato Pies | Contacto elegido: Madison North Livingston · 10 N Livingston | 20 | Validar funcionamiento y sucursal |
| 23 | Pizzeria Delfina | Palo Alto · 651 Emerson Street | 20 | Validar funcionamiento |
| 24 | Zachary's Chicago Pizza | Pleasant Hill · 140 Crescent Drive | 20 | Validar funcionamiento |
| 25 | Downtown Pizza | 156 Magnolia St | 20 | Validar funcionamiento publicado en el código |
| 26 | Pizza Luce | Downtown Minneapolis · 119 N 4th St | 40 | Validar antecedente antiguo, menor prioridad |
| 27 | Golden Boy Pizza | North Beach · 542 Green Street | 40 | Antecedente antiguo y encaje parcial |

Los 12 de la cohorte inicial contienen 5 casos con algún comentario reciente fechado; entre las ocho incorporaciones se aceptaron comentarios recientes de comida de Pizzeria Delfina y uno favorable de servicio y entrega de Golden Boy. Este último no renueva la fila antigua. Entre los cinco siguientes, Crushed Red tiene una opinión favorable publicada el 03/06/2026, sin dificultad telefónica. Little Chef agrega opiniones favorables de comida de junio de 2026. Hay nueve seleccionados con algún comentario reciente aceptado. En los 27, solo Pappy’s y Pequod’s tienen comentarios operativos recientes comprobados. La búsqueda no demuestra ausencia de otras reseñas. Una reseña de comida no renueva una queja telefónica antigua. El detalle de las búsquedas está en [COMENTARIOS.md](COMENTARIOS.md).

## Fichas en el mismo orden que el CSV

### 1. Joe's Kansas City Bar-B-Que

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Joe's Kansas City Bar-B-Que |
| `city` | Kansas City |
| `state` | KS |
| `locations_count` | 3 |
| `cuisine` | Barbacoa |
| `phone` | +19137223366 |
| `website` | https://www.joeskc.com/pages/locations |
| `source_url` | https://www.joeskc.com/pages/contact-us |
| `signal_1` | La página de contacto indica que recibe pedidos de carryout por teléfono. |
| `signal_2` | La empresa pide volver a llamar si las líneas están ocupadas y aclara que atenderá cuando pueda. |
| `priority_score` | 40 |
| `why_now` | Sin novedad fechada. La instrucción oficial de volver a llamar permite preguntar por las llamadas que no llegan a atender. |
| `notes` | Sucursal: Gas Station · 3002 W 47th. No se midieron llamadas perdidas ni su causa. La web enlaza pickup online aunque el texto de contacto diga que no recibe pedidos online: no se afirma exclusividad telefónica. Por qué se elige: Es el argumento publicado más directo sobre dificultad para comunicarse: la empresa pide reintentar si las líneas están ocupadas. Qué validar: Cuando las líneas están ocupadas, ¿cuántas llamadas quedan sin atender y quién se encarga de ellas? Fuente de señal 2: https://www.joeskc.com/pages/contact-us Perfil y contacto: https://www.joeskc.com/pages/locations Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Es el argumento publicado más directo sobre dificultad para comunicarse: la empresa pide reintentar si las líneas están ocupadas.

**Qué podría necesitar y qué falta demostrar:** Si parte de esas llamadas busca pedir o consultar, podría servir una atención que responda cuando el equipo no puede. Falta saber cuántas quedan sin atender y por qué.

**Puntaje explicado:** 20 por canal + 20 por comunicación + 0 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Fecha de comentario pendiente. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** Cuando las líneas están ocupadas, ¿cuántas llamadas quedan sin atender y quién se encarga de ellas?

### 2. Katie's Pizza & Pasta Osteria

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Katie's Pizza & Pasta Osteria |
| `city` | Rock Hill |
| `state` | MO |
| `locations_count` | 4 |
| `cuisine` | Pizza |
| `phone` | +13149426557 |
| `website` | https://katies.com/ |
| `source_url` | https://katies.com/pages/important-info |
| `signal_1` | La página Important Info dice que recibe muchas llamadas y tiene líneas limitadas; pide volver a llamar cuando están todas ocupadas. |
| `signal_2` | La misma página permite pedidos telefónicos en vivo para quienes no tienen computadora y favorece el pedido online para administrar la capacidad. |
| `priority_score` | 40 |
| `why_now` | Sin fecha de publicación comprobable. Confirmar la política de líneas ocupadas todavía publicada y qué cambió desde que se escribió. |
| `notes` | Sucursal: Rock Hill · 9568 Manchester Road. La página conserva texto de dos sedes y retiro en auto: su vigencia no está confirmada. Se cuentan cuatro fichas con dirección, teléfono y horario: Rock Hill, Town & Country, Ballpark Village y Crestwood; no las aperturas anunciadas ni otra marca del grupo. El aviso Host/Hostess de Rock Hill en StaffedUp aporta tareas de teléfono y salón, sin puntos adicionales. No se midieron llamadas perdidas. No se toma la actualización global de Indeed como fecha de una reseña. Por qué se elige: La propia empresa explica una dificultad de acceso telefónico y el uso del teléfono para pedir, aunque con una política restrictiva. Qué validar: ¿Sigue vigente en Rock Hill la política de líneas ocupadas? ¿El límite está en las líneas, en quién atiende o en la cocina? ¿Qué solución usan hoy? Fuente de señal 2: https://katies.com/pages/important-info Perfil y contacto: https://katies.com/pages/rock-hill Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** La propia empresa explica una dificultad de acceso telefónico y el uso del teléfono para pedir, aunque con una política restrictiva.

**Qué podría necesitar y qué falta demostrar:** Podría necesitar ayuda para responder consultas o a quienes no pueden pedir online. Hay que distinguir capacidad de líneas, atención y cocina.

**Puntaje explicado:** 20 por canal + 20 por comunicación + 0 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** ¿Sigue vigente en Rock Hill la política de líneas ocupadas? ¿El límite está en las líneas, en quién atiende o en la cocina? ¿Qué solución usan hoy?

### 3. Pequod's Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Pequod's Pizza |
| `city` | Chicago |
| `state` | IL |
| `locations_count` | 2 |
| `cuisine` | Pizza |
| `phone` | +17733271512 |
| `website` | https://pequodspizza.com/ |
| `source_url` | https://pequodspizza.com/faqs/ |
| `signal_1` | La FAQ permite anticipar pedidos para llevar por teléfono. |
| `signal_2` | La misma FAQ identifica el pico de 18 a 20 y los sábados como el día más concurrido. |
| `priority_score` | 40 |
| `why_now` | Sin novedad telefónica fechada. Revisar cobertura del pico publicado de 18 a 20; la demora de entrega de agosto de 2026 no se atribuye al teléfono. |
| `notes` | Sucursal: Chicago · 2207 N Clybourn. Los dos hechos principales provienen de la misma FAQ. Usan Whale Tale para ciertos retiros, lo que puede aliviar trabajo. Emily W relata demora de entrega el 26/08/2026 y Jasmine G entrega a tiempo el 26/09/2026; no se conoce la causa ni se suman puntos nuevos. Por qué se elige: La empresa identifica un pico concreto de 18 a 20 y permite anticipar pedidos por teléfono; se puede plantear una pregunta operativa específica. Qué validar: Entre las 18 y las 20, ¿quién atiende los pedidos por teléfono y qué pasa si ya está atendiendo a otra persona? Fuente de señal 2: https://pequodspizza.com/faqs/ Perfil y contacto: https://pequodspizza.com/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** La empresa identifica un pico concreto de 18 a 20 y permite anticipar pedidos por teléfono; se puede plantear una pregunta operativa específica.

**Qué podría necesitar y qué falta demostrar:** Los pedidos telefónicos podrían competir con la atención presencial durante ese horario. No se comprobó que eso ocurra.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Comentario operativo reciente. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** Entre las 18 y las 20, ¿quién atiende los pedidos por teléfono y qué pasa si ya está atendiendo a otra persona?

### 4. Litza's Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Litza's Pizza |
| `city` | Midvale |
| `state` | UT |
| `locations_count` | 2 |
| `cuisine` | Pizza |
| `phone` | +18015612171 |
| `website` | https://www.litzaspizza.com/ |
| `source_url` | https://www.litzaspizza.com/blog/midvale-family-pizza/ |
| `signal_1` | El selector oficial de pedidos ofrece llamar a Midvale, además de pedir por Slice. |
| `signal_2` | Una nota oficial del 6 de mayo de 2026 describe el salón de Midvale lleno los viernes y sábados por la noche. |
| `priority_score` | 40 |
| `why_now` | La nota oficial del 06/05/2026 permite preguntar por la cobertura telefónica de las noches de fin de semana en Midvale. |
| `notes` | Sucursal: 835 East Fort Union Boulevard. Dos hechos de la misma página oficial. Comparte edificio con Hires Big H, que no cuenta como otra sede. La reseña de esperas de repartidores es del 27/05/2023: antecedente antiguo, sin llamada perdida comprobada. Por qué se elige: Hay una descripción oficial de mayo de 2026 del salón de Midvale lleno en noches de fin de semana, junto con la opción de pedir por teléfono. Qué validar: Los viernes y sábados por la noche, ¿la misma persona atiende el salón y las llamadas? ¿Qué ocurre cuando coinciden? Fuente de señal 2: https://www.litzaspizza.com/blog/midvale-family-pizza/ Perfil y contacto: https://www.litzaspizza.com/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Hay una descripción oficial de mayo de 2026 del salón de Midvale lleno en noches de fin de semana, junto con la opción de pedir por teléfono.

**Qué podría necesitar y qué falta demostrar:** El salón concurrido y los pedidos telefónicos podrían pedir atención al mismo tiempo. La publicación no informa llamadas perdidas.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Comentario operativo o telefónico antiguo. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** Los viernes y sábados por la noche, ¿la misma persona atiende el salón y las llamadas? ¿Qué ocurre cuando coinciden?

### 5. Bar-Bill Tavern

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Bar-Bill Tavern |
| `city` | East Aurora |
| `state` | NY |
| `locations_count` | 3 |
| `cuisine` | Alitas |
| `phone` | +17166527959 |
| `website` | https://www.barbill.com/ |
| `source_url` | https://www.barbill.com/faqs |
| `signal_1` | La FAQ de East Aurora permite pedir para llevar por teléfono o internet. |
| `signal_2` | La empresa indica que los fines de semana suelen estar ocupados y aumentan las esperas; describe el cierre de pedidos online al agotar capacidad nocturna. |
| `priority_score` | 40 |
| `why_now` | Sin novedad fechada. Preguntar cómo cubren llamadas en fines de semana y al agotarse la capacidad del pedido online. |
| `notes` | Sucursal: East Aurora · 185 Main St; retiros en 191 Main St Rear. El argumento es de East Aurora; no se traslada a Clarence o Rochester, que no aceptan esos pedidos telefónicos/online. El retiro de East Aurora no es una cuarta sede. Contestar más llamadas no aumenta la capacidad de cocina. Por qué se elige: East Aurora admite pedidos por teléfono y publica mayor espera en fines de semana y un cierre del canal online al agotar capacidad. Qué validar: Cuando se cierra el pedido online por capacidad, ¿aumentan las llamadas? ¿Las pueden atender o el límite es la cocina? Fuente de señal 2: https://www.barbill.com/faqs Perfil y contacto: https://www.barbill.com/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** East Aurora admite pedidos por teléfono y publica mayor espera en fines de semana y un cierre del canal online al agotar capacidad.

**Qué podría necesitar y qué falta demostrar:** Podrían acumularse consultas mientras el equipo atiende el servicio. No sabemos si el cierre online hace aumentar las llamadas.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** Cuando se cierra el pedido online por capacidad, ¿aumentan las llamadas? ¿Las pueden atender o el límite es la cocina?

### 6. Pappy's Smokehouse

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Pappy's Smokehouse |
| `city` | St. Louis |
| `state` | MO |
| `locations_count` | 2 |
| `cuisine` | Barbacoa |
| `phone` | +13145354340 |
| `website` | https://www.pappyssmokehouse.com/contact |
| `source_url` | https://www.pappyssmokehouse.com/contact |
| `signal_1` | La FAQ oficial permite pedir retiro al 314-535-4340, además de hacerlo online. |
| `signal_2` | AMarie525: Una hora de fila en visita de julio de 2026; la autora destaca fines de semana con béisbol y comida servida en menos de cinco minutos tras pedir. |
| `priority_score` | 40 |
| `why_now` | Reseña publicada el 17/08/2026 sobre una visita de julio: preguntar por cobertura telefónica en días concurridos. |
| `notes` | Sucursal: St. Louis · 3106 Olive St. Una sola reseña sobre fila presencial. La misma autora dice que la comida llegó en menos de cinco minutos tras pedir: se conserva ese dato favorable. No se midieron llamadas perdidas. Por qué se elige: Combina pedidos telefónicos oficiales con una experiencia presencial reciente que describe una hora de fila. Qué validar: En los días con más fila, ¿los pedidos por teléfono los toma el mismo equipo? ¿Quedan llamadas sin atender? Fuente de señal 2: https://www.tripadvisor.co.uk/Restaurant_Review-g44881-d1052764-Reviews-Pappy_s_Smokehouse-Saint_Louis_Missouri.html Perfil y contacto: https://www.pappyssmokehouse.com/contact Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Combina pedidos telefónicos oficiales con una experiencia presencial reciente que describe una hora de fila.

**Qué podría necesitar y qué falta demostrar:** Conviene preguntar si quienes atienden esa fila también responden pedidos remotos. La fila por sí sola no demuestra un problema telefónico.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Comentario operativo reciente. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** En los días con más fila, ¿los pedidos por teléfono los toma el mismo equipo? ¿Quedan llamadas sin atender?

### 7. Mama's Pizza Omaha

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Mama's Pizza Omaha |
| `city` | Omaha |
| `state` | NE |
| `locations_count` | 4 |
| `cuisine` | Pizza |
| `phone` | +14025539270 |
| `website` | https://mamaspizzaomaha.com/ |
| `source_url` | https://mamaspizzaomaha.com/ |
| `signal_1` | La página oficial ofrece pedidos por teléfono para Midtown. |
| `signal_2` | La FAQ de reservas de grupos identifica como picos las noches de viernes a domingo; no es una queja telefónica ni una política atribuida solo a Midtown. |
| `priority_score` | 40 |
| `why_now` | Sin novedad telefónica fechada. La FAQ permite preguntar por las noches de viernes a domingo; confirmar aplicación y vigencia en Midtown. |
| `notes` | Sucursal: Midtown · 715 N Saddle Creek Road. La FAQ trata reservas de grupos y muestra actualización del 22/07/2025; no es un comentario reciente. Cuatro sedes publicadas: Midtown, West Omaha, La Vista y Tiburon. Hay canal online. No hay llamadas perdidas comprobadas ni una reseña reciente original aceptada. Por qué se elige: El canal está identificado para Midtown y la empresa publica momentos de mayor actividad en su política de grupos. Qué validar: En Midtown, ¿también tienen más trabajo las noches de viernes a domingo? ¿Quién cubre los pedidos telefónicos mientras atienden el salón? Fuente de señal 2: https://mamaspizzaomaha.com/faqs/ Perfil y contacto: https://mamaspizzaomaha.com/locations/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El canal está identificado para Midtown y la empresa publica momentos de mayor actividad en su política de grupos.

**Qué podría necesitar y qué falta demostrar:** Conviene comprobar si las llamadas y la atención presencial coinciden en esos horarios y cómo se cubren.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Midtown, ¿también tienen más trabajo las noches de viernes a domingo? ¿Quién cubre los pedidos telefónicos mientras atienden el salón?

### 8. HOTLIPS Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | HOTLIPS Pizza |
| `city` | Portland |
| `state` | OR |
| `locations_count` | 2 |
| `cuisine` | Pizza |
| `phone` | +15035952342 |
| `website` | https://www.hotlipspizza.com/ |
| `source_url` | https://www.hotlipspizza.com/ |
| `signal_1` | La web pide llamar cuando desactiva temporalmente pedidos online para controlar los tiempos. |
| `signal_2` | La página de empleo identifica noches y fines de semana como momentos de mayor actividad. |
| `priority_score` | 40 |
| `why_now` | Sin novedad fechada. Confirmar cómo cubren las llamadas durante la política publicada de cierre temporal online. |
| `notes` | Sucursal: Pearl · 721 NW 9th Ave, Suite 150. Dos páginas de la misma empresa, sin fecha de publicación comprobada. Pearl y Hawthorne son las dos sedes publicadas; no se cuentan tres cerradas ni la cocina central. Ya usan canales digitales y control de capacidad. Atender más llamadas no aumenta la producción. Grubhub bloqueó las reseñas por país: no se acepta el fragmento como prueba. Por qué se elige: Publica una derivación concreta de pedidos hacia el teléfono y horarios de mayor trabajo. Qué validar: Cuando desactivan pedidos online, ¿quién responde las llamadas? ¿Necesitan atender consultas o la cocina ya no puede aceptar pedidos? Fuente de señal 2: https://www.hotlipspizza.com/jobs Perfil y contacto: https://www.hotlipspizza.com/pearl Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Publica una derivación concreta de pedidos hacia el teléfono y horarios de mayor trabajo.

**Qué podría necesitar y qué falta demostrar:** Las llamadas podrían coincidir con el servicio; también puede tratarse de un límite de cocina ya gestionado.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** Cuando desactivan pedidos online, ¿quién responde las llamadas? ¿Necesitan atender consultas o la cocina ya no puede aceptar pedidos?

### 9. Black's Barbecue

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Black's Barbecue |
| `city` | Lockhart |
| `state` | TX |
| `locations_count` | 4 |
| `cuisine` | Barbacoa |
| `phone` | +15123982712 |
| `website` | https://www.blacksbbq.com/locations |
| `source_url` | https://www.blacksbbq.com/locations/lockhart/pick-up-delivery |
| `signal_1` | La página de Lockhart invita a hacer pedidos para retirar por teléfono. |
| `signal_2` | La misma página avisa que cuando están muy ocupados solo toman pedidos presenciales. |
| `priority_score` | 40 |
| `why_now` | Sin novedad fechada. Distinguir un problema de atención de un límite de cocina antes de proponer una solución. |
| `notes` | Sucursal: 215 N Main St. Política oficial, no relato de llamada perdida. También hay pedidos online. No confundir con Terry Black’s. Si solo falta capacidad de cocina, este argumento no justifica vender atención telefónica. Por qué se elige: Publica una restricción concreta de pedidos cuando tiene mucho trabajo. Es una oportunidad condicionada a entender la causa. Qué validar: Cuando solo aceptan pedidos presenciales, ¿es por capacidad de cocina o porque no pueden atender llamadas? ¿Se pierden también consultas que podrían responder? Fuente de señal 2: https://www.blacksbbq.com/locations/lockhart/pick-up-delivery Perfil y contacto: https://www.blacksbbq.com/locations Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Publica una restricción concreta de pedidos cuando tiene mucho trabajo. Es una oportunidad condicionada a entender la causa.

**Qué podría necesitar y qué falta demostrar:** Podría necesitar ayuda para responder consultas o explicar límites. Si el único problema es que la cocina no puede preparar más comida, atender más pedidos no lo resuelve.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** Cuando solo aceptan pedidos presenciales, ¿es por capacidad de cocina o porque no pueden atender llamadas? ¿Se pierden también consultas que podrían responder?

### 10. Glass Nickel Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Glass Nickel Pizza |
| `city` | Fitchburg |
| `state` | WI |
| `locations_count` | 10 |
| `cuisine` | Pizza |
| `phone` | +16088484877 |
| `website` | https://www.glassnickelpizza.com/location-overview/ |
| `source_url` | https://seminole26-5.squarespace.com/events |
| `signal_1` | El organizador de una recaudación del 11 de marzo de 2025 informa que recibió relatos de esperas telefónicas muy largas y posibles pedidos que no se pudieron realizar. |
| `signal_2` | En el mismo balance explica que hubo tanta actividad que llamaron al dueño para ayudar. |
| `priority_score` | 20 |
| `why_now` | Antecedente del 11/03/2025, fuera de los últimos 12 meses. Confirmar repetición y cambios en la atención; sin urgencia actual comprobada. |
| `notes` | Sucursal: 3191 Muir Field Rd. Un evento y un organizador que transmite relatos de terceros. Los dos hechos salen del mismo episodio: suma una vez en comunicación, sin sumar de nuevo canal o pico. Hay comentarios favorables de entrega de 2026; no actualizan la queja telefónica ni se traslada a otras sedes. Por qué se elige: El evento de Fitchburg relaciona dificultad telefónica y actividad adicional, pero es de marzo de 2025 y el organizador transmite relatos ajenos. Qué validar: En la recaudación de marzo de 2025 hubo dificultades telefónicas reportadas: ¿volvieron a ocurrir en eventos posteriores y cómo las cubren hoy? Fuente de señal 2: https://seminole26-5.squarespace.com/events Perfil y contacto: https://www.glassnickelpizza.com/location-overview/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El evento de Fitchburg relaciona dificultad telefónica y actividad adicional, pero es de marzo de 2025 y el organizador transmite relatos ajenos.

**Qué podría necesitar y qué falta demostrar:** Ese episodio puede servir para preguntar si vuelve a pasar durante promociones. No se presenta como una dificultad actual de la cadena.

**Puntaje explicado:** 0 por canal + 20 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Comentario operativo o telefónico antiguo. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** En la recaudación de marzo de 2025 hubo dificultades telefónicas reportadas: ¿volvieron a ocurrir en eventos posteriores y cómo las cubren hoy?

### 11. Home Run Inn

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Home Run Inn |
| `city` | Hillside |
| `state` | IL |
| `locations_count` | 6 |
| `cuisine` | Pizza |
| `phone` | +17084939696 |
| `website` | https://www.homeruninnpizza.com/ |
| `source_url` | https://recruiting.paylocity.com/Recruiting/Jobs/Details/4520679 |
| `signal_1` | El puesto Cashier de Hillside incluye responder llamadas entrantes y tomar pedidos de comida para llevar. |
| `signal_2` | El mismo puesto recibe y ubica comensales, gestiona la espera, cobra y ayuda a retirar y preparar mesas. |
| `priority_score` | 20 |
| `why_now` | El portal del empleador registra publicación del aviso el 21/09/2026. Preguntar por la organización actual del puesto, sin atribuir urgencia ni falta de personal. |
| `notes` | Sucursal: Hillside · 60 S Mannheim Rd. Fuente original Paylocity enlazada desde Careers oficial, leída en HTML público. La fecha publicada aparece en los datos del listado; no demuestra que las tareas hayan empezado ese día. Se cuentan seis restaurantes del directorio actual; se excluyen fábricas, supermercados y locales cerrados de directorios antiguos. No se puntúa la frase genérica sobre trabajar en un ambiente rápido. Sin comentario reciente original aceptado. Por qué se elige: El empleador describe para Hillside una combinación explícita de pedidos por teléfono y atención del salón. Qué validar: En Hillside, ¿la misma persona toma pedidos telefónicos y ubica o ayuda con las mesas? ¿Quién cubre las llamadas cuando sale del puesto? Fuente de señal 2: https://recruiting.paylocity.com/Recruiting/Jobs/Details/4520679 Perfil y contacto: https://www.homeruninnpizza.com/restaurants/hillside/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El empleador describe para Hillside una combinación explícita de pedidos por teléfono y atención del salón.

**Qué podría necesitar y qué falta demostrar:** Es una buena pregunta sobre cobertura: no sabemos si el puesto se reparte entre varias personas o si ya tienen un sistema de apoyo.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Hillside, ¿la misma persona toma pedidos telefónicos y ubica o ayuda con las mesas? ¿Quién cubre las llamadas cuando sale del puesto?

### 12. Crushed Red

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Crushed Red |
| `city` | Kirkwood |
| `state` | MO |
| `locations_count` | 5 |
| `cuisine` | Pizza y ensaladas |
| `phone` | +13142380100 |
| `website` | https://crushed-red.com/ |
| `source_url` | https://staffedup.com/crushed-red-kirkwood/ |
| `signal_1` | El aviso de Wine Tender de Kirkwood incluye pedidos por teléfono y online. |
| `signal_2` | El mismo puesto cobra pedidos presenciales y lleva bebidas a las mesas. |
| `priority_score` | 20 |
| `why_now` | Sin novedad operativa fechada. Confirmar que el reparto de tareas publicado siga vigente. |
| `notes` | Sucursal: Kirkwood · 140 S Kirkwood Rd. Ambas señales salen del mismo puesto, no son pruebas independientes. Aviso sin fecha comprobada; no demuestra falta de empleados. Cinco fichas oficiales: Creve Coeur, Kirkwood, Chesterfield, Clayton y Overland Park. Photoshoot49 publicó el 03/06/2026 una opinión favorable sobre comida y atención de mostrador/mesa, sin dificultad telefónica; no agrega puntos. Por qué se elige: Un puesto local combina llamadas, cobro y atención de mesas. Qué validar: En Kirkwood, ¿quién cubre el teléfono cuando el Wine Tender lleva bebidas a las mesas? Fuente de señal 2: https://staffedup.com/crushed-red-kirkwood/ Perfil y contacto: https://crushed-red.com/locations/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Un puesto local combina llamadas, cobro y atención de mesas.

**Qué podría necesitar y qué falta demostrar:** Esas tareas podrían competir por atención; falta conocer el reparto real por turno.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** En Kirkwood, ¿quién cubre el teléfono cuando el Wine Tender lleva bebidas a las mesas?

### 13. SPIN! Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | SPIN! Pizza |
| `city` | Richardson |
| `state` | TX |
| `locations_count` | 13 |
| `cuisine` | Pizza |
| `phone` | +19722357746 |
| `website` | https://www.spinpizza.com/ |
| `source_url` | https://www.indeed.com/viewjob?jk=c309fd6de51c1b87 |
| `signal_1` | El aviso Hourly Team Member de Richardson asigna a caja los pedidos telefónicos y para llevar. |
| `signal_2` | La misma descripción indica que caja ayuda a los camareros cuando hace falta. No demuestra que ambas tareas coincidan ni que fallen llamadas. |
| `priority_score` | 20 |
| `why_now` | Sin fecha de publicación comprobable del aviso. Validar el reparto actual de tareas de caja en Richardson. |
| `notes` | Sucursal: Richardson · 348 W Campbell Rd. Descripción leída en el aviso original de Indeed. Dos hechos del mismo puesto, no dos pruebas independientes. Se cuentan las 13 sedes con ficha del directorio oficial; no se usan conteos de terceros. La mención genérica de picos de cocina no suma presión ni falta de personal. Sin comentario reciente aceptado; el original de DoorDash no abrió. Por qué se elige: El aviso corresponde a Richardson y combina pedidos telefónicos con apoyo al salón. Qué validar: En Richardson, cuando caja ayuda a los camareros, ¿quién toma los pedidos por teléfono? ¿Queda alguna llamada sin atender? Fuente de señal 2: https://www.indeed.com/viewjob?jk=c309fd6de51c1b87 Perfil y contacto: https://www.spinpizza.com/locations/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El aviso corresponde a Richardson y combina pedidos telefónicos con apoyo al salón.

**Qué podría necesitar y qué falta demostrar:** Puede servir una cobertura cuando caja ayuda a los camareros. Falta comprobar si ya tienen esa cobertura y qué demanda reciben.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Richardson, cuando caja ayuda a los camareros, ¿quién toma los pedidos por teléfono? ¿Queda alguna llamada sin atender?

### 14. Prime Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Prime Pizza |
| `city` | Brea |
| `state` | CA |
| `locations_count` | 13 |
| `cuisine` | Pizza |
| `phone` | +17145823422 |
| `website` | https://primepizza.com/ |
| `source_url` | https://www.indeed.com/viewjob?jk=e88f1eed0ffb8ee3 |
| `signal_1` | El anuncio de cajero para Brea incluye tomar pedidos en persona y por teléfono. |
| `signal_2` | El mismo cajero cobra, ordena tickets y empaqueta comida. |
| `priority_score` | 20 |
| `why_now` | Sin novedad fechada. El aviso de cajero permite preguntar por el reparto actual de tareas en Brea; confirmar su vigencia. |
| `notes` | Sucursal: 235 E Imperial Highway. Aviso sin fecha de publicación comprobable: no se afirma contratación vigente ni falta de personal. Dos tareas del mismo puesto no son dos pruebas de llamadas perdidas. El directorio publica 13 sedes con datos de atención; se excluyen tres anunciadas. Los comentarios de comida de 2026 no prueban el problema. Por qué se elige: El puesto de Brea combina teléfono, mostrador, cobro y empaquetado. Es una descripción local concreta, sin evidencia de falla. Qué validar: En Brea, ¿el cajero sigue tomando llamadas mientras cobra y empaqueta? ¿Cómo cubren las llamadas cuando se juntan esas tareas? Fuente de señal 2: https://www.indeed.com/viewjob?jk=e88f1eed0ffb8ee3 Perfil y contacto: https://primepizza.com/locations Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El puesto de Brea combina teléfono, mostrador, cobro y empaquetado. Es una descripción local concreta, sin evidencia de falla.

**Qué podría necesitar y qué falta demostrar:** Compartir esas tareas puede hacer difícil responder en algún momento. Falta comprobar cómo se reparten por turno y si hay llamadas sin atender.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** En Brea, ¿el cajero sigue tomando llamadas mientras cobra y empaqueta? ¿Cómo cubren las llamadas cuando se juntan esas tareas?

### 15. NY Pie Nashville

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | NY Pie Nashville |
| `city` | Franklin |
| `state` | TN |
| `locations_count` | 4 |
| `cuisine` | Pizza |
| `phone` | +16156143535 |
| `website` | https://www.nypienashville.com/ |
| `source_url` | https://www.linkedin.com/jobs/view/team-member-at-ny-pie-nashville-4420664523 |
| `signal_1` | El anuncio de Franklin asigna a caja atender llamadas e ingresar pedidos al sistema. |
| `signal_2` | La misma caja cobra, prepara ensaladas y postres, limpia y repone. |
| `priority_score` | 20 |
| `why_now` | El anuncio de Franklin sirve para preguntar por la organización del puesto. Su fecha aparece de forma relativa; confirmar vigencia sin inventar una urgencia. |
| `notes` | Sucursal: 1441 New Highway 96 West. Los dos hechos provienen del mismo anuncio. No hay una queja aceptada ni se suman puntos por contratar. El sitio también publica testimonios favorables sin fecha; no se toman como reseñas recientes verificadas. Por qué se elige: El anuncio de Franklin asigna a caja llamadas, ingreso de pedidos, cobro y preparación de otros productos. Qué validar: En Franklin, ¿caja atiende las llamadas mientras cobra y prepara productos? ¿Hay alguien que la cubra cuando se acumula trabajo? Fuente de señal 2: https://www.linkedin.com/jobs/view/team-member-at-ny-pie-nashville-4420664523 Perfil y contacto: https://www.nypienashville.com/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El anuncio de Franklin asigna a caja llamadas, ingreso de pedidos, cobro y preparación de otros productos.

**Qué podría necesitar y qué falta demostrar:** La atención telefónica podría competir con esas tareas. La descripción del puesto no muestra una dificultad real ni falta de empleados.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Franklin, ¿caja atiende las llamadas mientras cobra y prepara productos? ¿Hay alguien que la cubra cuando se acumula trabajo?

### 16. Billy G's

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Billy G's |
| `city` | Kirkwood |
| `state` | MO |
| `locations_count` | 2 |
| `cuisine` | Americana, pizza y sandwiches |
| `phone` | +13149848000 |
| `website` | https://billygskirkwood.com/ |
| `source_url` | https://staffedup.com/billygskirkwood/ |
| `signal_1` | El puesto Carryout de Kirkwood incluye tomar pedidos por teléfono. |
| `signal_2` | El mismo puesto toma pedidos presenciales, cobra y coordina el empaquetado para llevar. |
| `priority_score` | 20 |
| `why_now` | Sin fecha comprobada del aviso. Revisar cómo funciona actualmente el puesto Carryout. |
| `notes` | Sucursal: Kirkwood · 131 W Argonne Dr. Mismo aviso para las dos señales, sin puntos por presión ni contratación. Se cuentan Kirkwood y Chesterfield (https://billygs.com/chesterfield/), sin sumar otras marcas del grupo Gianino. La web también ofrece pedidos online; para agregar bebidas alcohólicas indica llamar. TripAdvisor no abrió: sus fragmentos no se aceptan como reseñas verificadas. Por qué se elige: El aviso local permite identificar quién combina llamadas y atención de pedidos presenciales. Qué validar: En Kirkwood, ¿quién cubre las llamadas cuando Carryout cobra o entrega un pedido? Fuente de señal 2: https://staffedup.com/billygskirkwood/ Perfil y contacto: https://billygskirkwood.com/order/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El aviso local permite identificar quién combina llamadas y atención de pedidos presenciales.

**Qué podría necesitar y qué falta demostrar:** Podría necesitar cobertura mientras caja atiende o entrega pedidos; no se comprobó una falla.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Kirkwood, ¿quién cubre las llamadas cuando Carryout cobra o entrega un pedido?

### 17. Super Taco Mexican Restaurants

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Super Taco Mexican Restaurants |
| `city` | Sacramento |
| `state` | CA |
| `locations_count` | 4 |
| `cuisine` | Mexicana, tacos y burritos |
| `phone` | +19164699104 |
| `website` | https://www.supertacomex.com/ |
| `source_url` | https://www.snagajob.com/jobs/1303458429 |
| `signal_1` | El aviso original de Server de Franklin incluye tomar pedidos de comida por teléfono. |
| `signal_2` | El mismo puesto cobra, empaqueta pedidos para retirar y ayuda a servir y limpiar mesas. |
| `priority_score` | 20 |
| `why_now` | Sin fecha absoluta comprobada del aviso. Confirmar que estas tareas describan la operación actual antes de ofrecer una solución. |
| `notes` | Sucursal: Franklin · 7131 Franklin Blvd. Dos hechos del mismo aviso, no dos fuentes independientes. La fecha relativa Today y Urgently hiring no se convierten en fecha absoluta ni en falta de personal. Cuatro sedes con horario publicado: Franklin, Grant Line, Calvine y Laguna. Mack Road está marcado REMODELING y queda fuera del conteo activo, aunque figure en el pie de página. Hay pedidos online. Uber Eats muestra opiniones favorables antiguas de 2022–enero de 2025, sin comentario reciente aceptado ni falla telefónica. No se usan copias de Google en Wanderlog como originales. Por qué se elige: El aviso del empleador vincula llamadas y atención de mesas en Franklin, una sede identificada. Qué validar: En Franklin, ¿quién cubre el teléfono cuando el servidor está atendiendo mesas o empaquetando retiros? Fuente de señal 2: https://www.snagajob.com/jobs/1303458429 Perfil y contacto: https://www.supertacomex.com/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El aviso del empleador vincula llamadas y atención de mesas en Franklin, una sede identificada.

**Qué podría necesitar y qué falta demostrar:** Las llamadas podrían coincidir con el servicio de mesas; el aviso no demuestra que queden sin atender.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Franklin, ¿quién cubre el teléfono cuando el servidor está atendiendo mesas o empaquetando retiros?

### 18. V Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | V Pizza |
| `city` | Jacksonville |
| `state` | FL |
| `locations_count` | 13 |
| `cuisine` | Pizza |
| `phone` | +19045271511 |
| `website` | https://www.vpizza.com/ |
| `source_url` | https://www.vpizza.com/jobs/cashier-and-food-runner/ |
| `signal_1` | El puesto general Cashier incluye responder llamadas y cargar pedidos para llevar en Toast; confirmar que describa San Marco. |
| `signal_2` | El mismo puesto también lleva comida a las mesas, cobra y limpia mesas; es una descripción general, sin sucursal asignada. |
| `priority_score` | 20 |
| `why_now` | Sin novedad fechada. Confirmar en San Marco la descripción general de caja y reparto de tareas. |
| `notes` | Sucursal: San Marco · 1406 Hendricks Ave. Aviso sin fecha comprobable ni sucursal fija. El directorio tiene 13 sedes con atención y una futura en Durbin: se excluye Durbin. El texto del puesto todavía menciona 12 y dos en construcción; se prefiere el directorio detallado. No se supone falta de personal, llamadas perdidas ni actividad urgente por contratar. Por qué se elige: La descripción oficial combina teléfono con trabajo en las mesas, una coincidencia directa con la hipótesis del ejercicio. Qué validar: En San Marco, ¿el cajero que toma llamadas también lleva comida y limpia mesas? ¿Quién lo cubre cuando sale al salón? Fuente de señal 2: https://www.vpizza.com/jobs/cashier-and-food-runner/ Perfil y contacto: https://www.vpizza.com/locations/san-marco-jacksonville-fl/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** La descripción oficial combina teléfono con trabajo en las mesas, una coincidencia directa con la hipótesis del ejercicio.

**Qué podría necesitar y qué falta demostrar:** Esas tareas podrían competir por la misma persona. Primero hay que confirmar que así se trabaje en San Marco.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En San Marco, ¿el cajero que toma llamadas también lleva comida y limpia mesas? ¿Quién lo cubre cuando sale al salón?

### 19. Holland Farms Bakery & Deli

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Holland Farms Bakery & Deli |
| `city` | Manlius |
| `state` | NY |
| `locations_count` | 2 |
| `cuisine` | Deli, sandwiches y panadería |
| `phone` | +13156716344 |
| `website` | https://hollandfarms.com/ |
| `source_url` | https://hollandfarms.com/manlius/ |
| `signal_1` | La página de Manlius ofrece pedidos telefónicos de panadería, deli y comidas para retirar. |
| `signal_2` | El puesto Bakery Clerk/Customer Service de Manlius combina pedidos telefónicos con atención presencial, cobro y reposición. |
| `priority_score` | 20 |
| `why_now` | Sin novedad fechada. Confirmar vigencia del puesto y volumen de pedidos de comida por teléfono. |
| `notes` | Sucursal: Manlius · 343 Fayette St. Dos sedes publicadas: Yorkville y Manlius. Encaje como deli con panadería, no como restaurante tradicional de salón. No se suman puntos por reglas normales del retiro express ni por una vacante. Se excluyen reseñas de Yorkville y copias sin original de Google/Yelp; no se verificó comentario reciente de Manlius. Por qué se elige: Hay un canal de pedidos de comida y un puesto de la misma sede que comparte teléfono y mostrador. Qué validar: En Manlius, ¿cuántas llamadas son por comidas del deli y quién atiende mientras el mostrador está ocupado? Fuente de señal 2: https://staffedup.com/holland-farms-bakery-deli-manlius/ Perfil y contacto: https://hollandfarms.com/manlius/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Hay un canal de pedidos de comida y un puesto de la misma sede que comparte teléfono y mostrador.

**Qué podría necesitar y qué falta demostrar:** El teléfono podría competir con la atención presencial; primero conviene conocer el peso del deli frente a los encargos de pastelería.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Manlius, ¿cuántas llamadas son por comidas del deli y quién atiende mientras el mostrador está ocupado?

### 20. Birria LES

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Birria LES |
| `city` | Astoria |
| `state` | NY |
| `locations_count` | 5 |
| `cuisine` | Mexicana, birria y tacos |
| `phone` | +17182551312 |
| `website` | https://www.doordash.com/business/birria-les-13501665/ |
| `source_url` | https://jobtoday.com/us/job/cashier-and-line-cooks-YRd2LY?locale=en-US |
| `signal_1` | El aviso original de Astoria incluye tomar pedidos por teléfono y en persona. |
| `signal_2` | El mismo puesto maneja caja y organiza y empaqueta pedidos de entrega. |
| `priority_score` | 20 |
| `why_now` | El anuncio se publicó el 01/06/2026: permite preguntar por el funcionamiento del puesto, sin suponer falta de personal. |
| `notes` | Sucursal: Astoria · 31-27 Ditmars Blvd. Dos señales del mismo aviso. El aviso dice dos locales; se prefieren las cinco direcciones publicadas en DoorDash: Rivington, St Marks, Chelsea, Bedford y Astoria. Website es ficha comercial, no dominio oficial confirmado. Teléfono y dirección en https://www.restaurantji.com/ny/astoria/birria-les-astoria-/ y https://restaurantguru.com/Birria-LES-Astoria-New-York: se usan como directorios de contacto, no sus copias de reseñas. Confirmar teléfono y conteo al contactar. No se aceptan sitios de muestra de OrderSave ni comentarios de otras marcas de birria. Por qué se elige: El aviso identifica la sede y combina atención telefónica, presencial y preparación de entregas. Qué validar: En Astoria, ¿quién responde el teléfono cuando caja está cobrando o empaquetando entregas? Fuente de señal 2: https://jobtoday.com/us/job/cashier-and-line-cooks-YRd2LY?locale=en-US Perfil y contacto: https://www.doordash.com/business/birria-les-13501665/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El aviso identifica la sede y combina atención telefónica, presencial y preparación de entregas.

**Qué podría necesitar y qué falta demostrar:** Las tareas podrían coincidir; falta confirmar su reparto y si las llamadas generan un problema.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Astoria, ¿quién responde el teléfono cuando caja está cobrando o empaquetando entregas?

### 21. Little Chef Chinese

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Little Chef Chinese |
| `city` | San Diego |
| `state` | CA |
| `locations_count` | 2 |
| `cuisine` | China para llevar |
| `phone` | +16192226627 |
| `website` | https://littlechefcatering.us/ |
| `source_url` | https://www.indeed.com/viewjob?jk=1ba99e6d1b3b1320 |
| `signal_1` | El aviso original de cajero de Ocean Beach incluye pedidos telefónicos, presenciales y de plataformas. |
| `signal_2` | El mismo puesto cobra, mantiene el área de clientes y ayuda con empaquetado y preparación simple en cocina. |
| `priority_score` | 20 |
| `why_now` | Sin fecha absoluta comprobada del aviso. Confirmar que estas tareas describan la operación actual antes de ofrecer una solución. |
| `notes` | Sucursal: Ocean Beach · 4910 Newport Ave. Las dos señales provienen del mismo puesto. Sin fecha absoluta comprobada, sin puntos por ambiente rápido ni vacante. Dos direcciones oficiales: Ocean Beach y Sorrento Valley. Operación centrada en takeout, con encaje parcial respecto de la hipótesis de personal en salón. En Uber Eats, Jeremy R. (21/06/2026) y Sarah H. (23/06/2026) elogian la comida: algún comentario reciente sí, dificultad telefónica no. TripAdvisor tiene experiencias antiguas; no se acepta como reciente el año 2026 del título ni testimonios copiados sin fecha en la web. Por qué se elige: El puesto identifica Ocean Beach y combina llamadas, caja y apoyo de cocina y mostrador. Qué validar: En Ocean Beach, ¿quién responde las llamadas cuando caja cobra o ayuda con preparaciones en cocina? Fuente de señal 2: https://www.indeed.com/viewjob?jk=1ba99e6d1b3b1320 Perfil y contacto: https://littlechefcatering.us/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El puesto identifica Ocean Beach y combina llamadas, caja y apoyo de cocina y mostrador.

**Qué podría necesitar y qué falta demostrar:** El teléfono podría competir con caja o preparación. El encaje es teléfono más mostrador; no se atribuye servicio de salón completo.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** En Ocean Beach, ¿quién responde las llamadas cuando caja cobra o ayuda con preparaciones en cocina?

### 22. Salvatore's Tomato Pies

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Salvatore's Tomato Pies |
| `city` | Madison |
| `state` | WI |
| `locations_count` | 3 |
| `cuisine` | Pizza |
| `phone` | +16083058885 |
| `website` | https://www.salvatorestomatopies.com/ |
| `source_url` | https://www.salvatorestomatopies.com/careers/ |
| `signal_1` | La descripción general Host/Phone de la cadena incluye tomar pedidos por teléfono; confirmar que corresponda a Madison. |
| `signal_2` | Ese mismo puesto toma reservas y ayuda a los camareros cuando hace falta. |
| `priority_score` | 20 |
| `why_now` | Sin novedad fechada. Confirmar primero que el puesto general Host/Phone corresponda a Madison y describa su operación actual. |
| `notes` | Sucursal: Contacto elegido: Madison North Livingston · 10 N Livingston. Aviso general sin sucursal ni fecha indicadas. Teléfono y dirección corresponden a Madison North Livingston; las tareas todavía no están confirmadas para esa sede. Sin llamada perdida ni falta de personal comprobadas. Por qué se elige: La descripción Host/Phone combina pedidos telefónicos, reservas y apoyo a camareros. Falta atribuir ese puesto a Madison. Qué validar: En Madison North Livingston, ¿el puesto Host/Phone también toma reservas y ayuda a los camareros? ¿Quién cubre las llamadas mientras lo hace? Fuente de señal 2: https://www.salvatorestomatopies.com/careers/ Perfil y contacto: https://www.salvatorestomatopies.com/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** La descripción Host/Phone combina pedidos telefónicos, reservas y apoyo a camareros. Falta atribuir ese puesto a Madison.

**Qué podría necesitar y qué falta demostrar:** El reparto de tareas coincide con la hipótesis del ejercicio a nivel de cadena. No se comprobó que se aplique al contacto elegido.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Madison North Livingston, ¿el puesto Host/Phone también toma reservas y ayuda a los camareros? ¿Quién cubre las llamadas mientras lo hace?

### 23. Pizzeria Delfina

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Pizzeria Delfina |
| `city` | Palo Alto |
| `state` | CA |
| `locations_count` | 4 |
| `cuisine` | Pizza |
| `phone` | +16503532208 |
| `website` | https://www.pizzeriadelfina.com/ |
| `source_url` | https://www.pizzeriadelfina.com/catering/ |
| `signal_1` | La página oficial de catering permite pedidos por teléfono y publica el contacto de Palo Alto; exige 24 horas de anticipación. No confirma pedidos individuales inmediatos por teléfono. |
| `signal_2` | El anuncio Host/Cashier de Palo Alto del 06/10/2026 combina teléfono, cobro, recepción de comensales y coordinación de takeout y delivery. |
| `priority_score` | 20 |
| `why_now` | Aviso de Palo Alto publicado el 06/10/2026. Sirve para revisar tareas telefónicas y de salón; no prueba falta de personal ni una contratación urgente. |
| `notes` | Sucursal: Palo Alto · 651 Emerson Street. Anuncio y página de catering leídos en HTML público porque la herramienta web no mostraba todo. Fecha del aviso y datos del puesto en HTML/JSON del original. Las tres sedes de catering no reemplazan las cuatro de la marca. Se excluye el aviso de Delfina Restaurant Mission: es otra operación. DoorDash de Palo Alto tiene reseñas favorables de comida del 22/04/2026 y 20/07/2026; no prueban dificultad telefónica. Por qué se elige: Hay un puesto local fechado que combina llamadas y salón. El pedido telefónico comprobado es catering: el argumento comercial queda limitado a ese canal y a consultas. Qué validar: En Palo Alto, ¿el Host/Cashier recibe pedidos individuales por teléfono o solo consultas y catering? ¿Quién cubre esas llamadas mientras recibe comensales? Fuente de señal 2: https://www.craigslist.org/view/d/palo-alto-host-cashier-pizzeria-delfina/6CCYBMgqvxpfbqfA7EQJsg Perfil y contacto: https://www.pizzeriadelfina.com/location/palo-alto/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Hay un puesto local fechado que combina llamadas y salón. El pedido telefónico comprobado es catering: el argumento comercial queda limitado a ese canal y a consultas.

**Qué podría necesitar y qué falta demostrar:** Podría ayudar a cubrir consultas y catering cuando recepción está ocupada; antes de proponer pedidos individuales hay que confirmar que los acepten por teléfono.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** En Palo Alto, ¿el Host/Cashier recibe pedidos individuales por teléfono o solo consultas y catering? ¿Quién cubre esas llamadas mientras recibe comensales?

### 24. Zachary's Chicago Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Zachary's Chicago Pizza |
| `city` | Pleasant Hill |
| `state` | CA |
| `locations_count` | 6 |
| `cuisine` | Pizza |
| `phone` | +19256027000 |
| `website` | https://zacharys.com/ |
| `source_url` | https://zacharys.com/frequently-asked-questions/ |
| `signal_1` | La FAQ acepta pedidos para comer en el local por teléfono de 11 a 16; después de las 16 solo acepta por teléfono pedidos para llevar. |
| `signal_2` | Pleasant Hill permite adelantar la pizza después de entrar en la lista de espera de mesas. Es una organización del servicio, sin presión extraordinaria comprobada. |
| `priority_score` | 20 |
| `why_now` | Sin problema reciente fechado. Validar cómo funciona la restricción de pedidos telefónicos para comer en el local después de las 16. |
| `notes` | Sucursal: Pleasant Hill · 140 Crescent Drive. No se suman puntos por una espera posible ni por una regla horaria. Se cuentan seis sedes del menú actual, incluida Livermore abierta; se deja atrás el texto antiguo que dice cinco. Hay pedidos online y plataformas. Sin comentario operativo reciente original aceptado. Por qué se elige: Hay una regla horaria concreta del teléfono y una forma publicada de coordinar pedidos con la espera de mesas. Qué validar: Después de las 16, ¿quién toma los pedidos para llevar por teléfono? ¿Cómo se coordina con las personas que esperan mesa? Fuente de señal 2: https://zacharys.com/locations/pleasant-hill/ Perfil y contacto: https://zacharys.com/locations/pleasant-hill/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Hay una regla horaria concreta del teléfono y una forma publicada de coordinar pedidos con la espera de mesas.

**Qué podría necesitar y qué falta demostrar:** Sirve para preguntar por el reparto de llamadas y atención de mesas después de las 16. No sabemos si la regla responde a una dificultad.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** Después de las 16, ¿quién toma los pedidos para llevar por teléfono? ¿Cómo se coordina con las personas que esperan mesa?

### 25. Downtown Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Downtown Pizza |
| `city` | Spartanburg |
| `state` | SC |
| `locations_count` | 2 |
| `cuisine` | Pizza |
| `phone` | +18642743893 |
| `website` | https://downtownpizzasc.com/ |
| `source_url` | https://downtownpizzasc.com/contact |
| `signal_1` | La respuesta publicada en los datos de la página confirma pedidos por teléfono. |
| `signal_2` | La misma respuesta indica que pedir online por Toast suele ser más rápido en horas de más trabajo; otra respuesta describe servicio de mostrador. |
| `priority_score` | 20 |
| `why_now` | Sin novedad fechada. Confirmar la vigencia de la comparación teléfono/Toast publicada en los datos de la web. |
| `notes` | Sucursal: 156 Magnolia St. Las respuestas están en los datos FAQ del código HTML, no visibles en el formulario: menor confianza y vigencia pendiente. No se suman puntos de falla ni presión. Spartanburg e Inman tienen sistemas separados. Las reseñas recientes de comida no prueban dificultad telefónica. Por qué se elige: El código de la página oficial dice que se puede pedir por teléfono y que Toast suele ser más rápido cuando hay más trabajo. Es un respaldo menos visible. Qué validar: En Spartanburg, ¿por qué recomiendan Toast frente al teléfono cuando hay más trabajo? ¿La diferencia está en atender, tomar el pedido o prepararlo? Fuente de señal 2: https://downtownpizzasc.com/contact Perfil y contacto: https://downtownpizzasc.com/contact Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** El código de la página oficial dice que se puede pedir por teléfono y que Toast suele ser más rápido cuando hay más trabajo. Es un respaldo menos visible.

**Qué podría necesitar y qué falta demostrar:** Puede haber una diferencia operativa entre canales. La comparación no demuestra llamadas perdidas ni permite identificar la causa.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 0 por presión = 20. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Sin comentario pertinente verificado. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** En Spartanburg, ¿por qué recomiendan Toast frente al teléfono cuando hay más trabajo? ¿La diferencia está en atender, tomar el pedido o prepararlo?

### 26. Pizza Luce

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Pizza Luce |
| `city` | Minneapolis |
| `state` | MN |
| `locations_count` | 9 |
| `cuisine` | Pizza |
| `phone` | +16123337359 |
| `website` | https://pizzaluce.com/locations |
| `source_url` | https://www.tripadvisor.co.uk/Restaurant_Review-g43323-d444556-Reviews-Pizza_Luce_Downtown-Minneapolis_Minnesota.html |
| `signal_1` | Rori T describe un pedido telefónico y una entrega bien atendidos en una reseña del 14 de octubre de 2022. |
| `signal_2` | KevChesters menciona más actividad en noches de partido el 21 de junio de 2024; Jake M describe servicio más lento por afluencia el 27 de septiembre de 2023. |
| `priority_score` | 40 |
| `why_now` | Antecedentes de 2022–2024, fuera de los últimos 12 meses. Sin disparador actual; confirmar primero canal y funcionamiento. |
| `notes` | Sucursal: Downtown Minneapolis · 119 N 4th St. La reseña telefónica del 14/10/2022 es favorable. Los relatos de actividad son de 2023–2024, de autores distintos. No se comprobó un comentario operativo reciente de Downtown ni llamadas perdidas. Puntaje histórico de 40, con menor prioridad comercial por antigüedad y relación indirecta con el problema. Por qué se elige: Hay antecedentes de uso del teléfono y actividad en noches de partido en Downtown, pero son de 2022–2024 y la atención telefónica fue buena. Qué validar: En Downtown, ¿siguen tomando pedidos por teléfono y aumenta esa demanda en noches de partido? ¿Cómo cubren esas llamadas hoy? Fuente de señal 2: https://www.tripadvisor.co.uk/Restaurant_Review-g43323-d444556-Reviews-Pizza_Luce_Downtown-Minneapolis_Minnesota.html Perfil y contacto: https://pizzaluce.com/locations Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Hay antecedentes de uso del teléfono y actividad en noches de partido en Downtown, pero son de 2022–2024 y la atención telefónica fue buena.

**Qué podría necesitar y qué falta demostrar:** Es una hipótesis histórica sobre coincidencia de tareas y demanda. Requiere confirmar canal y funcionamiento actuales antes de usarla comercialmente.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Comentario operativo o telefónico antiguo. No se comprobó un comentario reciente fechado del período para esta sucursal.

**Pregunta para validar:** En Downtown, ¿siguen tomando pedidos por teléfono y aumenta esa demanda en noches de partido? ¿Cómo cubren esas llamadas hoy?

### 27. Golden Boy Pizza

| Campo del CSV | Valor |
| --- | --- |
| `company_name` | Golden Boy Pizza |
| `city` | San Francisco |
| `state` | CA |
| `locations_count` | 3 |
| `cuisine` | Pizza |
| `phone` | +14159829738 |
| `website` | https://www.goldenboypizza.com/ |
| `source_url` | https://www.goldenboypizza.com/ |
| `signal_1` | La web oficial ofrece pedir por teléfono, personalmente o por plataformas; informa que funciona solo para llevar. |
| `signal_2` | nadia y relata 30 minutos de fila en North Beach; publicó su reseña el 12/07/2025. Es un antecedente antiguo de atención presencial, no una llamada perdida. |
| `priority_score` | 40 |
| `why_now` | Antecedente del 12/07/2025, fuera de los últimos 12 meses. Sin urgencia actual; confirmar funcionamiento y si vuelve a haber filas similares. |
| `notes` | Sucursal: North Beach · 542 Green Street. Encaje parcial: takeout sin salón, con tres sedes oficiales. Una fila presencial antigua no demuestra volumen telefónico ni que el mismo empleado atienda ambos canales. El relato de fila del 10/08/2025 también es antiguo. Frank S. el 11/06/2026 elogia servicio y entrega en Uber Eats: se conserva como contrapeso favorable, sin renovar la fila antigua. Los fragmentos de TripAdvisor que aluden a 2026 no se aceptan: la lectura del original no permitió vincularlos a una reseña fechada concreta. Por qué se elige: Combina un canal telefónico oficial con una fila concreta de la misma sucursal, aunque el antecedente es antiguo y el encaje es menor. Qué validar: En North Beach, ¿quién responde pedidos telefónicos mientras atienden la fila de ventanilla? ¿Qué cambió desde el episodio de julio de 2025? Fuente de señal 2: https://www.tripadvisor.com/Restaurant_Review-g60713-d353911-Reviews-Golden_Boy_Pizza-San_Francisco_California.html Perfil y contacto: https://www.goldenboypizza.com/ Corte: 14/10/2026. |

**Por qué lo elegimos y por qué va aquí:** Combina un canal telefónico oficial con una fila concreta de la misma sucursal, aunque el antecedente es antiguo y el encaje es menor.

**Qué podría necesitar y qué falta demostrar:** La coincidencia posible es entre teléfono y ventanilla. Al ser solo takeout, no se plantea el problema de empleados atendiendo mesas.

**Puntaje explicado:** 20 por canal + 0 por comunicación + 20 por presión = 40. No se suman puntos dos veces por el mismo episodio.

**Comentarios:** Comentario operativo o telefónico antiguo. Se comprobó algún comentario reciente de la sucursal; su tema puede ser distinto del problema telefónico.

**Pregunta para validar:** En North Beach, ¿quién responde pedidos telefónicos mientras atienden la fila de ventanilla? ¿Qué cambió desde el episodio de julio de 2025?

## Decisiones de formato y alcance

Se usa una fila por cadena y un contacto de una sucursal identificada. `locations_count` indica el total de la cadena, no cantidad de incidentes. `phone` usa el formato internacional +1 y diez dígitos. `source_url` apunta a la primera señal; la segunda fuente y el perfil están en `notes`, junto con sucursal, límites y pregunta de validación. Si las dos señales salen de la misma página, se deja visible.

`why_now` explica el motivo para revisar el caso y avisa cuando no hay novedad fechada. No se convierte una página consultada hoy en una noticia nueva, una vacante en falta de personal ni una entrega demorada en una llamada perdida.

Se conservaron los 12 casos iniciales y se incorporaron quince después de revisar diez tandas de diez candidatos. El CSV tiene 27 hipótesis documentadas, con confianza desigual. Otros 17 de la cohorte original siguen en la lista secundaria. Los 100 resultados de la ampliación están en [TANDAS.md](TANDAS.md). Se detuvo la ampliación al completar 27; no se afirma que sean todos los casos posibles. Los motivos de selección y exclusión están en [CASOS.md](CASOS.md).

## Controles realizados

Se compararon las 13 columnas y su orden con el template, se quitaron sus ejemplos y se comprobaron 27 empresas sin duplicados. Se revisaron correspondencia de los datos con el control de fuentes, formato de teléfonos, rango de 2–15 locales, dos señales por fila y sumas. CSV y este Markdown se generan a partir de los mismos registros para evitar diferencias.

Se volvieron a leer fuentes oficiales y avisos accesibles; el blog de Litza’s y los datos de Downtown se comprobaron en HTML público. Estos controles comprueban lo publicado y el archivo; no sustituyen hablar con los negocios. No se contactó a los restaurantes.
