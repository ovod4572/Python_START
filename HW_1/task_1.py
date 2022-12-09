"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.

Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)

Пример:
6
True

7
True

1
False
"""
number = int(input("Enter the number of the day of the week from 1 to 7: "))

if number < 1 or number > 7:
    print('Input Error')
elif number > 5:
    print('True')
else:
    print('False')