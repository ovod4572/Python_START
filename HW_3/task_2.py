"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[2, 3, 4, 5, 6]
[12, 15, 16]

[2, 3, 5, 6]
[12, 15]
"""
from random import randint

len_array = int(input("Enter the number: "))
numbers = []
#new_numbers = []

for i in range(len_array):
    numbers.append(randint(1, 10))
print(numbers)   

# if len_array % 2 == 0:
#     for i in range(int(len_array / 2)):
#         new_numbers.append(numbers[i] * numbers[-i - 1])
# else:
#     for i in range(int(len_array / 2 + 1)):
#         new_numbers.append(numbers[i] * numbers[-i - 1])

# print(new_numbers)
print([numbers[i] * numbers[-i - 1] for i in range((len_array + 1) // 2)])


