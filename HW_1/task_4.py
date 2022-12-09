"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
в этой четверти (x и y).

Ввод: значение типа <int>
Вывод: значение типа <str>

Пример:

3
x < 0, y < 0
"""
a = int(input('Enter quarter number: '))

if a == 1:
    print('quarter = 1 => x∈(0, ∞) и y∈(0, ∞)')
elif a == 2:
    print('quarter = 2 => x∈(0, -∞) и y∈(0, ∞)')
elif a == 3:
    print('quarter = 3 => x∈(0, -∞) и y∈(0, -∞)')
elif a == 4:
    print('quarter = 4 => x∈(0, ∞) и y∈(0, -∞)')
else:
    print('Input Error')
    