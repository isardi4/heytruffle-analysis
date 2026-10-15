# Los 30 prospectos del CSV, explicados

La lista contiene posibles compradores, priorizados para validar la necesidad. Todos tienen encaje de perfil y una señal de operación telefónica en la investigación previa. No se exige una queja para incluirlos. No se comprobó que los 30 pierdan llamadas.

## Selección y procedencia

Se revisaron cadenas de 2–15 locales en EE. UU., cocina casual de volumen y pedidos para llevar. Se conservaron las que tenían pedidos telefónicos, tareas que incluyen llamadas o un rol telefónico explícito, junto con contexto para formular una pregunta comercial. Dos señales pueden provenir de la misma publicación; no representan dos incidentes independientes. Los 27 candidatos de IA y tres de Apollo se revisaron con fuentes públicas; el nombre sugerido por IA no es evidencia.

Se integra la investigación original con el reproceso sobre texto capturado. Una captura sin señal o una descarga fallida no anula una fuente revisada anteriormente. Cuando no está el texto en el corpus actual, se declara pendiente de recaptura; no se lo presenta como una extracción LLM nueva.

## Prioridad calculada por Python

Regla prioridad-v3: base 80 para dificultad telefónica explícita; 50 para tareas compartidas con el teléfono o pedidos telefónicos junto con demanda/límite de capacidad; 30 para evidencia exploratoria de canal u operación telefónica; 15 si el argumento depende de antecedentes antiguos. Antigüedad se aplica antes que las otras bandas.

Bonificaciones por presencia de señales: canal de pedidos +5, tareas compartidas +5, demanda +5, atribución a la sucursal +3, texto de ambas fuentes disponible +3, publicación operativa fechada en los últimos 365 días +3. El total de bonificaciones se limita a 19 puntos, o 9 para antecedentes antiguos. Si una dificultad explícita estuviera atribuida a varias sucursales, +5 por sucursal adicional, máximo +15 dentro del mismo límite de 19; hoy no hay cobertura para aplicar ese bono. Varias citas no se cuentan como incidentes. El número de locales de la cadena no es el número de locales afectados.

El puntaje ordena la investigación y el contacto; no estima ingresos, disposición de compra ni porcentaje de llamadas perdidas. El volumen telefónico no está medido. Las políticas de espera, las vacantes y las colas presenciales se explican como señales indirectas. La fecha de captura no se usa como fecha de publicación. Empates: nombre de empresa. Cálculo reproducible con fecha de corte 2026-10-15.

| Orden | Empresa | Prioridad | Puntos |
|---|---|---|---:|
| 1 | Joe's Kansas City Bar-B-Que | Alta: dificultad telefónica publicada | 88 |
| 2 | Katie's Pizza & Pasta Osteria | Alta: dificultad telefónica publicada | 88 |
| 3 | Litza's Pizza | Media: hipótesis operativa respaldada | 69 |
| 4 | Birria LES | Media: hipótesis operativa respaldada | 66 |
| 5 | Downtown Pizza | Media: hipótesis operativa respaldada | 66 |
| 6 | Home Run Inn | Media: hipótesis operativa respaldada | 66 |
| 7 | Pappy's Smokehouse | Media: hipótesis operativa respaldada | 66 |
| 8 | Pizzeria Delfina | Media: hipótesis operativa respaldada | 66 |
| 9 | Bar-Bill Tavern | Media: hipótesis operativa respaldada | 63 |
| 10 | Billy G's | Media: hipótesis operativa respaldada | 63 |
| 11 | Crushed Red | Media: hipótesis operativa respaldada | 63 |
| 12 | HOTLIPS Pizza | Media: hipótesis operativa respaldada | 63 |
| 13 | Holland Farms Bakery & Deli | Media: hipótesis operativa respaldada | 63 |
| 14 | Little Chef Chinese | Media: hipótesis operativa respaldada | 63 |
| 15 | NY Pie Nashville | Media: hipótesis operativa respaldada | 63 |
| 16 | Pequod's Pizza | Media: hipótesis operativa respaldada | 63 |
| 17 | Prime Pizza | Media: hipótesis operativa respaldada | 63 |
| 18 | SPIN! Pizza | Media: hipótesis operativa respaldada | 63 |
| 19 | Salvatore's Tomato Pies | Media: hipótesis operativa respaldada | 63 |
| 20 | Super Taco Mexican Restaurants | Media: hipótesis operativa respaldada | 63 |
| 21 | Black's Barbecue | Media: hipótesis operativa respaldada | 61 |
| 22 | Mama's Pizza Omaha | Media: hipótesis operativa respaldada | 60 |
| 23 | Sickies Garage Burgers & Brews | Media: hipótesis operativa respaldada | 58 |
| 24 | The Kickin' Chicken | Media: hipótesis operativa respaldada | 58 |
| 25 | V Pizza | Media: hipótesis operativa respaldada | 58 |
| 26 | Zachary's Chicago Pizza | Exploratoria: encaje y operación telefónica | 41 |
| 27 | Dallas BBQ | Exploratoria: encaje y operación telefónica | 33 |
| 28 | Pizza Luce | Revalidar antecedente antiguo | 24 |
| 29 | Golden Boy Pizza | Revalidar antecedente antiguo | 23 |
| 30 | Glass Nickel Pizza | Revalidar antecedente antiguo | 18 |

## 1. Joe's Kansas City Bar-B-Que

**Motivo de inclusión:** Es el argumento publicado más directo sobre dificultad para comunicarse: la empresa pide reintentar si las líneas están ocupadas.

**Utilidad posible:** Si parte de esas llamadas busca pedir o consultar, podría servir una atención que responda cuando el equipo no puede. Falta saber cuántas quedan sin atender y por qué.

