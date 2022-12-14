"""
Написать программу по переводу целого числа из десятичной системы счисления в двоичную.

Ввод: значение типа <int>
Вывод: значение типа <int>

Примеры:
45
101101

3
11

2
10
"""

def binary(number):
    if number == 1:
        return 1

#    return f'{binary(number // 2)}{number % 2}'       
    return number % 2 + 10 * binary(number // 2)

number = int(input("Enter the number: "))
print(binary(number))


