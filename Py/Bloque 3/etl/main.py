
from pathlib import Path
from carga import cargarDatos
from limpieza import limpiarDatos
from informe import crearInforme

RUTA = Path(__file__).parent / "datos" / "ventas_sucio.csv"

datos = cargarDatos(RUTA)

validas, rechazos = limpiarDatos(datos)
header = ["fecha", "producto", "unidades", "precio_unitario", "vendedor"]

crearInforme(header, validas, rechazos)