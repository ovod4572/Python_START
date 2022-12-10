"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""

from random import randint

num = int(input('Enter the number: '))
new_list = [randint(-num, num) for r in range(num)]
index_list = []
prod = 1
data = open('indexes.txt', 'r')
for index in data:
    index_list.append(int(index))
for i in range(-num, num):
    if i in index_list:
        prod *= new_list[i]
print(prod)
