import csv
from pathlib import Path

RUTA = Path(__file__).parent / "CSV" / "iris.csv"

with open(RUTA, newline="") as f:
    filas = list(csv.DictReader(f))
 
for fila in filas:
    fila["largo_pet"] = float(fila["largo_pet"])
    fila["ancho_pet"] = float(fila["ancho_pet"])
    fila["largo_sep"] = float(fila["largo_sep"])
    fila["ancho_sep"] = float(fila["ancho_sep"])

clases = {r["clase"] for r in filas}
medias = []
for clase in clases:
    sum_la_pet = 0
    sum_an_pet = 0
    sum_la_sep = 0
    sum_an_sep = 0
    long = 0
    for fila in filas:
        if fila["clase"] == clase:
            sum_la_pet += fila["largo_pet"] 
            sum_an_pet += fila["ancho_pet"]
            sum_la_sep += fila["largo_sep"]
            sum_an_sep += fila["ancho_sep"]
            long += 1 
    medias.append({"clase" : clase, "media_la_pet" : round(float(sum_la_pet/long),2),"media_an_pet": round(float(sum_an_pet/long),2),"media_la_sep": round(float(sum_la_sep/long),2),"media_an_sep": round(float(sum_an_sep/long),2)})
print(medias)
