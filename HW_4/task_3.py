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

k = int(input('Введите натуральную степень k: '))
ratios = [randint(0, 100) for i in range(k)] + [randint(1, 100)]
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
with open('task_4.txt', 'w') as data:
    data.write(polinom)
    