**Qué validar:** Cuando las líneas están ocupadas, ¿cuántas llamadas quedan sin atender y quién se encarga de ellas?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 80 + bono aplicado 8 = 88. Componentes: {"base": 80, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 0, "atribucion_local": 0, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 88 |
| `why_now` | Sin novedad fechada. La instrucción oficial de volver a llamar permite preguntar por las llamadas que no llegan a atender. |
| `notes` | Sucursal: Gas Station · 3002 W 47th. No se midieron llamadas perdidas ni su causa. La web enlaza pickup online aunque el texto de contacto diga que no recibe pedidos online: no se afirma exclusividad telefónica. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: Es el argumento publicado más directo sobre dificultad para comunicarse: la empresa pide reintentar si las líneas están ocupadas. Qué validar: Cuando las líneas están ocupadas, ¿cuántas llamadas quedan sin atender y quién se encarga de ellas? Prioridad: Alta: dificultad telefónica publicada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://www.joeskc.com/pages/contact-us Perfil y contacto: https://www.joeskc.com/pages/locations Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 2. Katie's Pizza & Pasta Osteria

**Motivo de inclusión:** La propia empresa explica una dificultad de acceso telefónico y el uso del teléfono para pedir, aunque con una política restrictiva.

**Utilidad posible:** Podría necesitar ayuda para responder consultas o a quienes no pueden pedir online. Hay que distinguir capacidad de líneas, atención y cocina.

**Qué validar:** ¿Sigue vigente en Rock Hill la política de líneas ocupadas? ¿El límite está en las líneas, en quién atiende o en la cocina? ¿Qué solución usan hoy?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 80 + bono aplicado 8 = 88. Componentes: {"base": 80, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 0, "atribucion_local": 0, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 88 |
| `why_now` | Sin fecha de publicación comprobable. Confirmar la política de líneas ocupadas todavía publicada y qué cambió desde que se escribió. |
| `notes` | Sucursal: Rock Hill · 9568 Manchester Road. La página conserva texto de dos sedes y retiro en auto: su vigencia no está confirmada. Se cuentan cuatro fichas con dirección, teléfono y horario: Rock Hill, Town & Country, Ballpark Village y Crestwood; no las aperturas anunciadas ni otra marca del grupo. El aviso Host/Hostess de Rock Hill en StaffedUp aporta tareas de teléfono y salón, sin puntos adicionales. No se midieron llamadas perdidas. No se toma la actualización global de Indeed como fecha de una reseña. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: La propia empresa explica una dificultad de acceso telefónico y el uso del teléfono para pedir, aunque con una política restrictiva. Qué validar: ¿Sigue vigente en Rock Hill la política de líneas ocupadas? ¿El límite está en las líneas, en quién atiende o en la cocina? ¿Qué solución usan hoy? Prioridad: Alta: dificultad telefónica publicada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://katies.com/pages/important-info Perfil y contacto: https://katies.com/pages/rock-hill Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 3. Litza's Pizza

**Motivo de inclusión:** Hay una descripción oficial de mayo de 2026 del salón de Midvale lleno en noches de fin de semana, junto con la opción de pedir por teléfono.

**Utilidad posible:** El salón concurrido y los pedidos telefónicos podrían pedir atención al mismo tiempo. La publicación no informa llamadas perdidas.

**Qué validar:** Los viernes y sábados por la noche, ¿la misma persona atiende el salón y las llamadas? ¿Qué ocurre cuando coinciden?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 50 + bono aplicado 19 = 69. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 5, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 3}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 69 |
| `why_now` | La nota oficial del 06/05/2026 permite preguntar por la cobertura telefónica de las noches de fin de semana en Midvale. |
| `notes` | Sucursal: 835 East Fort Union Boulevard. Dos hechos de la misma página oficial. Comparte edificio con Hires Big H, que no cuenta como otra sede. La reseña de esperas de repartidores es del 27/05/2023: antecedente antiguo, sin llamada perdida comprobada. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: Hay una descripción oficial de mayo de 2026 del salón de Midvale lleno en noches de fin de semana, junto con la opción de pedir por teléfono. Qué validar: Los viernes y sábados por la noche, ¿la misma persona atiende el salón y las llamadas? ¿Qué ocurre cuando coinciden? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://www.litzaspizza.com/blog/midvale-family-pizza/ Perfil y contacto: https://www.litzaspizza.com/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 4. Birria LES

**Motivo de inclusión:** El aviso identifica la sede y combina atención telefónica, presencial y preparación de entregas.

**Utilidad posible:** Las tareas podrían coincidir; falta confirmar su reparto y si las llamadas generan un problema.

**Qué validar:** En Astoria, ¿quién responde el teléfono cuando caja está cobrando o empaquetando entregas?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 16 = 66. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 3}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 66 |
| `why_now` | El anuncio se publicó el 01/06/2026: permite preguntar por el funcionamiento del puesto, sin suponer falta de personal. |
| `notes` | Sucursal: Astoria · 31-27 Ditmars Blvd. Dos señales del mismo aviso. El aviso dice dos locales; se prefieren las cinco direcciones publicadas en DoorDash: Rivington, St Marks, Chelsea, Bedford y Astoria. Website es ficha comercial, no dominio oficial confirmado. Teléfono y dirección en https://www.restaurantji.com/ny/astoria/birria-les-astoria-/ y https://restaurantguru.com/Birria-LES-Astoria-New-York: se usan como directorios de contacto, no sus copias de reseñas. Confirmar teléfono y conteo al contactar. No se aceptan sitios de muestra de OrderSave ni comentarios de otras marcas de birria. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El aviso identifica la sede y combina atención telefónica, presencial y preparación de entregas. Qué validar: En Astoria, ¿quién responde el teléfono cuando caja está cobrando o empaquetando entregas? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://jobtoday.com/us/job/cashier-and-line-cooks-YRd2LY?locale=en-US Perfil y contacto: https://www.doordash.com/business/birria-les-13501665/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 5. Downtown Pizza

**Motivo de inclusión:** El código de la página oficial dice que se puede pedir por teléfono y que Toast suele ser más rápido cuando hay más trabajo. Es un respaldo menos visible.

**Utilidad posible:** Puede haber una diferencia operativa entre canales. La comparación no demuestra llamadas perdidas ni permite identificar la causa.

**Qué validar:** En Spartanburg, ¿por qué recomiendan Toast frente al teléfono cuando hay más trabajo? ¿La diferencia está en atender, tomar el pedido o prepararlo?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 50 + bono aplicado 16 = 66. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 5, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 66 |
| `why_now` | Sin novedad fechada. Confirmar la vigencia de la comparación teléfono/Toast publicada en los datos de la web. |
| `notes` | Sucursal: 156 Magnolia St. Las respuestas están en los datos FAQ del código HTML, no visibles en el formulario: menor confianza y vigencia pendiente. No se suman puntos de falla ni presión. Spartanburg e Inman tienen sistemas separados. Las reseñas recientes de comida no prueban dificultad telefónica. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El código de la página oficial dice que se puede pedir por teléfono y que Toast suele ser más rápido cuando hay más trabajo. Es un respaldo menos visible. Qué validar: En Spartanburg, ¿por qué recomiendan Toast frente al teléfono cuando hay más trabajo? ¿La diferencia está en atender, tomar el pedido o prepararlo? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://downtownpizzasc.com/contact Perfil y contacto: https://downtownpizzasc.com/contact Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 6. Home Run Inn

**Motivo de inclusión:** El empleador describe para Hillside una combinación explícita de pedidos por teléfono y atención del salón.

**Utilidad posible:** Es una buena pregunta sobre cobertura: no sabemos si el puesto se reparte entre varias personas o si ya tienen un sistema de apoyo.

