# Criterio de selección y prioridad

**Perfil.** Buscamos cadenas de EEUU, con 2–15 sucursales y cocina casual de volumen, como posibles compradores de una solución para atender pedidos y consultas telefónicas. El perfil determina inclusión; la evidencia determina prioridad. Una empresa puede ser un lead sin una queja pública.

**Origen y selección.** Hay 154 candidatos con revisión registrada: 29 iniciales, de los que se conservaron 12; otros 100 en diez tandas, que aportaron 15; y 25 del export gratuito de Apollo, con tres incorporaciones. Así llegamos a 27 del discovery con IA más tres de Apollo. La revisión combinó búsquedas, lectura de fuentes y comprobación de marca y sucursal, con distinta profundidad. En esa etapa se buscaban dos hechos útiles por caso. Los no incorporados incluían empresas fuera de perfil y otras sin respaldo suficiente; no se afirma que las 124 restantes carezcan de potencial comercial. El [embudo y sus registros](README.md#cómo-llegamos-a-estos-30) permiten seguir esas decisiones.

**Lote del piloto.** Entregamos 30 frente a la meta de 40. Es la selección del discovery, no una nueva clasificación completa de los 154. `locales.csv` se acepta como entrada; Python controla país y sucursales, sin certificar nuevamente toda su información comercial. En el flujo actual, una evidencia pendiente reduce prioridad sin excluir a una empresa del perfil.

**Evidencia.** El discovery consultó webs, empleos y testimonios públicos. La corrida entregada capturó páginas oficiales enlazadas y conservó texto, URL y fecha. Priorizamos pedidos y consultas telefónicas, tareas compartidas, presión de demanda y dificultades publicadas. Una vacante o una cola presencial no demuestra llamadas perdidas. Los problemas atribuidos a varias sucursales tienen más valor que una señal aislada.

**IA y Python.** La IA propuso candidatos e interpretó documentos con prompts versionados. Las respuestas quedan separadas del código. Python valida citas, agrega indicadores y calcula la prioridad; la persona define el objetivo y los criterios. Los modos de ejecución están en la [guía](comprobacion_codex/README.md).

**Resultado.** Los 30 permanecen como leads: 14 tienen señales telefónicas y 16 evidencia pendiente, con menor prioridad. El puntaje ordena el contacto; no estima ganancia, intención de compra ni volumen de llamadas perdidas. Las bandas y reglas están en [Arquitectura](ARQUITECTURA.md).
