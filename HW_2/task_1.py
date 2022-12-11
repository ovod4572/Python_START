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
number = float(input('Enter the number: '))  
sum = []
x = abs(number)
sum = 0

for i in str(x):
    if i != '.': 
        sum += int(i)
    
print(sum) 