**Qué validar:** En Hillside, ¿la misma persona toma pedidos telefónicos y ubica o ayuda con las mesas? ¿Quién cubre las llamadas cuando sale del puesto?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 16 = 66. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 3}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 66 |
| `why_now` | El portal del empleador registra publicación del aviso el 21/09/2026. Preguntar por la organización actual del puesto, sin atribuir urgencia ni falta de personal. |
| `notes` | Sucursal: Hillside · 60 S Mannheim Rd. Fuente original Paylocity enlazada desde Careers oficial, leída en HTML público. La fecha publicada aparece en los datos del listado; no demuestra que las tareas hayan empezado ese día. Se cuentan seis restaurantes del directorio actual; se excluyen fábricas, supermercados y locales cerrados de directorios antiguos. No se puntúa la frase genérica sobre trabajar en un ambiente rápido. Sin comentario reciente original aceptado. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El empleador describe para Hillside una combinación explícita de pedidos por teléfono y atención del salón. Qué validar: En Hillside, ¿la misma persona toma pedidos telefónicos y ubica o ayuda con las mesas? ¿Quién cubre las llamadas cuando sale del puesto? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://recruiting.paylocity.com/Recruiting/Jobs/Details/4520679 Perfil y contacto: https://www.homeruninnpizza.com/restaurants/hillside/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 7. Pappy's Smokehouse

**Motivo de inclusión:** Combina pedidos telefónicos oficiales con una experiencia presencial reciente que describe una hora de fila.

**Utilidad posible:** Conviene preguntar si quienes atienden esa fila también responden pedidos remotos. La fila por sí sola no demuestra un problema telefónico.

**Qué validar:** En los días con más fila, ¿los pedidos por teléfono los toma el mismo equipo? ¿Quedan llamadas sin atender?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 16 = 66. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 5, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 3}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 66 |
| `why_now` | Reseña publicada el 17/08/2026 sobre una visita de julio: preguntar por cobertura telefónica en días concurridos. |
| `notes` | Sucursal: St. Louis · 3106 Olive St. Una sola reseña sobre fila presencial. La misma autora dice que la comida llegó en menos de cinco minutos tras pedir: se conserva ese dato favorable. No se midieron llamadas perdidas. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: Combina pedidos telefónicos oficiales con una experiencia presencial reciente que describe una hora de fila. Qué validar: En los días con más fila, ¿los pedidos por teléfono los toma el mismo equipo? ¿Quedan llamadas sin atender? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.tripadvisor.co.uk/Restaurant_Review-g44881-d1052764-Reviews-Pappy_s_Smokehouse-Saint_Louis_Missouri.html Perfil y contacto: https://www.pappyssmokehouse.com/contact Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 8. Pizzeria Delfina

**Motivo de inclusión:** Hay un puesto local fechado que combina llamadas y salón. El pedido telefónico comprobado es catering: el argumento comercial queda limitado a ese canal y a consultas.

**Utilidad posible:** Podría ayudar a cubrir consultas y catering cuando recepción está ocupada; antes de proponer pedidos individuales hay que confirmar que los acepten por teléfono.

**Qué validar:** En Palo Alto, ¿el Host/Cashier recibe pedidos individuales por teléfono o solo consultas y catering? ¿Quién cubre esas llamadas mientras recibe comensales?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 16 = 66. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 3}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 66 |
| `why_now` | Aviso de Palo Alto publicado el 06/10/2026. Sirve para revisar tareas telefónicas y de salón; no prueba falta de personal ni una contratación urgente. |
| `notes` | Sucursal: Palo Alto · 651 Emerson Street. Anuncio y página de catering leídos en HTML público porque la herramienta web no mostraba todo. Fecha del aviso y datos del puesto en HTML/JSON del original. Las tres sedes de catering no reemplazan las cuatro de la marca. Se excluye el aviso de Delfina Restaurant Mission: es otra operación. DoorDash de Palo Alto tiene reseñas favorables de comida del 22/04/2026 y 20/07/2026; no prueban dificultad telefónica. El canal confirmado es catering con anticipación; no demuestra pedidos individuales inmediatos. Por qué se elige: Hay un puesto local fechado que combina llamadas y salón. El pedido telefónico comprobado es catering: el argumento comercial queda limitado a ese canal y a consultas. Qué validar: En Palo Alto, ¿el Host/Cashier recibe pedidos individuales por teléfono o solo consultas y catering? ¿Quién cubre esas llamadas mientras recibe comensales? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.craigslist.org/view/d/palo-alto-host-cashier-pizzeria-delfina/6CCYBMgqvxpfbqfA7EQJsg Perfil y contacto: https://www.pizzeriadelfina.com/location/palo-alto/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 9. Bar-Bill Tavern

**Motivo de inclusión:** East Aurora admite pedidos por teléfono y publica mayor espera en fines de semana y un cierre del canal online al agotar capacidad.

**Utilidad posible:** Podrían acumularse consultas mientras el equipo atiende el servicio. No sabemos si el cierre online hace aumentar las llamadas.

**Qué validar:** Cuando se cierra el pedido online por capacidad, ¿aumentan las llamadas? ¿Las pueden atender o el límite es la cocina?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 5, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin novedad fechada. Preguntar cómo cubren llamadas en fines de semana y al agotarse la capacidad del pedido online. |
| `notes` | Sucursal: East Aurora · 185 Main St; retiros en 191 Main St Rear. El argumento es de East Aurora; no se traslada a Clarence o Rochester, que no aceptan esos pedidos telefónicos/online. El retiro de East Aurora no es una cuarta sede. Contestar más llamadas no aumenta la capacidad de cocina. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: East Aurora admite pedidos por teléfono y publica mayor espera en fines de semana y un cierre del canal online al agotar capacidad. Qué validar: Cuando se cierra el pedido online por capacidad, ¿aumentan las llamadas? ¿Las pueden atender o el límite es la cocina? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.barbill.com/faqs Perfil y contacto: https://www.barbill.com/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 10. Billy G's

**Motivo de inclusión:** El aviso local permite identificar quién combina llamadas y atención de pedidos presenciales.

**Utilidad posible:** Podría necesitar cobertura mientras caja atiende o entrega pedidos; no se comprobó una falla.

