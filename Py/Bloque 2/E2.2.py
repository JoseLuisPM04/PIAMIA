# Deduplicar conservando el orden de aparición original. Es decir, elimina las copias repetidas de una lista.

lista = [1,2,3,7,5,3,2,1]
lista_sin = []

for i in range(len(lista)-1):
    if lista[i] not in lista_sin:
        lista_sin.append(lista[i])

print(lista_sin)