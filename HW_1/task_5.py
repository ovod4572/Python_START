"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Результат округлить до сотых.

Ввод: четыре значения типа <int>
Вывод: значение типа <float>

Пример:

4 10
11 5
9.22
"""
ax = int(input('Enter point coordinate A along the X axis: '))
ay = int(input('Enter point coordinate A along the Y axis: '))
bx = int(input('Enter point coordinate B along the X axis: '))
by = int(input('Enter point coordinate B along the Y axis: '))

import math
distans = round(math.sqrt((ax-bx)**2+(ay-by)**2), 2)
print(f'A({ax},{ay}); B({bx},{by}) -> {distans}')

