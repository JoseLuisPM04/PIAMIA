# Estadísticas de una lista de notas: media, máximo, mínimo y cuántas aprobadas, sin usar statistics.

notas = [1,2,3,4,5,6,7,8,9,10]
aprobados = sum(1 for n in notas if n >= 5)

print("Media: ",sum(notas)/ len(notas))
print("Han aprobado: ",aprobados)

print("Maximo: ",max(notas))
print("Minimo: ",min(notas))

