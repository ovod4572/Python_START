"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""
number = input ('Enter the number: ')
def summa(x):                            
    x = abs(float(x))
    sum = 0

    for i in str(x):
        if i is not '.':  # !=
            sum = sum + int(i)
    return sum
print ( f'{number} -> {summa(number)}')  
    
