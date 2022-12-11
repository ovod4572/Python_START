"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
from random import uniform

len_array = int(input("Введите количество чисел в списке: "))
sign = int(input("Введите количество знаков после запятой: "))
float_numbers = []

for i in range(len_array):
    float_numbers.append(round(uniform(1, 10), sign))   
print(float_numbers)

for i in range(len_array):
    float_numbers[i] = float_numbers[i] - int(float_numbers[i])
float_numbers.sort()
dif_numbers = float_numbers[-1] - float_numbers[0]
print(f' => {round(dif_numbers, sign)}')