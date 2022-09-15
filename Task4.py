#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#*Пример:* 
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

n = int(input(f'Задайте степень числа k:\t'))
koeff = [randint(0, 100) for i in range(n+1)]
print(koeff)

if n != 0:
    def make(n):
        result = []
        for i in range(n):
            if koeff[i] > 1 and n - i > 1:
                result.append(f'{str(koeff[i])}x**{n - i}')
            elif koeff[i] > 1 and n - i == 1:
                result.append(f'{str(koeff[i])}x')
            elif koeff[i] == 1 and n - i > 1:
                result.append(f'x**{n - i})')
            elif koeff[i] == 1 and n - 1 == 1:
                result.append('x')
        if koeff[-1] != 0:
                result.append(str(koeff[-1]))   
        return ' + '.join(result) + ' = 0' 
    print(make(n))  
else:   
    print(f'n должно быть больше нуля, иначе не многочлен')

# from random import randint
# n = int(input(f'Задайте степень числа k:\t'))
# koeff = [randint(0, 100) for i in range(n+1)]
# print(koeff)

# if n != 0:
#     def make(n):
#         str = ''
#         for i in range(n+1):
#             if koeff[i] > 1 and n - i > 1:
#                 str += f'{koeff[i]}x**{n-i} + '
#             elif koeff[i] > 1 and n - i == 1:
#                 str += f'{koeff[i]}x + '
#             elif koeff[i] == 1 and n - i > 1:
#                 str += f'x**{n - i} + '
#             elif koeff[i] == 1 and n - i == 1:
#                 str += f'x'
#             elif koeff[i] > 1 and n - i == 0:
#                 str += f'{koeff[i]} = 0'
#             elif koeff[i] == 0 or koeff[i] == 1:
#                 str += f''
#             else:
#                 str += f'{koeff}*x**{n-i} + '
#         print(str)       
#     make(n)  
# else:   
#     print(f'n должно быть больше нуля, иначе не многочлен')

f = open('task4.txt', 'w')
f.write(make(n))
f.close()