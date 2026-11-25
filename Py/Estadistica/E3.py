""". Dado un conjunto data de observaciones, ajusta una normal usando la media y desviación poblacional del conjunto. 
Crea una función normal_tasks(data, x, p) que:

Cree un NormalDist ajustado a data.
Calcule la probabilidad P(X <= x) (CDF).
Calcule el percentil (inversa) inv_cdf(p): el valor y tal que P(X <= y) = p.
Devuelva además el z-score de x usando (x - mean)/stdev.

Usa statistics.NormalDist.
"""
from statistics import NormalDist, mean, stdev

nums = [4,6,8,10,12]
media = mean(nums)
desviacion = stdev(nums)

dist = NormalDist(media, desviacion)
print(f"P(7): {dist.cdf(7.0)}")
print(f"inv_cdf(7): {dist.inv_cdf()}")
print(f"z-score(7): {dist.zscore(float(7.0))}")