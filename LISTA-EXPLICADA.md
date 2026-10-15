# Lista oficial y prioridad por empresa

Este documento se genera desde el CSV y la auditoría de la comprobación actual. La entrega de la raíz es una copia exacta de ese resultado; no mezcla puntajes históricos.

Se incluyen 30 prospectos por perfil. El perfil determina inclusión; la evidencia determina prioridad. Una fuente faltante o sin señales deja evidencia pendiente, sin descartar al prospecto ni inventar un problema.

## Regla prioridad-v4

Perfil sin evidencia telefónica: 10–14. Antecedentes antiguos: 15–24. Canal exploratorio: 30–49. Hipótesis operativa: 50–69. Dificultad explícita: 80–99. Las bonificaciones usan presencia de señales, alcance, texto y recencia; varias citas no se convierten en varios incidentes. El puntaje no estima probabilidad de compra ni ganancia.

[Arquitectura](ARQUITECTURA.md) · [Guía de ejecución](comprobacion_codex/README.md) · [Componentes de puntaje](comprobacion_codex/auditoria_prioridad.json)

| Empresa | Prioridad | Evidencia | Puntos |
|---|---|---|---:|
| Joe's Kansas City Bar-B-Que | Alta: dificultad telefónica publicada | Señal telefónica | 88 |
| Downtown Pizza | Media: hipótesis operativa respaldada | Señal telefónica | 69 |
| Pequod's Pizza | Media: hipótesis operativa respaldada | Señal telefónica | 68 |
| HOTLIPS Pizza | Media: hipótesis operativa respaldada | Señal telefónica | 63 |
| Zachary's Chicago Pizza | Media: hipótesis operativa respaldada | Señal telefónica | 63 |
| Glass Nickel Pizza | Media: hipótesis operativa respaldada | Señal telefónica | 58 |
| Salvatore's Tomato Pies | Media: hipótesis operativa respaldada | Señal telefónica | 58 |
| Litza's Pizza | Exploratoria: encaje y operación telefónica | Señal telefónica | 41 |
| Pappy's Smokehouse | Exploratoria: encaje y operación telefónica | Señal telefónica | 41 |
| Golden Boy Pizza | Exploratoria: encaje y operación telefónica | Señal telefónica | 38 |
| Billy G's | Exploratoria: encaje y operación telefónica | Señal telefónica | 36 |
| Dallas BBQ | Exploratoria: encaje y operación telefónica | Señal telefónica | 33 |
| Little Chef Chinese | Exploratoria: encaje y operación telefónica | Señal telefónica | 33 |
| Prime Pizza | Exploratoria: encaje y operación telefónica | Señal telefónica | 33 |
| Bar-Bill Tavern | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Birria LES | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Black's Barbecue | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Crushed Red | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Holland Farms Bakery & Deli | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Home Run Inn | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Katie's Pizza & Pasta Osteria | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Mama's Pizza Omaha | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| NY Pie Nashville | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Pizza Luce | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Pizzeria Delfina | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| SPIN! Pizza | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Sickies Garage Burgers & Brews | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| Super Taco Mexican Restaurants | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| The Kickin' Chicken | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |
| V Pizza | Baja: perfil válido; evidencia telefónica pendiente | Pendiente | 10 |

## Joe's Kansas City Bar-B-Que

**Argumento o dato de perfil:** La empresa pide volver a llamar cuando sus teléfonos están ocupados al intentar pedir.

**Segunda señal o pendiente:** La página indica pedidos por teléfono o en persona.

**Prioridad:** base 80 + bonificación aplicada 8 = 88.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Alta: dificultad telefónica publicada Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Gas Station · 3002 W 47th. Fuentes operativas: https://www.joeskc.com/pages/contact-us. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Downtown Pizza

**Argumento o dato de perfil:** El puesto Front of House combina mostrador, pedidos telefónicos y empaquetado.

**Segunda señal o pendiente:** Spartanburg acepta pedidos telefónicos e indica que Toast suele ser más rápido en horas concurridas.

**Prioridad:** base 50 + bonificación aplicada 19 = 69.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Media: hipótesis operativa respaldada Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: 156 Magnolia St. Fuentes operativas: https://downtownpizzasc.com/careers | https://downtownpizzasc.com/contact. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Pequod's Pizza

**Argumento o dato de perfil:** El formulario incluye un puesto llamado Host / Phone entre las posiciones disponibles para solicitar.

**Segunda señal o pendiente:** Pequod’s permite anticipar pedidos por teléfono o por internet.

