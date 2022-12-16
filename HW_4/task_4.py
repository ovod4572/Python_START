"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""


def coeff(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def degree(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def decomp(str):
    str = str[0].replace(' ', '').split('=')
    str = str[0].split('+')
    lst = []
    l = len(str)
    k = 0
    if degree(str[-1]) == -1:
        lst.append(int(str[-1]))
        l -= 1
        k = 1
    i = 1
    index = l-1
    while index >= 0:
        if degree(str[index]) != -1 and degree(str[index]) == i:
            lst.append(coeff(str[index]))
            index -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
    return lst


def lst_new(lst1, lst2):
    ll = min(len(lst1), len(lst2))
    mm = max(len(lst1), len(lst2))
    if len(lst1) > len(lst2):
        ll = len(lst2)
    lst_new = [lst1[i] + lst2[i] for i in range(ll)]
    if len(lst1) > len(lst2):
        mm = len(lst1)
        for i in range(ll, mm):
            lst_new.append(lst1[i])
    else:
        mm = len(lst2)
        for i in range(ll, mm):
            lst_new.append(lst2[i])
    return lst_new


with open('HW_4/polynom_1.txt', 'r') as data:
    st1 = data.readlines()
with open('HW_4/polynom_2.txt', 'r') as data:
    st2 = data.readlines()
with open('HW_4/polynom_3.txt', 'r') as data:
    st3 = data.readlines()
print(st1)
print(st2)
print(st3)
lst1 = decomp(st1)
lst2 = decomp(st2)
lst3 = decomp(st3)
lst12 = lst_new(lst1, lst2)
lst_sum = lst_new(lst12, lst3)

polynom = ' + '.join([f'{(j,"")[j==1]}x^{i}' for i,
                      j in enumerate(lst_sum) if j][::-1]) + '= 0'
polynom = polynom.replace('x^1+', 'x+')
polynom = polynom.replace('x^0', '')
polynom += ('', '1')[polynom[-1] == '+']
polynom = (polynom, polynom[:-2])[polynom[-2:] == '^1']
print(polynom)
with open('HW_4/polynom_sum.txt', 'w',) as data:
    data.write(polynom)

    