**Qué validar:** En Kirkwood, ¿quién cubre las llamadas cuando Carryout cobra o entrega un pedido?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin fecha comprobada del aviso. Revisar cómo funciona actualmente el puesto Carryout. |
| `notes` | Sucursal: Kirkwood · 131 W Argonne Dr. Mismo aviso para las dos señales, sin puntos por presión ni contratación. Se cuentan Kirkwood y Chesterfield (https://billygs.com/chesterfield/), sin sumar otras marcas del grupo Gianino. La web también ofrece pedidos online; para agregar bebidas alcohólicas indica llamar. TripAdvisor no abrió: sus fragmentos no se aceptan como reseñas verificadas. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El aviso local permite identificar quién combina llamadas y atención de pedidos presenciales. Qué validar: En Kirkwood, ¿quién cubre las llamadas cuando Carryout cobra o entrega un pedido? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://staffedup.com/billygskirkwood/ Perfil y contacto: https://billygskirkwood.com/order/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 11. Crushed Red

**Motivo de inclusión:** Un puesto local combina llamadas, cobro y atención de mesas.

**Utilidad posible:** Esas tareas podrían competir por atención; falta conocer el reparto real por turno.

**Qué validar:** En Kirkwood, ¿quién cubre el teléfono cuando el Wine Tender lleva bebidas a las mesas?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin novedad operativa fechada. Confirmar que el reparto de tareas publicado siga vigente. |
| `notes` | Sucursal: Kirkwood · 140 S Kirkwood Rd. Ambas señales salen del mismo puesto, no son pruebas independientes. Aviso sin fecha comprobada; no demuestra falta de empleados. Cinco fichas oficiales: Creve Coeur, Kirkwood, Chesterfield, Clayton y Overland Park. Photoshoot49 publicó el 03/06/2026 una opinión favorable sobre comida y atención de mostrador/mesa, sin dificultad telefónica; no agrega puntos. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: Un puesto local combina llamadas, cobro y atención de mesas. Qué validar: En Kirkwood, ¿quién cubre el teléfono cuando el Wine Tender lleva bebidas a las mesas? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://staffedup.com/crushed-red-kirkwood/ Perfil y contacto: https://crushed-red.com/locations/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 12. HOTLIPS Pizza

**Motivo de inclusión:** Publica una derivación concreta de pedidos hacia el teléfono y horarios de mayor trabajo.

**Utilidad posible:** Las llamadas podrían coincidir con el servicio; también puede tratarse de un límite de cocina ya gestionado.

**Qué validar:** Cuando desactivan pedidos online, ¿quién responde las llamadas? ¿Necesitan atender consultas o la cocina ya no puede aceptar pedidos?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 5, "atribucion_local": 0, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin novedad fechada. Confirmar cómo cubren las llamadas durante la política publicada de cierre temporal online. |
| `notes` | Sucursal: Pearl · 721 NW 9th Ave, Suite 150. Dos páginas de la misma empresa, sin fecha de publicación comprobada. Pearl y Hawthorne son las dos sedes publicadas; no se cuentan tres cerradas ni la cocina central. Ya usan canales digitales y control de capacidad. Atender más llamadas no aumenta la producción. Grubhub bloqueó las reseñas por país: no se acepta el fragmento como prueba. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: Publica una derivación concreta de pedidos hacia el teléfono y horarios de mayor trabajo. Qué validar: Cuando desactivan pedidos online, ¿quién responde las llamadas? ¿Necesitan atender consultas o la cocina ya no puede aceptar pedidos? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://www.hotlipspizza.com/jobs Perfil y contacto: https://www.hotlipspizza.com/pearl Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 13. Holland Farms Bakery & Deli

**Motivo de inclusión:** Hay un canal de pedidos de comida y un puesto de la misma sede que comparte teléfono y mostrador.

**Utilidad posible:** El teléfono podría competir con la atención presencial; primero conviene conocer el peso del deli frente a los encargos de pastelería.

**Qué validar:** En Manlius, ¿cuántas llamadas son por comidas del deli y quién atiende mientras el mostrador está ocupado?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin novedad fechada. Confirmar vigencia del puesto y volumen de pedidos de comida por teléfono. |
| `notes` | Sucursal: Manlius · 343 Fayette St. Dos sedes publicadas: Yorkville y Manlius. Encaje como deli con panadería, no como restaurante tradicional de salón. No se suman puntos por reglas normales del retiro express ni por una vacante. Se excluyen reseñas de Yorkville y copias sin original de Google/Yelp; no se verificó comentario reciente de Manlius. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: Hay un canal de pedidos de comida y un puesto de la misma sede que comparte teléfono y mostrador. Qué validar: En Manlius, ¿cuántas llamadas son por comidas del deli y quién atiende mientras el mostrador está ocupado? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://staffedup.com/holland-farms-bakery-deli-manlius/ Perfil y contacto: https://hollandfarms.com/manlius/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 14. Little Chef Chinese

**Motivo de inclusión:** El puesto identifica Ocean Beach y combina llamadas, caja y apoyo de cocina y mostrador.

**Utilidad posible:** El teléfono podría competir con caja o preparación. El encaje es teléfono más mostrador; no se atribuye servicio de salón completo.

**Qué validar:** En Ocean Beach, ¿quién responde las llamadas cuando caja cobra o ayuda con preparaciones en cocina?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin fecha absoluta comprobada del aviso. Confirmar que estas tareas describan la operación actual antes de ofrecer una solución. |
| `notes` | Sucursal: Ocean Beach · 4910 Newport Ave. Las dos señales provienen del mismo puesto. Sin fecha absoluta comprobada, sin puntos por ambiente rápido ni vacante. Dos direcciones oficiales: Ocean Beach y Sorrento Valley. Operación centrada en takeout, con encaje parcial respecto de la hipótesis de personal en salón. En Uber Eats, Jeremy R. (21/06/2026) y Sarah H. (23/06/2026) elogian la comida: algún comentario reciente sí, dificultad telefónica no. TripAdvisor tiene experiencias antiguas; no se acepta como reciente el año 2026 del título ni testimonios copiados sin fecha en la web. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El puesto identifica Ocean Beach y combina llamadas, caja y apoyo de cocina y mostrador. Qué validar: En Ocean Beach, ¿quién responde las llamadas cuando caja cobra o ayuda con preparaciones en cocina? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.indeed.com/viewjob?jk=1ba99e6d1b3b1320 Perfil y contacto: https://littlechefcatering.us/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 15. NY Pie Nashville

**Motivo de inclusión:** El anuncio de Franklin asigna a caja llamadas, ingreso de pedidos, cobro y preparación de otros productos.

**Utilidad posible:** La atención telefónica podría competir con esas tareas. La descripción del puesto no muestra una dificultad real ni falta de empleados.

**Qué validar:** En Franklin, ¿caja atiende las llamadas mientras cobra y prepara productos? ¿Hay alguien que la cubra cuando se acumula trabajo?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | El anuncio de Franklin sirve para preguntar por la organización del puesto. Su fecha aparece de forma relativa; confirmar vigencia sin inventar una urgencia. |
| `notes` | Sucursal: 1441 New Highway 96 West. Los dos hechos provienen del mismo anuncio. No hay una queja aceptada ni se suman puntos por contratar. El sitio también publica testimonios favorables sin fecha; no se toman como reseñas recientes verificadas. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El anuncio de Franklin asigna a caja llamadas, ingreso de pedidos, cobro y preparación de otros productos. Qué validar: En Franklin, ¿caja atiende las llamadas mientras cobra y prepara productos? ¿Hay alguien que la cubra cuando se acumula trabajo? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.linkedin.com/jobs/view/team-member-at-ny-pie-nashville-4420664523 Perfil y contacto: https://www.nypienashville.com/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 16. Pequod's Pizza

**Motivo de inclusión:** La empresa identifica un pico concreto de 18 a 20 y permite anticipar pedidos por teléfono; se puede plantear una pregunta operativa específica.

**Utilidad posible:** Los pedidos telefónicos podrían competir con la atención presencial durante ese horario. No se comprobó que eso ocurra.

**Qué validar:** Entre las 18 y las 20, ¿quién atiende los pedidos por teléfono y qué pasa si ya está atendiendo a otra persona?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 5, "atribucion_local": 0, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin novedad telefónica fechada. Revisar cobertura del pico publicado de 18 a 20; la demora de entrega de agosto de 2026 no se atribuye al teléfono. |
| `notes` | Sucursal: Chicago · 2207 N Clybourn. Los dos hechos principales provienen de la misma FAQ. Usan Whale Tale para ciertos retiros, lo que puede aliviar trabajo. Emily W relata demora de entrega el 26/08/2026 y Jasmine G entrega a tiempo el 26/09/2026; no se conoce la causa ni se suman puntos nuevos. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: La empresa identifica un pico concreto de 18 a 20 y permite anticipar pedidos por teléfono; se puede plantear una pregunta operativa específica. Qué validar: Entre las 18 y las 20, ¿quién atiende los pedidos por teléfono y qué pasa si ya está atendiendo a otra persona? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://pequodspizza.com/faqs/ Perfil y contacto: https://pequodspizza.com/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 17. Prime Pizza

**Motivo de inclusión:** El puesto de Brea combina teléfono, mostrador, cobro y empaquetado. Es una descripción local concreta, sin evidencia de falla.

**Utilidad posible:** Compartir esas tareas puede hacer difícil responder en algún momento. Falta comprobar cómo se reparten por turno y si hay llamadas sin atender.

**Qué validar:** En Brea, ¿el cajero sigue tomando llamadas mientras cobra y empaqueta? ¿Cómo cubren las llamadas cuando se juntan esas tareas?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin novedad fechada. El aviso de cajero permite preguntar por el reparto actual de tareas en Brea; confirmar su vigencia. |
| `notes` | Sucursal: 235 E Imperial Highway. Aviso sin fecha de publicación comprobable: no se afirma contratación vigente ni falta de personal. Dos tareas del mismo puesto no son dos pruebas de llamadas perdidas. El directorio publica 13 sedes con datos de atención; se excluyen tres anunciadas. Los comentarios de comida de 2026 no prueban el problema. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El puesto de Brea combina teléfono, mostrador, cobro y empaquetado. Es una descripción local concreta, sin evidencia de falla. Qué validar: En Brea, ¿el cajero sigue tomando llamadas mientras cobra y empaqueta? ¿Cómo cubren las llamadas cuando se juntan esas tareas? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.indeed.com/viewjob?jk=e88f1eed0ffb8ee3 Perfil y contacto: https://primepizza.com/locations Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 18. SPIN! Pizza

**Motivo de inclusión:** El aviso corresponde a Richardson y combina pedidos telefónicos con apoyo al salón.

**Utilidad posible:** Puede servir una cobertura cuando caja ayuda a los camareros. Falta comprobar si ya tienen esa cobertura y qué demanda reciben.

**Qué validar:** En Richardson, cuando caja ayuda a los camareros, ¿quién toma los pedidos por teléfono? ¿Queda alguna llamada sin atender?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin fecha de publicación comprobable del aviso. Validar el reparto actual de tareas de caja en Richardson. |
| `notes` | Sucursal: Richardson · 348 W Campbell Rd. Descripción leída en el aviso original de Indeed. Dos hechos del mismo puesto, no dos pruebas independientes. Se cuentan las 13 sedes con ficha del directorio oficial; no se usan conteos de terceros. La mención genérica de picos de cocina no suma presión ni falta de personal. Sin comentario reciente aceptado; el original de DoorDash no abrió. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El aviso corresponde a Richardson y combina pedidos telefónicos con apoyo al salón. Qué validar: En Richardson, cuando caja ayuda a los camareros, ¿quién toma los pedidos por teléfono? ¿Queda alguna llamada sin atender? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.indeed.com/viewjob?jk=c309fd6de51c1b87 Perfil y contacto: https://www.spinpizza.com/locations/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 19. Salvatore's Tomato Pies

**Motivo de inclusión:** La descripción Host/Phone combina pedidos telefónicos, reservas y apoyo a camareros. Falta atribuir ese puesto a Madison.

**Utilidad posible:** El reparto de tareas coincide con la hipótesis del ejercicio a nivel de cadena. No se comprobó que se aplique al contacto elegido.

**Qué validar:** En Madison North Livingston, ¿el puesto Host/Phone también toma reservas y ayuda a los camareros? ¿Quién cubre las llamadas mientras lo hace?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 0, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin novedad fechada. Confirmar primero que el puesto general Host/Phone corresponda a Madison y describa su operación actual. |
| `notes` | Sucursal: Contacto elegido: Madison North Livingston · 10 N Livingston. Aviso general sin sucursal ni fecha indicadas. Teléfono y dirección corresponden a Madison North Livingston; las tareas todavía no están confirmadas para esa sede. Sin llamada perdida ni falta de personal comprobadas. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: La descripción Host/Phone combina pedidos telefónicos, reservas y apoyo a camareros. Falta atribuir ese puesto a Madison. Qué validar: En Madison North Livingston, ¿el puesto Host/Phone también toma reservas y ayuda a los camareros? ¿Quién cubre las llamadas mientras lo hace? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://www.salvatorestomatopies.com/careers/ Perfil y contacto: https://www.salvatorestomatopies.com/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 20. Super Taco Mexican Restaurants

**Motivo de inclusión:** El aviso del empleador vincula llamadas y atención de mesas en Franklin, una sede identificada.

**Utilidad posible:** Las llamadas podrían coincidir con el servicio de mesas; el aviso no demuestra que queden sin atender.

**Qué validar:** En Franklin, ¿quién cubre el teléfono cuando el servidor está atendiendo mesas o empaquetando retiros?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 13 = 63. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 63 |
| `why_now` | Sin fecha absoluta comprobada del aviso. Confirmar que estas tareas describan la operación actual antes de ofrecer una solución. |
| `notes` | Sucursal: Franklin · 7131 Franklin Blvd. Dos hechos del mismo aviso, no dos fuentes independientes. La fecha relativa Today y Urgently hiring no se convierten en fecha absoluta ni en falta de personal. Cuatro sedes con horario publicado: Franklin, Grant Line, Calvine y Laguna. Mack Road está marcado REMODELING y queda fuera del conteo activo, aunque figure en el pie de página. Hay pedidos online. Uber Eats muestra opiniones favorables antiguas de 2022–enero de 2025, sin comentario reciente aceptado ni falla telefónica. No se usan copias de Google en Wanderlog como originales. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El aviso del empleador vincula llamadas y atención de mesas en Franklin, una sede identificada. Qué validar: En Franklin, ¿quién cubre el teléfono cuando el servidor está atendiendo mesas o empaquetando retiros? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.snagajob.com/jobs/1303458429 Perfil y contacto: https://www.supertacomex.com/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 21. Black's Barbecue

**Motivo de inclusión:** Publica una restricción concreta de pedidos cuando tiene mucho trabajo. Es una oportunidad condicionada a entender la causa.

**Utilidad posible:** Podría necesitar ayuda para responder consultas o explicar límites. Si el único problema es que la cocina no puede preparar más comida, atender más pedidos no lo resuelve.

**Qué validar:** Cuando solo aceptan pedidos presenciales, ¿es por capacidad de cocina o porque no pueden atender llamadas? ¿Se pierden también consultas que podrían responder?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 50 + bono aplicado 11 = 61. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 61 |
| `why_now` | Sin novedad fechada. Distinguir un problema de atención de un límite de cocina antes de proponer una solución. |
| `notes` | Sucursal: 215 N Main St. Política oficial, no relato de llamada perdida. También hay pedidos online. No confundir con Terry Black’s. Si solo falta capacidad de cocina, este argumento no justifica vender atención telefónica. Puede ser un límite de cocina; validar utilidad de atender más llamadas. Por qué se elige: Publica una restricción concreta de pedidos cuando tiene mucho trabajo. Es una oportunidad condicionada a entender la causa. Qué validar: Cuando solo aceptan pedidos presenciales, ¿es por capacidad de cocina o porque no pueden atender llamadas? ¿Se pierden también consultas que podrían responder? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://www.blacksbbq.com/locations/lockhart/pick-up-delivery Perfil y contacto: https://www.blacksbbq.com/locations Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 22. Mama's Pizza Omaha

**Motivo de inclusión:** El canal está identificado para Midtown y la empresa publica momentos de mayor actividad en su política de grupos.

**Utilidad posible:** Conviene comprobar si las llamadas y la atención presencial coinciden en esos horarios y cómo se cubren.

**Qué validar:** En Midtown, ¿también tienen más trabajo las noches de viernes a domingo? ¿Quién cubre los pedidos telefónicos mientras atienden el salón?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 10 = 60. Componentes: {"base": 50, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 5, "atribucion_local": 0, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 60 |
| `why_now` | Sin novedad telefónica fechada. La FAQ permite preguntar por las noches de viernes a domingo; confirmar aplicación y vigencia en Midtown. |
| `notes` | Sucursal: Midtown · 715 N Saddle Creek Road. La FAQ trata reservas de grupos y muestra actualización del 22/07/2025; no es un comentario reciente. Cuatro sedes publicadas: Midtown, West Omaha, La Vista y Tiburon. Hay canal online. No hay llamadas perdidas comprobadas ni una reseña reciente original aceptada. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El canal está identificado para Midtown y la empresa publica momentos de mayor actividad en su política de grupos. Qué validar: En Midtown, ¿también tienen más trabajo las noches de viernes a domingo? ¿Quién cubre los pedidos telefónicos mientras atienden el salón? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://mamaspizzaomaha.com/faqs/ Perfil y contacto: https://mamaspizzaomaha.com/locations/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 23. Sickies Garage Burgers & Brews

**Motivo de inclusión:** El aviso de Host de Las Vegas combina teléfono y pedidos para llevar dentro de sus responsabilidades.

**Utilidad posible:** El mismo puesto recibe y sienta clientes, cobra y debe manejar varias prioridades; eso permite preguntar cómo cubren el teléfono cuando coinciden tareas.

**Qué validar:** En Las Vegas, ¿quién atiende las llamadas cuando el host gestiona los pedidos para llevar y recibe a los clientes? ¿Se acumulan llamadas en esos momentos?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 8 = 58. Componentes: {"base": 50, "canal_pedidos": 0, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
| `company_name` | Sickies Garage Burgers & Brews |
| `city` | Las Vegas |
| `state` | NV |
| `locations_count` | 13 |
| `cuisine` | Hamburguesas, alitas y casual dining |
| `phone` | +17257355400 |
| `website` | https://sickiesburgers.com/ |
| `source_url` | https://www.indeed.com/viewjob?jk=156af54be52f371c |
| `signal_1` | El aviso de Host de Las Vegas asigna responder el teléfono y tomar pedidos to-go cuando hace falta. |
| `signal_2` | Ese puesto también recibe, sienta y maneja pagos de comensales; pide manejar varias prioridades. |
| `priority_score` | 58 |
| `why_now` | No hay fecha de publicación comprobable; el aviso describe tareas, no vacante vigente ni urgencia actual. |
| `notes` | Sucursal: Las Vegas · 6629 S Las Vegas Blvd, Bldg J, Ste B120. El directorio oficial publica 13 sedes y confirma que Las Vegas está abierta. El aviso menciona responder teléfono y tomar to-go, pero no especifica si los pedidos llegan por teléfono; confirmar en conversación. No demuestra llamadas perdidas ni falta de personal. Las tareas no confirman que los pedidos to-go entren por teléfono. Por qué se elige: El aviso de Host de Las Vegas combina teléfono y pedidos para llevar dentro de sus responsabilidades. Qué validar: En Las Vegas, ¿quién atiende las llamadas cuando el host gestiona los pedidos para llevar y recibe a los clientes? ¿Se acumulan llamadas en esos momentos? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.indeed.com/viewjob?jk=156af54be52f371c Perfil y contacto: https://sickiesburgers.com/locations/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 24. The Kickin' Chicken

**Motivo de inclusión:** El aviso de Host de West Ashley combina pedidos para llevar y respuesta telefónica en una operación que describe como rápida y de alta energía.

**Utilidad posible:** La coincidencia de tareas se ajusta al problema que buscamos validar; el aviso no demuestra llamadas perdidas ni insuficiencia de personal.

**Qué validar:** En West Ashley, ¿quién atiende el teléfono cuando el host gestiona pedidos para llevar y recibe a los clientes? ¿Se acumulan llamadas en los turnos rápidos?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 50 + bono aplicado 8 = 58. Componentes: {"base": 50, "canal_pedidos": 0, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
| `company_name` | The Kickin' Chicken |
| `city` | Charleston |
| `state` | SC |
| `locations_count` | 6 |
| `cuisine` | Pollo frito, alitas y comida casual |
| `phone` | +18437665292 |
| `website` | https://kickinchicken.com/ |
| `source_url` | https://www.indeed.com/viewjob?jk=900e178cb8264cb4 |
| `signal_1` | El aviso de Host de West Ashley incluye manejar pedidos to-go y responder el teléfono. |
| `signal_2` | El mismo puesto describe turnos de alta energía, ritmo rápido y apoyo donde se necesite. |
| `priority_score` | 58 |
| `why_now` | El aviso no tiene fecha comprobable; sirve como evidencia de las tareas descritas, no como contratación vigente. |
| `notes` | Sucursal: West Ashley · 1179 Sam Rittenberg Blvd. El sitio oficial cuenta seis locales en Charleston y enlaza West Ashley. Teléfono del local obtenido de su página oficial. Las dos señales provienen del mismo aviso; no se interpreta “ritmo rápido” como una llamada perdida. Sin contacto comercial realizado. Las tareas no confirman que los pedidos to-go entren por teléfono. Por qué se elige: El aviso de Host de West Ashley combina pedidos para llevar y respuesta telefónica en una operación que describe como rápida y de alta energía. Qué validar: En West Ashley, ¿quién atiende el teléfono cuando el host gestiona pedidos para llevar y recibe a los clientes? ¿Se acumulan llamadas en los turnos rápidos? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.indeed.com/viewjob?jk=900e178cb8264cb4 Perfil y contacto: https://kickinchicken.com/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 25. V Pizza

**Motivo de inclusión:** La descripción oficial combina teléfono con trabajo en las mesas, una coincidencia directa con la hipótesis del ejercicio.

**Utilidad posible:** Esas tareas podrían competir por la misma persona. Primero hay que confirmar que así se trabaje en San Marco.

**Qué validar:** En San Marco, ¿el cajero que toma llamadas también lleva comida y limpia mesas? ¿Quién lo cubre cuando sale al salón?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 50 + bono aplicado 8 = 58. Componentes: {"base": 50, "canal_pedidos": 0, "tareas_compartidas": 5, "demanda": 0, "atribucion_local": 0, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 58 |
| `why_now` | Sin novedad fechada. Confirmar en San Marco la descripción general de caja y reparto de tareas. |
| `notes` | Sucursal: San Marco · 1406 Hendricks Ave. Aviso sin fecha comprobable ni sucursal fija. El directorio tiene 13 sedes con atención y una futura en Durbin: se excluye Durbin. El texto del puesto todavía menciona 12 y dos en construcción; se prefiere el directorio detallado. No se supone falta de personal, llamadas perdidas ni actividad urgente por contratar. Las tareas no confirman que los pedidos to-go entren por teléfono. Por qué se elige: La descripción oficial combina teléfono con trabajo en las mesas, una coincidencia directa con la hipótesis del ejercicio. Qué validar: En San Marco, ¿el cajero que toma llamadas también lleva comida y limpia mesas? ¿Quién lo cubre cuando sale al salón? Prioridad: Media: hipótesis operativa respaldada; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://www.vpizza.com/jobs/cashier-and-food-runner/ Perfil y contacto: https://www.vpizza.com/locations/san-marco-jacksonville-fl/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 26. Zachary's Chicago Pizza

**Motivo de inclusión:** Hay una regla horaria concreta del teléfono y una forma publicada de coordinar pedidos con la espera de mesas.

**Utilidad posible:** Sirve para preguntar por el reparto de llamadas y atención de mesas después de las 16. No sabemos si la regla responde a una dificultad.

**Qué validar:** Después de las 16, ¿quién toma los pedidos para llevar por teléfono? ¿Cómo se coordina con las personas que esperan mesa?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 30 + bono aplicado 11 = 41. Componentes: {"base": 30, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 41 |
| `why_now` | Sin problema reciente fechado. Validar cómo funciona la restricción de pedidos telefónicos para comer en el local después de las 16. |
| `notes` | Sucursal: Pleasant Hill · 140 Crescent Drive. No se suman puntos por una espera posible ni por una regla horaria. Se cuentan seis sedes del menú actual, incluida Livermore abierta; se deja atrás el texto antiguo que dice cinco. Hay pedidos online y plataformas. Sin comentario operativo reciente original aceptado. La regla de espera no demuestra saturación; prioridad exploratoria. Por qué se elige: Hay una regla horaria concreta del teléfono y una forma publicada de coordinar pedidos con la espera de mesas. Qué validar: Después de las 16, ¿quién toma los pedidos para llevar por teléfono? ¿Cómo se coordina con las personas que esperan mesa? Prioridad: Exploratoria: encaje y operación telefónica; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://zacharys.com/locations/pleasant-hill/ Perfil y contacto: https://zacharys.com/locations/pleasant-hill/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 27. Dallas BBQ

**Motivo de inclusión:** La empresa publica un rol específico de Phone Operator y ofrece takeout y delivery en sus locales.

**Utilidad posible:** También enumera por separado Phone Operator, Host y Takeout Packing en un ambiente fast-paced; es una operación donde vale la pena validar cómo se reparte la demanda.

**Qué validar:** En Times Square, ¿el puesto Phone Operator toma pedidos de comida? ¿Qué pasa con las llamadas en los picos y cómo se coordina con takeout packing?

**Procedencia:** Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas.

**Cálculo:** base 30 + bono aplicado 3 = 33. Componentes: {"base": 30, "canal_pedidos": 0, "tareas_compartidas": 0, "demanda": 0, "atribucion_local": 0, "texto_de_ambas_fuentes_disponible": 3, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
| `company_name` | Dallas BBQ |
| `city` | New York |
| `state` | NY |
| `locations_count` | 12 |
| `cuisine` | Barbacoa, pollo y casual dining |
| `phone` | +12122219000 |
| `website` | https://www.dallasbbq.com/ |
| `source_url` | https://www.dallasbbq.com/careers |
| `signal_1` | La empresa publica el puesto Phone Operator, mantiene teléfono para Times Square y ofrece takeout y delivery diarios. |
| `signal_2` | El equipo se describe como fast-paced; enumera por separado Phone Operator y Takeout Packing. |
| `priority_score` | 33 |
| `why_now` | La página de empleo y menú está activa al corte, pero no publica fecha de contratación ni medida de llamadas. |
| `notes` | Sucursal: Times Square · 241 W 42nd Street. La página oficial afirma 12 locales; el menú enlaza diez sedes existentes y una nueva de Secaucus, por lo que el total puede estar cambiando. El teléfono y dirección de Times Square están en su ficha oficial. Tener un Phone Operator puede significar que ya resolvieron cobertura; no se afirma una falla. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: La empresa publica un rol específico de Phone Operator y ofrece takeout y delivery en sus locales. Qué validar: En Times Square, ¿el puesto Phone Operator toma pedidos de comida? ¿Qué pasa con las llamadas en los picos y cómo se coordina con takeout packing? Prioridad: Exploratoria: encaje y operación telefónica; regla prioridad-v3. Procedencia: Texto de ambas fuentes disponible en la captura; respuestas LLM simuladas. Fuente de señal 2: https://www.dallasbbq.com/careers Perfil y contacto: https://www.dallasbbq.com/careers Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 28. Pizza Luce

**Motivo de inclusión:** Hay antecedentes de uso del teléfono y actividad en noches de partido en Downtown, pero son de 2022–2024 y la atención telefónica fue buena.

**Utilidad posible:** Es una hipótesis histórica sobre coincidencia de tareas y demanda. Requiere confirmar canal y funcionamiento actuales antes de usarla comercialmente.

**Qué validar:** En Downtown, ¿siguen tomando pedidos por teléfono y aumenta esa demanda en noches de partido? ¿Cómo cubren esas llamadas hoy?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 15 + bono aplicado 9 = 24. Componentes: {"base": 15, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 5, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 24 |
| `why_now` | Antecedentes de 2022–2024, fuera de los últimos 12 meses. Sin disparador actual; confirmar primero canal y funcionamiento. |
| `notes` | Sucursal: Downtown Minneapolis · 119 N 4th St. La reseña telefónica del 14/10/2022 es favorable. Los relatos de actividad son de 2023–2024, de autores distintos. No se comprobó un comentario operativo reciente de Downtown ni llamadas perdidas. Puntaje histórico de 40, con menor prioridad comercial por antigüedad y relación indirecta con el problema. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: Hay antecedentes de uso del teléfono y actividad en noches de partido en Downtown, pero son de 2022–2024 y la atención telefónica fue buena. Qué validar: En Downtown, ¿siguen tomando pedidos por teléfono y aumenta esa demanda en noches de partido? ¿Cómo cubren esas llamadas hoy? Prioridad: Revalidar antecedente antiguo; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.tripadvisor.co.uk/Restaurant_Review-g43323-d444556-Reviews-Pizza_Luce_Downtown-Minneapolis_Minnesota.html Perfil y contacto: https://pizzaluce.com/locations Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 29. Golden Boy Pizza

**Motivo de inclusión:** Combina un canal telefónico oficial con una fila concreta de la misma sucursal, aunque el antecedente es antiguo y el encaje es menor.

**Utilidad posible:** La coincidencia posible es entre teléfono y ventanilla. Al ser solo takeout, no se plantea el problema de empleados atendiendo mesas.

**Qué validar:** En North Beach, ¿quién responde pedidos telefónicos mientras atienden la fila de ventanilla? ¿Qué cambió desde el episodio de julio de 2025?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 15 + bono aplicado 8 = 23. Componentes: {"base": 15, "canal_pedidos": 5, "tareas_compartidas": 0, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 23 |
| `why_now` | Antecedente del 12/07/2025, fuera de los últimos 12 meses. Sin urgencia actual; confirmar funcionamiento y si vuelve a haber filas similares. |
| `notes` | Sucursal: North Beach · 542 Green Street. Encaje parcial: takeout sin salón, con tres sedes oficiales. Una fila presencial antigua no demuestra volumen telefónico ni que el mismo empleado atienda ambos canales. El relato de fila del 10/08/2025 también es antiguo. Frank S. el 11/06/2026 elogia servicio y entrega en Uber Eats: se conserva como contrapeso favorable, sin renovar la fila antigua. Los fragmentos de TripAdvisor que aluden a 2026 no se aceptan: la lectura del original no permitió vincularlos a una reseña fechada concreta. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: Combina un canal telefónico oficial con una fila concreta de la misma sucursal, aunque el antecedente es antiguo y el encaje es menor. Qué validar: En North Beach, ¿quién responde pedidos telefónicos mientras atienden la fila de ventanilla? ¿Qué cambió desde el episodio de julio de 2025? Prioridad: Revalidar antecedente antiguo; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://www.tripadvisor.com/Restaurant_Review-g60713-d353911-Reviews-Golden_Boy_Pizza-San_Francisco_California.html Perfil y contacto: https://www.goldenboypizza.com/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## 30. Glass Nickel Pizza

**Motivo de inclusión:** El evento de Fitchburg relaciona dificultad telefónica y actividad adicional, pero es de marzo de 2025 y el organizador transmite relatos ajenos.

**Utilidad posible:** Ese episodio puede servir para preguntar si vuelve a pasar durante promociones. No se presenta como una dificultad actual de la cadena.

**Qué validar:** En la recaudación de marzo de 2025 hubo dificultades telefónicas reportadas: ¿volvieron a ocurrir en eventos posteriores y cómo las cubren hoy?

**Procedencia:** Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM.

**Cálculo:** base 15 + bono aplicado 3 = 18. Componentes: {"base": 15, "canal_pedidos": 0, "tareas_compartidas": 0, "demanda": 0, "atribucion_local": 3, "texto_de_ambas_fuentes_disponible": 0, "publicacion_operativa_reciente": 0}.

| Campo | Valor |
|---|---|
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
| `priority_score` | 18 |
| `why_now` | Antecedente del 11/03/2025, fuera de los últimos 12 meses. Confirmar repetición y cambios en la atención; sin urgencia actual comprobada. |
| `notes` | Sucursal: 3191 Muir Field Rd. Un evento y un organizador que transmite relatos de terceros. Los dos hechos salen del mismo episodio: suma una vez en comunicación, sin sumar de nuevo canal o pico. Hay comentarios favorables de entrega de 2026; no actualizan la queja telefónica ni se traslada a otras sedes. No se midieron llamadas perdidas ni frecuencia de incidentes. Por qué se elige: El evento de Fitchburg relaciona dificultad telefónica y actividad adicional, pero es de marzo de 2025 y el organizador transmite relatos ajenos. Qué validar: En la recaudación de marzo de 2025 hubo dificultades telefónicas reportadas: ¿volvieron a ocurrir en eventos posteriores y cómo las cubren hoy? Prioridad: Revalidar antecedente antiguo; regla prioridad-v3. Procedencia: Respaldo de investigación previa con enlaces; falta recapturar una o ambas fuentes para repetir la extracción LLM. Fuente de señal 2: https://seminole26-5.squarespace.com/events Perfil y contacto: https://www.glassnickelpizza.com/location-overview/ Fuentes investigadas al 14/10/2026; cálculo al 2026-10-15. |

## Alcance de la entrega

30 filas frente a una meta de 40. Se conserva la selección investigada y no se agregan empresas sin argumento para completar la cantidad. El ejercicio permite menos filas con una explicación. Apollo aportó tres incorporaciones de su export de 25; los otros 27 nombres se propusieron con IA y se investigaron. Ver historico/APOLLO-REVISION.md y los respaldos de historico/. No se contactó a los restaurantes.