**Prioridad:** base 50 + bonificación aplicada 18 = 68.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Media: hipótesis operativa respaldada Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Chicago · 2207 N Clybourn. Fuentes operativas: https://pequodspizza.com/employment-application/ | https://pequodspizza.com/faqs/. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## HOTLIPS Pizza

**Argumento o dato de perfil:** HOTLIPS usa el teléfono para controlar los tiempos cuando desactiva temporalmente los pedidos online.

**Segunda señal o pendiente:** La página laboral de HOTLIPS identifica noches y fines de semana como sus períodos de mayor actividad.

**Prioridad:** base 50 + bonificación aplicada 13 = 63.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Media: hipótesis operativa respaldada Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Pearl · 721 NW 9th Ave, Suite 150. Fuentes operativas: https://www.hotlipspizza.com/ | https://www.hotlipspizza.com/jobs. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Zachary's Chicago Pizza

**Argumento o dato de perfil:** Las tareas del host incluyen pedidos por teléfono y mostrador, cobro, ensaladas y levantar mesas.

**Segunda señal o pendiente:** Después de las 16, Zachary’s limita los pedidos telefónicos a takeout.

**Prioridad:** base 50 + bonificación aplicada 13 = 63.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Media: hipótesis operativa respaldada Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Pleasant Hill · 140 Crescent Drive. Fuentes operativas: https://zacharys.com/jobs/ | https://zacharys.com/frequently-asked-questions/. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Glass Nickel Pizza

**Argumento o dato de perfil:** El formulario de empleo incluye un puesto denominado Phones/Counter, sin detallar sus tareas.

**Segunda señal o pendiente:** Glass Nickel indica llamar directamente al local por problemas que necesitan atención inmediata.

**Prioridad:** base 50 + bonificación aplicada 8 = 58.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Media: hipótesis operativa respaldada Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: 3191 Muir Field Rd. Fuentes operativas: https://www.glassnickelpizza.com/careers/ | https://www.glassnickelpizza.com/contact/. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Salvatore's Tomato Pies

**Argumento o dato de perfil:** El puesto combina responder llamadas, recibir y sentar clientes y ayudar con pedidos.

**Segunda señal o pendiente:** Salvatore’s ofrece el teléfono para contacto directo o respuestas urgentes.

**Prioridad:** base 50 + bonificación aplicada 8 = 58.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Media: hipótesis operativa respaldada Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Contacto elegido: Madison North Livingston · 10 N Livingston. Fuentes operativas: https://www.salvatorestomatopies.com/careers/ | https://www.salvatorestomatopies.com/contact/. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Litza's Pizza

**Argumento o dato de perfil:** El sitio invita a pedir por teléfono con anticipación.

**Segunda señal o pendiente:** El selector ofrece llamar para pedir a Midvale, además de Slice.

**Prioridad:** base 30 + bonificación aplicada 11 = 41.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Exploratoria: encaje y operación telefónica Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: 835 East Fort Union Boulevard. Fuentes operativas: https://www.litzaspizza.com/ | https://www.litzaspizza.com/jobs/. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Pappy's Smokehouse

**Argumento o dato de perfil:** Los pedidos de retiro pueden hacerse llamando al teléfono publicado de St. Louis.

**Segunda señal o pendiente:** Pide llamar si se visita tarde porque puede agotar sus productos antes del cierre.

**Prioridad:** base 30 + bonificación aplicada 11 = 41.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Exploratoria: encaje y operación telefónica Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: St. Louis · 3106 Olive St. Fuentes operativas: https://www.pappyssmokehouse.com/contact. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Golden Boy Pizza

**Argumento o dato de perfil:** Golden Boy opera solo para llevar y ofrece llamar por adelantado, pedir presencialmente o delivery.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 30 + bonificación aplicada 8 = 38.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Exploratoria: encaje y operación telefónica Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: North Beach · 542 Green Street. Fuentes operativas: https://www.goldenboypizza.com/. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Billy G's

**Argumento o dato de perfil:** Billy G’s dirige las consultas urgentes y de reservas al host desk por teléfono de 10 a 22.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 30 + bonificación aplicada 6 = 36.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Exploratoria: encaje y operación telefónica Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Kirkwood · 131 W Argonne Dr. Fuentes operativas: https://billygskirkwood.com/contact/. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Dallas BBQ

**Argumento o dato de perfil:** Dallas BBQ publica el puesto Phone Operator, separado de Host y Takeout Packing.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 30 + bonificación aplicada 3 = 33.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Exploratoria: encaje y operación telefónica Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Times Square · 241 W 42nd Street. Fuentes operativas: http://www.dallasbbq.com/careers. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Little Chef Chinese

