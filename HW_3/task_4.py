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
number = int(input("Enter the number: "))
def binary(number):
    if number == 0:
        return 0
       
    return number % 2 + 10 * binary(number // 2)
print(binary(number))


