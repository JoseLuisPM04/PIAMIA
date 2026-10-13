import csv



def cargarDatos(ruta):
    with open(ruta, newline="") as f:
        datos = list(csv.DictReader(f))
    return datos
    