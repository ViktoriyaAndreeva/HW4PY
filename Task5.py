#5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# разбиваем многочлен
def get_to_line(line):
    line = line.replace(' ', '')
    items = line.split("+")
    print(f'Многочлен:', items)
    result = []
    for i in items:
        if '=0' in i:
            koeff = i.split('=0')[0]
            result.append({'koeff': int(koeff),'n': 0})
            continue
        koeff = 1
        if 'x' in i:
            koeff = i.split('x')[0]
            koeff = int(koeff)
            if '*' not in i:
                result.append({'koeff': int(koeff), 'n': 1})
        n = 1
        if '**' in i:
            n = i.split('**')[1]
            n = int(n)
            result.append({'koeff': koeff, 'n': n})
    return result 
# суммируем многочлены
def sum_poly(poly1, poly2):
    # ищем максим.степень в каждом многочлене
    max_n1 = max(i['n'] for i in poly1)
    max_n2 = max(i['n'] for i in poly2)
    max_n = max(max_n1, max_n2)
    print(f'Максимальная степень в многочленах:', max_n)
    # результат хранит коэффициенты нового многочлена, где индекс - степень
    result = []
    for n in range(max_n + 1):
        # коэффициент n степени для многочленов
        koeff_n1 = get_power_koeff(poly1, n)
        koeff_n2 = get_power_koeff(poly2, n)
        result.append(koeff_n1 + koeff_n2)
    return result
# поиск коэффициента для степени n (индекс - степень)
def get_power_koeff(poly, n):
    for i in poly:
        if i['n'] == n:
            return i['koeff']
    return 0
# читаем строки из файлов
def read_file(filename):
    f = open(filename, 'r')
    data = f.readline()
    f.close()
    return data
# "разбитые" формулы из файлов
poly1 = get_to_line(read_file('task4.txt'))
poly2 = get_to_line(read_file('NewFile.txt'))
# находим коэффициенты нового многочлена
new_poly = sum_poly(poly1, poly2)
koeff_p = list(reversed(new_poly))
print(f'Коэффициенты нового многочлена:', koeff_p)

# находим максимальную степень нового многочлена
n_p = 4 
# формируем новый многочлен
def make(n_p):
        result = []
        for i in range(n_p):
            if koeff_p[i] > 1:
                if n_p - i > 1:
                    result.append(f'{str(koeff_p[i])}x**{n_p - i}')
                elif n_p - i == 1:
                    result.append(f'{str(koeff_p[i])}x')
            elif koeff_p[i] == 1:
                if n_p- i > 1:
                    result.append(f'x**{n_p- i})')
                elif n_p - 1 == 1:
                    result.append('x')
        if koeff_p[-1] != 0:
                result.append(str(koeff_p[-1]))   
        return ' + '.join(result) + ' = 0' 
print(make(n_p))  

f = open('task5.txt', 'w')
f.write(make(n_p))
f.close()