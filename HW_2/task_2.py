"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""
number = int(input("Enter the number: "))
i = 1
num = 1
x = []
while i <= number:
    num = num * i
    i = i + 1
    x.append(num)
print(x)
