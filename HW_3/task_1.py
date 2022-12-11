"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""
from random import randint

len_array = int(input("Enter the number: "))
numbers = []
sum_elements = 0

for i in range(len_array):
    numbers.append(randint(1, 10))
for val in numbers[1::2]:
    sum_elements += sum_elements

print(f'{numbers} -> {sum_elements}')



