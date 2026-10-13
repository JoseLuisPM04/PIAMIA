import csv
import json
from pathlib import Path

RUTA_LIMPIO = Path(__file__).parent / "datos" / "ventas_limpio.csv"
RUTA_RECHAZOS = Path(__file__).parent / "datos" / "errores.json"

def crearInforme(header, validos, rechazos):
    with open(RUTA_LIMPIO, "w", newline="", encoding="UTF-8") as f:
        escr = csv.DictWriter(f, header)
        escr.writeheader()
        escr.writerows(validos)
    with open(RUTA_RECHAZOS, "w", newline="") as j:
        json.dump(rechazos, j, indent=2) 