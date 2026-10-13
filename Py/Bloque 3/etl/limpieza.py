import datetime

formato = "%Y-%m-%d"

lineas = []
rechazos = []

def validar(linea):
    if len(linea) != 5:
        raise ValueError("Numero de datos incorrecto")
    datetime.datetime.strptime(linea["fecha"], formato)
    linea["producto"] = str(linea["producto"])
    if linea["producto"] == '':
        raise ValueError("Producto nulo")
    linea["unidades"] = int(linea["unidades"])
    linea["precio_unitario"] = float(linea["precio_unitario"])

    linea["vendedor"] = str(linea["vendedor"])
    if linea["vendedor"] == '':
        raise ValueError("Vendedor nulo")
    return linea

def limpiarDatos(datos):
    for n, linea in enumerate(datos, start=2):
        try:
            limpia = validar(linea)
        except(ValueError, KeyError) as e:
            rechazos.append({"linea": n, "motivo" :str(e)})
            continue
        lineas.append(limpia)
    return lineas, rechazos

