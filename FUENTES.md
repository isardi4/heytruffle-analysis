# Qué fuentes usamos y por qué

Corte de la investigación: 14 de octubre de 2026. Los enlaces que respaldan cada empresa están en [CASOS.md](CASOS.md). Aquí se explica para qué sirvió cada clase de fuente y qué parte no aceptamos como prueba.

Una página puede servir para una cosa y no para otra. Por ejemplo, una web oficial puede confirmar el teléfono sin demostrar que se pierdan llamadas. No se acepta ni se descarta una plataforma entera sin mirar el contenido concreto.

Con la evidencia registrada se conservan 27 casos en preselección provisional y 17 en una lista secundaria de validación. No se afirma que los secundarios carezcan del problema: falta evidencia suficiente o actual.

## De dónde salieron los nombres, antes de verificar fuentes

Los primeros nombres de candidatos fueron propuestos por la IA a partir del conocimiento previo del modelo, antes de verificar fuentes en este trabajo: posibles cadenas regionales de pizza, alitas y comida china. No se obtuvo primero un listado completo de restaurantes desde un directorio. La secuencia fue proponer nombres y después buscarlos; las sucursales se obtuvieron de las páginas oficiales. Luego se buscaron los nombres y sus directorios oficiales para filtrar el perfil. No salió de una base comprada ni de una exportación completa de Google Maps. La propuesta de nombres fue una ayuda para descubrir candidatos; las webs, avisos y reseñas respaldan los datos aceptados. [README.md](README.md) muestra las consultas de ejemplo, las etapas y quién hizo cada tarea. No es posible identificar el dato de entrenamiento que originó cada sugerencia. No se atribuye una página de descubrimiento a nombres que ya estaban en la propuesta del modelo.

## Fuentes que usamos

| Fuente | Para qué la usamos | Por qué sirve | Límite que conservamos |
| --- | --- | --- | --- |
| Directorios y fichas oficiales | Cantidad de locales, dirección, teléfono y opciones de pedido. | El negocio publica sus propios datos y permite identificar la sucursal. | Puede haber anuncios futuros, locales cerrados o diferencias entre secciones. No confirma apertura mediante una llamada. |
| Menús y preguntas frecuentes oficiales | Saber si reciben pedidos telefónicos y si declaran límites de atención o capacidad. | Explican cómo pide el cliente y qué reglas aplica el negocio. | Una instrucción puede estar desactualizada. Aceptar teléfono no prueba volumen ni ventas perdidas. |
| Avisos originales del empleador | Ver si una misma función toma pedidos telefónicos y también cobra, empaqueta o ayuda en el salón. | Describe un modo concreto de repartir tareas. | No indica cuántas personas cubren el puesto ni si les alcanza el tiempo. No prueba falta de empleados. |
| Reseñas individuales leídas en su plataforma | Buscar experiencias concretas con fecha, local y contexto. | Permiten leer qué intentó hacer una persona y qué respuesta recibió. | Son relatos, no registros de llamadas. Pueden ser aislados, antiguos o describir bien el servicio. |
| Balance publicado por un organizador de un evento | Entender un episodio concreto de mucha actividad y dificultad telefónica. | Quien organizó el evento publica su propio balance. | Puede transmitir relatos de otros sin identificar a cada persona. Un evento no demuestra un patrón habitual. |
| Testimonios elegidos por el restaurante y copias de reseñas | Conservar pistas o contexto cuando se puede identificar el relato. | A veces permiten acceder a detalles que no aparecen en otra página legible. | Pueden omitir fecha, sucursal o parte del contexto. No son otra experiencia independiente por aparecer copiados. |
| Noticias y comunicados | Comprobar aperturas, cierres o cambios del negocio. | Pueden aportar una fecha y explicar por qué cambió el perfil. | Una noticia antigua no describe necesariamente el presente. Un comunicado de un proveedor también tiene interés comercial. |
| Buscador web | Localizar las páginas anteriores. | Ahorra tiempo para encontrar una fuente específica. | El fragmento del resultado no se acepta por sí solo como hecho comprobado. |

