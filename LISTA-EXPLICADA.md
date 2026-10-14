# Los 12 casos del CSV, explicados

Este documento acompaña a [gtm-lista.csv](gtm-lista.csv). Presenta las mismas 12 empresas, en el mismo orden, con los mismos datos, señales, puntos y límites. Es una selección de hipótesis para validar, no una lista de llamadas perdidas confirmadas. Corte: **14/10/2026**.

## Cómo leer la prioridad

El orden de las filas es el orden sugerido para revisar o validar los casos. Se considera primero qué tan directo es el argumento, si corresponde a la sucursal elegida y qué falta confirmar. Entre argumentos parecidos, se prefiere evidencia más reciente. Las descripciones de tareas y los antecedentes antiguos quedan identificados.

`priority_score` cuenta señales aceptadas; no es una probabilidad ni mide ventas perdidas. Canal: 0/20/40; comunicación: 0/20/40; presión de servicio: 0/20. La antigüedad se muestra aparte, sin un descuento numérico inventado. Por eso un caso histórico con 40 puede ir después de una hipótesis de funcionamiento con 20. El orden comercial no se obtiene ordenando solo ese número.

**Ventaja:** no se equipara una queja con un anuncio de empleo o con una experiencia antigua. **Límite:** el orden requiere criterio; cada elección puede cambiar al confirmar cómo trabaja el negocio.

## Resumen de la lista

| Orden | Empresa | Sucursal | Puntos | Motivo para ubicarla aquí |
| --- | --- | --- | ---: | --- |
| 1 | Joe's Kansas City Bar-B-Que | Gas Station · 3002 W 47th | 40 | Primera revisión |
| 2 | Pequod's Pizza | Chicago · 2207 N Clybourn | 40 | Primera revisión |
| 3 | Litza's Pizza | 835 East Fort Union Boulevard | 40 | Primera revisión |
| 4 | Bar-Bill Tavern | East Aurora · 185 Main St; retiros en 191 Main St Rear | 40 | Primera revisión |
| 5 | Pappy's Smokehouse | St. Louis · 3106 Olive St | 40 | Primera revisión |
| 6 | Black's Barbecue | 215 N Main St | 40 | Primera revisión, con límite de capacidad |
| 7 | Glass Nickel Pizza | 3191 Muir Field Rd | 20 | Validar antecedente antiguo |
| 8 | Prime Pizza | 235 E Imperial Highway | 20 | Validar funcionamiento |
| 9 | NY Pie Nashville | 1441 New Highway 96 West | 20 | Validar funcionamiento |
| 10 | Salvatore's Tomato Pies | Contacto elegido: Madison North Livingston · 10 N Livingston | 20 | Validar funcionamiento y sucursal |
| 11 | Downtown Pizza | 156 Magnolia St | 20 | Validar funcionamiento publicado en el código |
| 12 | Pizza Luce | Downtown Minneapolis · 119 N 4th St | 40 | Validar antecedente antiguo, menor prioridad |

Los 12 contienen 5 casos con algún comentario reciente fechado, pero solo Pappy’s y Pequod’s tienen comentarios operativos recientes comprobados. Una reseña de comida no renueva una queja telefónica antigua. El detalle de las búsquedas está en [COMENTARIOS.md](COMENTARIOS.md).

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

### 2. Pequod's Pizza

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

### 3. Litza's Pizza

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

### 4. Bar-Bill Tavern

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

### 5. Pappy's Smokehouse

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

### 6. Black's Barbecue

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

### 7. Glass Nickel Pizza

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

### 8. Prime Pizza

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

### 9. NY Pie Nashville

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

### 10. Salvatore's Tomato Pies

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

### 11. Downtown Pizza

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

### 12. Pizza Luce

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

## Decisiones de formato y alcance

Se usa una fila por cadena y un contacto de una sucursal identificada. `locations_count` indica el total de la cadena, no cantidad de incidentes. `phone` usa el formato internacional +1 y diez dígitos. `source_url` apunta a la primera señal; la segunda fuente y el perfil están en `notes`, junto con sucursal, límites y pregunta de validación. Si las dos señales salen de la misma página, se deja visible.

`why_now` explica el motivo para revisar el caso y avisa cuando no hay novedad fechada. No se convierte una página consultada hoy en una noticia nueva, una vacante en falta de personal ni una entrega demorada en una llamada perdida.

Se conservaron los 12 casos razonados y se mantuvieron otros 17 en una lista secundaria de validación. Se presentan menos de 40 porque no hay respaldo suficiente para defender más filas con el mismo detalle. Los motivos de selección y exclusión están en [CASOS.md](CASOS.md).

## Controles realizados

Se compararon las 13 columnas y su orden con el template, se quitaron sus ejemplos y se comprobaron 12 empresas sin duplicados. Se revisaron correspondencia de los datos con el control de fuentes, formato de teléfonos, rango de 2–15 locales, dos señales por fila y sumas. CSV y este Markdown se generan a partir de los mismos registros para evitar diferencias.

Se volvieron a leer fuentes oficiales y avisos accesibles; el blog de Litza’s y los datos de Downtown se comprobaron en HTML público. Estos controles comprueban lo publicado y el archivo; no sustituyen hablar con los negocios. No se contactó a los restaurantes.
