""" Escribe compare_means(nums) que reciba una lista de números positivos y devuelva un dict con: media aritmética (mean),
    media armónica (harmonic_mean), media geométrica (geometric_mean), desviación poblacional (pstdev)
    y coeficiente de variación (cv = pstdev/mean). """
from statistics import mean, harmonic_mean, geometric_mean, pstdev


nums = [4,6,8,10,12]
resultado = {}

resultado["mean"] = mean(nums)
resultado["harmonic_mean"] = harmonic_mean(nums)
resultado["geometric_mean"] = geometric_mean(nums)
resultado["pstdev"] = pstdev(nums)
resultado["cv"] = pstdev(nums)/mean(nums)
print(resultado)