Google Maps, Yelp, Tripadvisor, App Store y BBB se usaron para localizar o consultar experiencias según el acceso disponible. No se afirma haber leído todo lo publicado en esas plataformas ni todos los comentarios de cada restaurante.

## Ejemplos de uso aceptado

| Página | Hecho que respalda | Qué no demuestra |
| --- | --- | --- |
| [Joe’s: contacto](https://www.joeskc.com/pages/contact-us) | La empresa admite pedidos telefónicos y pide reintentar si las líneas están ocupadas. | Cuántas llamadas se pierden, la causa o exclusividad del teléfono. La misma página enlaza pedidos online y conserva instrucciones contradictorias. |
| [Pequod’s: FAQ](https://pequodspizza.com/faqs/) | Pedidos anticipados por teléfono y pico habitual entre las 18 y las 20. | Que no puedan atender llamadas en esa franja. Los dos hechos comparten una fuente. |
| [Bar-Bill: FAQ](https://www.barbill.com/faqs) | East Aurora admite pedidos telefónicos y avisa mayores esperas los fines de semana. | Que ocurra igual en Clarence o Rochester, donde no admite ese takeout. |
| [Black’s: Lockhart](https://www.blacksbbq.com/locations/lockhart/pick-up-delivery) | Con mucha carga limita pedidos a quienes van al local. | Que el cuello de botella sea atender el teléfono. Puede estar en la cocina. |
| [Litza’s: publicación sobre Midvale](https://www.litzaspizza.com/blog/midvale-family-pizza/) | Describe salón lleno los viernes y sábados por la noche; la página también ofrece pedidos telefónicos. | Llamadas perdidas. El texto del 06/05/2026 se recuperó del HTML público cuando el navegador de investigación falló. |
| [Prime: aviso de Brea](https://www.indeed.com/viewjob?jk=e88f1eed0ffb8ee3) | El cajero toma pedidos telefónicos y presenciales, cobra y empaqueta. | Personal insuficiente, contratación urgente o llamadas que quedaron sin contestar. |
| [Salvatore’s: empleo](https://www.salvatorestomatopies.com/careers/) | Un puesto reúne pedidos telefónicos, reservas y apoyo a camareros. | Que se aplique a Madison North Livingston: la vacante no identifica sucursal. |
| [NY Pie: aviso de Franklin](https://www.linkedin.com/jobs/view/team-member-at-ny-pie-nashville-4420664523) | Caja combina llamadas, pedidos, cobros y otras tareas. | Una fecha exacta a partir del texto relativo de LinkedIn ni volumen de llamadas. |
| [Seminole: balance del evento de Glass Nickel](https://seminole26-5.squarespace.com/events) | El organizador relata dificultades telefónicas y ayuda adicional del dueño para el evento de Fitchburg del 11/03/2025. | Respaldo actual: el evento es anterior al corte del 14/10/2025 y se conserva como antecedente de menor prioridad. Tampoco prueba varios clientes identificados, una cifra de llamadas o que pase todos los fines de semana. La fecha corresponde al evento, no a la publicación del balance. |
| [Pappy’s: reseñas de St. Louis](https://www.tripadvisor.co.uk/Restaurant_Review-g44881-d1052764-Reviews-Pappy_s_Smokehouse-Saint_Louis_Missouri.html) | AMarie525 describe una hora de fila en julio de 2026, en una reseña publicada el 17/08/2026. La FAQ oficial confirma el canal telefónico por separado. | Una llamada perdida. La autora también describe comida servida en menos de cinco minutos después de pedir. |
| [Pizza Lucé: reseñas de Downtown](https://www.tripadvisor.co.uk/Restaurant_Review-g43323-d444556-Reviews-Pizza_Luce_Downtown-Minneapolis_Minnesota.html) | Autores distintos describen una buena experiencia telefónica en 2022 y actividad de noches de partido en 2023–2024. | Funcionamiento actual o mala atención telefónica. Se conserva como antecedente histórico. |
| [Downtown Pizza: contacto](https://downtownpizzasc.com/contact) | Los datos publicados en el código confirman teléfono y comparan la rapidez del pedido online en horas de trabajo. | Un episodio de saturación. La respuesta está en JSON-LD —texto estructurado para buscadores—, no en el formulario visible. |

## Fuentes o usos que dejamos afuera

| Fuente o resultado | Por qué no lo usamos para esa afirmación | Cómo afecta al caso |
| --- | --- | --- |
| [FindGlocal: publicación de Prince’s South](https://www.findglocal.com/US/Nashville/238604926540881/Prince%27s-Hot-Chicken-South) | El buscador mostraba una invitación a pedir por teléfono, pero abrir la página devolvió error y recuperar el HTML devolvió un bloqueo. No se leyó el post. | No agrega la segunda señal. La queja original de Brad S sí se conserva por separado. |
| [Sidehustles: puesto de Southwood Valley](https://sidehustles.com/job/to-go-southwood-valley-effb7c59/) y [portal de empleo de Wings ’N More](https://wingsnmore.com/careers/) | La mención útil al teléfono aparecía en el resumen del agregador. No se pudo comprobar en el texto original del empleador; Paycom solo cargó la aplicación con JavaScript. | Se conserva una pista, sin ascender el caso. No se atribuye al empleador el resumen de otra herramienta. |
| [Grubhub: Chengdu Impression](https://www.grubhub.com/restaurant/chengdu-impression-2545-n-halsted-st-chicago/285709/reviews) | El contenido no se pudo leer con el acceso utilizado. | Los fragmentos no suman puntos. El bloqueo no demuestra ausencia de quejas. |
| Resúmenes automáticos de Tripadvisor, Wanderlog, Restaurantji u otras páginas | Juntan comentarios y pueden perder autor, fecha, local o contexto. | Se intenta llegar al relato individual. No se usa el resumen para afirmar falta de personal o llamadas perdidas. |
| [Copia de Jasmine McGee sobre WingBasket](https://www.roostcafeandbistro.com/wingbasket-37211/) | Se pudo leer, pero falta fecha individual y no se confirma el motivo de la llamada. La autora vio el salón vacío. | Sirve como relato limitado, no prueba de un pico; el caso sigue sin seleccionar. No se confunde fecha del artículo con fecha de la reseña. |
| [Testimonio de Brent’s Northridge](https://brentsdeli.com/northridge-restaurants/) | Fue elegido por la empresa, no muestra fecha y describe demora para pagar. | No se usa como llamada perdida ni como prueba de presión actual. El caso necesita refuerzo. |
| [Publicación de iHeart de 2020 sobre Munhall](https://dve.iheart.com/content/2020-03-19-iheart-western-pa-businesses/) | Describe restricciones de aquella etapa. | Aporta historia del canal, no una segunda señal de presión actual. |
| [FAQ de Five Points](https://fivepointspizza.com/faq/) | Su posible restricción de delivery con alto volumen no ubica un incidente u horario concreto. | Confirma teléfono, pero no suma pico en el criterio aplicado. |
| Formularios genéricos de empleo de [Pete’s](https://petesfamouspizza.com/careers/) y [Brent’s](https://brentsdeli.com/careers/) | Reciben postulaciones, sin describir tareas del puesto ni fechar una necesidad. | No prueban que falte personal. |
| Homónimos y relatos de otra sucursal | El nombre parecido no acredita que sea la misma empresa ni la misma operación. | No se usan el empleo de The Pizza Company en Davison, Michigan, para Munhall, ni Champion Wings de Tupelo para Jonesboro. |
| Directorios de contactos personales como SignalHire o ContactOut | No permiten demostrar qué tareas hace el equipo ni cómo atiende el local. | No se usan sus datos personales para la lista ni como prueba operativa. Los teléfonos elegidos son públicos del negocio. |

## Dos distinciones importantes

**Fuente válida, caso fuera del perfil.** Las páginas oficiales de Arthur Bryant’s, Regents, Greenbush y Chino Bandido sirven para comprobar datos. Justamente esos datos respaldan dejarlos afuera: solo se pudo confirmar una sede publicada. No descartamos la fuente por contradecir la selección.

Lo mismo sucede con [Kim’s Uncle Pizza](https://www.unclepizzawestmont.com/ordering-info): su página reconoce líneas ocupadas y un límite de producción, pero solo se confirmó un restaurante. La señal es útil para entender el problema; el negocio queda fuera del tamaño pedido.

**Fuente comercial, dato que juega en contra.** El [comunicado de kea sobre Flying Pie](https://www.webwire.com/ViewPressRel.asp?aId=302758) describe tanto el problema de 2023 como una prueba de solución. No se usa solo la primera mitad para presentar hoy una oportunidad sin atender. Tampoco se da por demostrada la eficacia o vigencia actual de esa solución.

## Cómo leímos y guardamos la información

Se usaron búsquedas web, lectura de páginas y, en algunos casos, recuperación del HTML público con curl. Python ayudó a leer texto estructurado y a ordenar registros. Recuperar HTML no evita un bloqueo: una página de Cloudflare o una aplicación vacía se registra como acceso fallido.

Cuando abrió una versión de Tripadvisor de otro país, se comprobó que la ficha correspondiera al mismo restaurante. Cambiar el dominio no crea otra reseña ni otra fuente independiente. No se completaron automáticamente años ausentes ni fechas relativas.

La investigación tuvo asistencia de IA. Los programas hacen cuentas y ordenan decisiones; no certifican la verdad de una reseña. No se usaron herramientas pagas, llamadas de prueba ni mensajes a restaurantes. Los documentos públicos conservan las afirmaciones resumidas y enlaces; la revisión humana final sigue pendiente.

## Antigüedad de los comentarios

Se separan comentarios recientes (últimos 12 meses, del 14/10/2025 al 14/10/2026), antiguos y de fecha desconocida. Se conserva lo que un comentario antiguo demuestra sobre aquel momento y se reduce su prioridad; no se descarta automáticamente ni se le borran puntos aceptados. Se registra por separado la fecha de publicación, la del hecho cuando aparece y la de consulta. No se inventa el día a partir de una fecha relativa.

También se separa la presencia de cualquier comentario reciente de su utilidad para el ejercicio. Un elogio sobre comida no renueva una queja telefónica de años atrás. Las copias no verificadas, comentarios de otra sede o textos sin contexto siguen teniendo esos límites aunque se cambie la regla de antigüedad.

Una página oficial permanente puede respaldar un canal publicado aunque no indique fecha. Se registra ese límite y no se la presenta como una novedad. En Google Maps, editar una reseña puede cambiar la fecha mostrada: la última edición no demuestra una visita nueva. [Ayuda oficial de Google Maps](https://support.google.com/maps/answer/6230175).

**A favor:** aprovecha antecedentes y permite revisar primero los casos con respaldo pertinente más cercano. **En contra:** obliga a leer fecha y contexto junto al puntaje; no permite asegurar que un problema antiguo siga existiendo.

## Revisión con las fuentes nuevas

En la revisión inicial se buscaron los **29 casos de aquella cohorte**, por empresa y sucursal, en Google, Reddit y las plataformas de entrega. Se hizo una segunda pasada de búsquedas orientada a comentarios recientes. Yelp tuvo un bloqueo de dominio, por lo que no se completó una revisión individual de sus reseñas. Google Maps tampoco permitió recuperar comentarios originales utilizables. Esos accesos incompletos no se anotan como ausencia de reseñas.

| Fuente | Por qué se probó | Resultado y límite |
| --- | --- | --- |
| Google Maps | Experiencias de una sucursal concreta. | Búsquedas realizadas; sin reseñas originales utilizables. No se aceptaron resúmenes ni comentarios de hoteles cercanos. |
| Yelp | Otra fuente de relatos originales. | Bloqueo del dominio. No se aceptó una copia como reemplazo del original. |
| Reddit local | Relatos sobre cómo se pide y atiende. | Se pudo leer, por ejemplo, el hilo de Joe’s gasolinera. Se descartaron parodias, recomendaciones sin experiencia concreta, otras sedes y originales inaccesibles. |
| DoorDash y Uber Eats | Comentarios de pedidos asociados a fichas de restaurantes. | Se pudieron leer comentarios fechados en varias fichas. No se atribuyen al restaurante problemas del repartidor ni se usa una valoración global como comentario. |

La revisión dejó **9 casos con algún comentario reciente fechado**, de los cuales **2 tienen contexto operativo reciente**. No aparecieron nuevas quejas telefónicas verificadas. El resultado por caso, fechas, fuentes, motivos para no usarlas y límites de acceso están en [COMENTARIOS.md](COMENTARIOS.md).

Ejemplos de decisiones de esta pasada:

- **Litza’s Midvale:** la queja de esperas y cancelaciones es del 27/05/2023. Se guarda como antecedente, sin convertirla en una situación actual. [DoorDash](https://www.doordash.com/store/litzas-pizza-midvale-24681844/).
- **Pequod’s Clybourn:** una clienta del 26/08/2026 relata una demora de entrega. No se determina si la causa fue cocina, repartidor o plataforma. Otra reseña de septiembre dice que llegó a tiempo. No se agregan puntos por teléfono ni se duplica presión ya puntuada. [Uber Eats](https://www.ubereats.com/store/pequods-pizza-chicago/v3x7GVrPXNi90ag_NUALzg).
- **Glass Nickel Fitchburg:** hay entregas anticipadas de 2026. Se conserva ese dato favorable, pero no actualiza el episodio telefónico de 2025. [Uber Eats](https://www.ubereats.com/store/glass-nickel-pizza-co-fitchburg/LOFHpbVHWvWlnNWAeNOW7w).
- **Black’s Lockhart:** se descartaron reseñas de Terry Black’s porque es otra empresa. **Buffalo Joe’s Clark:** se descartó la ficha de Howard por ser otra sucursal. **Krispy Brooklyn:** las esperas de Jersey City o Brooklyn Char en Indiana no se trasladaron al local elegido.

Esto es una revisión pública con fuentes accesibles, no una lectura exhaustiva de todas las reseñas existentes.

## Fuentes de las ocho incorporaciones

La ampliación revisó seis grupos de diez candidatos. [TANDAS.md](TANDAS.md) muestra la decisión y fuente o pista de cada uno. [LISTA-EXPLICADA.md](LISTA-EXPLICADA.md) y [CASOS.md](CASOS.md) incluyen los dos hechos aceptados, sus enlaces y los límites de cada alta.

Se usaron páginas oficiales para el teléfono, la cantidad de sedes y políticas de Mama’s, Zachary’s, Katie’s y Golden Boy. En V Pizza se usó la descripción oficial de caja. En SPIN! se pudo leer el aviso original de Indeed. En Home Run Inn se siguió Careers hasta el portal Paylocity del empleador y se leyó el HTML original; en Delfina se leyó el anuncio original de Craigslist y la página oficial de catering, incluidos los datos de Palo Alto que el lector no mostraba completos. Los datos estructurados ayudan a leer un original; no son otra fuente independiente.

Se revisaron resultados de Reddit y plataformas de entrega para las ocho altas, además de reseñas generales. No se recuperó un relato pertinente nuevo aceptable de Reddit. Algunos originales de TripAdvisor, Indeed, DoorDash y Uber Eats no abrieron: esos intentos quedan incompletos, no se convierten en ausencia de comentarios. No se reiteró la revisión individual bloqueada de Yelp o Google Maps ni se afirmó que se hubiera completado.

Se aceptaron el relato antiguo de fila de nadia y en TripAdvisor de North Beach (12/07/2025), las opiniones favorables de comida de Sarah F y Gabriel M en DoorDash Palo Alto (20/07/2026 y 22/04/2026) y el comentario favorable de servicio y entrega de Frank S en Uber Eats North Beach (11/06/2026). Solo el primero respalda la señal de presión, como antecedente antiguo. Los otros conservan contexto y datos favorables, sin puntos nuevos. Las búsquedas sobre 2026 no actualizaron fechas de reseñas viejas.

Se descartaron para puntuar los fragmentos sin original de Pizza Shuttle, Cane Rosso y Pie Tap; las copias de quejas de Mineo’s y Sizzle Pie; el anuncio de otra operación de Delfina; los homónimos de Home Slice y Goodfellas; formularios que solo piden el teléfono del postulante; y bases de contactos personales. Los ejemplos ficticios de planes de negocio no prueban la operación de Picasso’s.

También se conservó evidencia que puede ir en contra: Sally’s anunció en 2020 una solución online junto con su problema telefónico. Un proveedor afirma haber ampliado las líneas de Imperial, pero el PDF no pudo leerse; es una pista comercial sin confirmación de su operación actual. No se toma ninguno de esos relatos como prueba de que el problema siga abierto.

## Fuentes de las cinco incorporaciones siguientes

En las dos últimas tandas, las búsquedas de avisos laborales permitieron encontrar nombres y luego contrastarlos con páginas de la marca. HOTLIPS también se investigó a partir de un nombre sugerido por conocimiento previo del modelo; no se atribuye su descubrimiento a un directorio. Buscar un nombre y confirmar un dato son pasos distintos.

- **HOTLIPS Pizza:** [primera señal](https://www.hotlipspizza.com/), [segunda señal](https://www.hotlipspizza.com/jobs) y [perfil/contacto](https://www.hotlipspizza.com/pearl). Dos páginas de la misma empresa, sin fecha de publicación comprobada. Pearl y Hawthorne son las dos sedes publicadas; no se cuentan tres cerradas ni la cocina central. Ya usan canales digitales y control de capacidad. Atender más llamadas no aumenta la producción. Grubhub bloqueó las reseñas por país: no se acepta el fragmento como prueba.
- **Crushed Red:** [primera señal](https://staffedup.com/crushed-red-kirkwood/), [segunda señal](https://staffedup.com/crushed-red-kirkwood/) y [perfil/contacto](https://crushed-red.com/locations/). Ambas señales salen del mismo puesto, no son pruebas independientes. Aviso sin fecha comprobada; no demuestra falta de empleados. Cinco fichas oficiales: Creve Coeur, Kirkwood, Chesterfield, Clayton y Overland Park. Photoshoot49 publicó el 03/06/2026 una opinión favorable sobre comida y atención de mostrador/mesa, sin dificultad telefónica; no agrega puntos.
- **Billy G's:** [primera señal](https://staffedup.com/billygskirkwood/), [segunda señal](https://staffedup.com/billygskirkwood/) y [perfil/contacto](https://billygskirkwood.com/order/). Mismo aviso para las dos señales, sin puntos por presión ni contratación. Se cuentan Kirkwood y Chesterfield (https://billygs.com/chesterfield/), sin sumar otras marcas del grupo Gianino. La web también ofrece pedidos online; para agregar bebidas alcohólicas indica llamar. TripAdvisor no abrió: sus fragmentos no se aceptan como reseñas verificadas.
- **Holland Farms Bakery & Deli:** [primera señal](https://hollandfarms.com/manlius/), [segunda señal](https://staffedup.com/holland-farms-bakery-deli-manlius/) y [perfil/contacto](https://hollandfarms.com/manlius/). Dos sedes publicadas: Yorkville y Manlius. Encaje como deli con panadería, no como restaurante tradicional de salón. No se suman puntos por reglas normales del retiro express ni por una vacante. Se excluyen reseñas de Yorkville y copias sin original de Google/Yelp; no se verificó comentario reciente de Manlius.
- **Birria LES:** [primera señal](https://jobtoday.com/us/job/cashier-and-line-cooks-YRd2LY?locale=en-US), [segunda señal](https://jobtoday.com/us/job/cashier-and-line-cooks-YRd2LY?locale=en-US) y [perfil/contacto](https://www.doordash.com/business/birria-les-13501665/). Dos señales del mismo aviso. El aviso dice dos locales; se prefieren las cinco direcciones publicadas en DoorDash: Rivington, St Marks, Chelsea, Bedford y Astoria. Website es ficha comercial, no dominio oficial confirmado. Teléfono y dirección en https://www.restaurantji.com/ny/astoria/birria-les-astoria-/ y https://restaurantguru.com/Birria-LES-Astoria-New-York: se usan como directorios de contacto, no sus copias de reseñas. Confirmar teléfono y conteo al contactar. No se aceptan sitios de muestra de OrderSave ni comentarios de otras marcas de birria.

Se aceptan avisos originales de StaffedUp y JobToday para describir tareas publicadas. No se usa la fecha de rastreo como publicación ni una vacante como prueba de falta de empleados. Las páginas de muestra de OrderSave no se identificaron como sitio oficial de Birria LES: quedan fuera. Las copias de Teal no sustituyen un aviso original inaccesible. Grubhub bloqueado por país y fragmentos de TripAdvisor sin original legible no prueban experiencias. **Ventaja:** se puede rastrear cada afirmación; **límite:** lo publicado puede estar desactualizado y requiere confirmación comercial.

## Fuentes y decisiones de las tandas nueve y diez

Los nombres aparecieron en búsquedas de tareas telefónicas en avisos y resultados sobre pedidos de comida. El filtro se hizo antes de aceptar una fila. La procedencia y decisión de los veinte están en [TANDAS.md](TANDAS.md).

- **Super Taco:** [aviso del empleador en Snagajob](https://www.snagajob.com/jobs/1303458429) para tareas de Franklin; [web de la marca](https://www.supertacomex.com/) para teléfono y cuatro sedes con horario. Mack Road está en remodelación y no se cuenta como activo. Dos tareas del mismo aviso no son fuentes independientes. Su etiqueta Today no se convirtió en fecha absoluta.
- **Little Chef:** [aviso original en Indeed](https://www.indeed.com/viewjob?jk=1ba99e6d1b3b1320) para Ocean Beach; [web propia](https://littlechefcatering.us/) para dos direcciones y teléfono. Los testimonios copiados sin fecha de esa web no se usaron como reseñas recientes. Los comentarios favorables originales de Uber Eats están detallados en COMENTARIOS.
- **Beau Jo’s:** se siguió el [empleo oficial](https://www.beaujos.com/about-us/employment/) hasta ADP; el portal pidió un navegador compatible y no mostró el puesto. Las copias de Teal/Tallo no sustituyen esa comprobación. Se deja pendiente, sin sumar.
- **Flying Pie Pizzaria, Idaho:** el [comunicado de kea del 30/03/2023](https://www.webwire.com/ViewPressRel.asp?aId=302758) anuncia pruebas de atención con IA. Sirve como evidencia en contra de asumir una necesidad sin resolver; el proveedor no es una evaluación independiente y la nota no demuestra continuidad ni éxito en 2026. No se mezcla con la marca de Oregón.
- **Sugarfire y Mike Duffy’s:** los avisos leídos mencionan carryout y teléfono o atención presencial, pero no se obtuvo una afirmación inequívoca de pedidos de comida por teléfono que cumpla el mismo criterio. No se mezclan puestos para completar la señal. Sugarfire publica once fichas; Mike Duffy’s, tres, pese a un encabezado de dos.
- **Cadenas grandes y perfiles no resueltos:** Newk’s y Taziki’s publican más de cien sedes; Mellow Mushroom declara más de 160. Se descartan por tamaño antes de buscar quejas. Para otros localizadores que no expusieron el listado completo se registró el límite, sin fabricar un conteo actual desde resúmenes o notas viejas.

**Ventaja:** filtrar primero evita dedicar el mismo tiempo a un negocio fuera del perfil. **Límite:** una fuente inaccesible o una búsqueda sin resultado deja una decisión provisional; no demuestra que el restaurante carezca del problema.

## Herramientas que todavía no son fuente de esta entrega

Apollo.io queda por evaluar como fuente externa de candidatos. No se consultó su base para esta versión y ningún dato de los 27 casos se atribuye a Apollo. La documentación de una herramienta describe funciones; no equivale a recuperar ni verificar empresas dentro de ella.
