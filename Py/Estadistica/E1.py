#1. Crea five_number_summary(nums) que devuelva (min, Q1, median, Q3, max) usando statistics. 
# Usa statistics.quantiles para los cuartiles y statistics.median para la mediana.
from statistics import median, quantiles

nums = [4,6,8,10,12]

print(f"Minimo: {min(nums)}, Q1: {quantiles(nums)[0]}, Median: {median(nums)}, Q3: {quantiles(nums)[2]}, Maximo: {max(nums)}")
