#Вычислить число Пи c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# Пи = 4*(-1)**n / (2*n + 1)
import math
d = float(input('Задайте точность d:\n'))

def find_pi(d):
    sum = 0
    n = 0
    sum_next = 4
    while abs(sum_next - sum) >= d: 
        sum = sum + 4 * math.pow ((-1), n ) / (2 * n + 1)
        sum_next = sum + 4 * math.pow ((-1), n + 1 ) / (2 * n + 2)
        n = n + 1      
    return round(sum/d)*d 
print(f'Число Пи с заданной точностью {d}: {find_pi(d)}')   