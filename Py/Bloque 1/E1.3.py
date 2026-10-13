tabla_mult = input("Dime la tabla: ")

for i in range(11):
    mult = int(i)*int(tabla_mult)
    print(f"{i: >2}" ," * ",tabla_mult," = ", f"{mult: >3}")