# Respaldo del discovery

Esta carpeta conserva el export original de 25 cuentas de Apollo, decisiones de revisión, fichas e indicadores anteriores. No es una entrada del pipeline actual; para evaluar la entrega, empezá por el [README central](../README.md).

Los archivos de `apollo/` permiten rastrear las incorporaciones de esa fuente. Los demás JSON documentan la investigación y selección iniciales.

La reproducción histórica se solicita explícitamente desde la raíz:

```sh
python3 scripts/preparar_entrega.py --legacy
```

Sus salidas van a `historico/reproduccion_inicial/` y no reemplazan la entrega oficial. El respaldo local comprimido está excluido de Git y no es necesario para ejecutar el proyecto.
