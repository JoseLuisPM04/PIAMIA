# Agenda: diccionario de contactos con alta, baja, búsqueda y listado ordenado, en un bucle de menú.

agenda = {
    "Jesus" : 64,
    "Selu" : 12,
    "Rocio" : 23,
    "Lucas" : 31
}

def Alta():
    nombre = input("Dime el nombre: ")
    numero = input("Dime el numero: ")
    agenda[nombre] = numero

def Baja():
    nombre = input("Dime el nombre: ")
    del agenda[nombre]

def Busqueda():
    nombre = input("Dime el nombre: ")
    print(agenda[nombre])

def Listar():
    print(dict(sorted(agenda.items())))


def Menu():
    while True:
        print("1. Alta")
        print("2. Baja")
        print("3. Busqueda")
        print("4. Listado")
        print("5. Salir")
        elec = int(input("Dime tu eleccion: "))
        match elec:
            case 1:
                Alta()
            case 2:
                Baja()
            case 3:
                Busqueda()
            case 4:
                Listar()
            case 5:
                break
            case _:
                print("Opcion invalida")
Menu()
