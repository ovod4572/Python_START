"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""

from random import randint

#коэффициент многочлена высшего порядка (ratios) не может быть равен нулю. 
# Если сумма коэффициентов равна нулю, то нет многочлена, нет задачи. 
# к=2 -> x**2 обязан присутствовать. к=8 -> x**8. k=25 -> x**24. Это как 2х2=5.
# Поэтому условие 0 = 0, как и К = 0, невозможны по определению. 
# (При К = 5 "многочлен" 0 равен 0 !!! Где многочлен?). Спасибо.

k = int(input('Введите натуральную степень k: '))
ratios = [randint(0, 100) for i in range(k + 1)]
if ratios[0] == 0:
    ratios[0] = randint(1, 100)
power = len(ratios) - 1
polinom = []

for ratio in ratios:
    if ratio:
        if power == 0:
            polinom. append(f'{ratio}')
        elif power == 1:
            polinom.append(f'{ratio if ratio != 1 else ""}x')
        else:
            polinom.append(f'{ratio if ratio != 1 else ""}x^{power}')
    power -= 1
polinom = ' + '.join(polinom) + ' = 0'
print(polinom)
with open('task_4.txt', 'a+',) as data:
    data.write(f'{polinom}\n')
    