**Argumento o dato de perfil:** El sitio invita a contactar por teléfono, correo o presencialmente para recibir ayuda.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 30 + bonificación aplicada 3 = 33.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Exploratoria: encaje y operación telefónica Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Ocean Beach · 4910 Newport Ave. Fuentes operativas: https://littlechefcatering.us/. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Prime Pizza

**Argumento o dato de perfil:** Prime Pizza invita a contactar por correo o llamando a sus sucursales.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 30 + bonificación aplicada 3 = 33.

**Validación comercial:** Hay operación telefónica documentada; validar volumen, cobertura y utilidad del producto. Exploratoria: encaje y operación telefónica Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: 235 E Imperial Highway. Fuentes operativas: https://primepizza.com/contact. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: con_senal_telefonica. Regla: prioridad-v4.

## Bar-Bill Tavern

**Argumento o dato de perfil:** Perfil según locales.csv: 3 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: East Aurora · 185 Main St; retiros en 191 Main St Rear. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Birria LES

**Argumento o dato de perfil:** Perfil según locales.csv: 5 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Astoria · 31-27 Ditmars Blvd. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Black's Barbecue

**Argumento o dato de perfil:** Perfil según locales.csv: 4 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: 215 N Main St. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Crushed Red

**Argumento o dato de perfil:** Perfil según locales.csv: 5 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Kirkwood · 140 S Kirkwood Rd. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Holland Farms Bakery & Deli

**Argumento o dato de perfil:** Perfil según locales.csv: 2 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Manlius · 343 Fayette St. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Home Run Inn

**Argumento o dato de perfil:** Perfil según locales.csv: 6 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Hillside · 60 S Mannheim Rd. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Katie's Pizza & Pasta Osteria

**Argumento o dato de perfil:** Perfil según locales.csv: 4 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Rock Hill · 9568 Manchester Road. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Mama's Pizza Omaha

**Argumento o dato de perfil:** Perfil según locales.csv: 4 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Midtown · 715 N Saddle Creek Road. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## NY Pie Nashville

**Argumento o dato de perfil:** Perfil según locales.csv: 4 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: 1441 New Highway 96 West. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Pizza Luce

**Argumento o dato de perfil:** Perfil según locales.csv: 9 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Downtown Minneapolis · 119 N 4th St. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Pizzeria Delfina

**Argumento o dato de perfil:** Perfil según locales.csv: 4 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Palo Alto · 651 Emerson Street. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## SPIN! Pizza

**Argumento o dato de perfil:** Perfil según locales.csv: 13 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Richardson · 348 W Campbell Rd. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Sickies Garage Burgers & Brews

**Argumento o dato de perfil:** Perfil según locales.csv: 13 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Las Vegas · 6629 S Las Vegas Blvd, Bldg J, Ste B120. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## Super Taco Mexican Restaurants

**Argumento o dato de perfil:** Perfil según locales.csv: 4 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: Franklin · 7131 Franklin Blvd. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## The Kickin' Chicken

**Argumento o dato de perfil:** Perfil según locales.csv: 6 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: West Ashley · 1179 Sam Rittenberg Blvd. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.

## V Pizza

**Argumento o dato de perfil:** Perfil según locales.csv: 13 sucursales en United States; operación telefónica por validar.

**Segunda señal o pendiente:** Pendiente: no hay una segunda señal operativa respaldada en esta ejecución.

**Prioridad:** base 10 + bonificación aplicada 0 = 10.

**Validación comercial:** Encaja en el perfil aceptado de locales.csv. Contacto exploratorio para validar uso del teléfono; evidencia operativa pendiente. Sin novedad fechada confirmada.

**Trazabilidad y límites:** Comprobación nueva desde locales.csv. LLM: Codex en conversación mediante respuestas JSON externas; no API. Sucursal: San Marco · 1406 Hendricks Ave. Fuentes operativas: ninguna en esta captura; source_url es la web de perfil, no una prueba de problema. Alcance y citas en resultados_evidencia_llm.csv. Categoría de cocina inferida de citas cuando disponible; validar volumen telefónico antes de calificar definitivamente. Cobertura parcial; no se midieron llamadas perdidas. Sin fichas ni etiquetas históricas. Estado de inclusión: prospecto_por_perfil. Evidencia: evidencia_telefonica_pendiente. Regla: prioridad-v4.
