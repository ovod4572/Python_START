"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


# def fib(n):
#     if n < 0:
#         return (-1) ** (-n + 1) * fib(-n)

#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)

fib = lambda n: 1 if n in (1, 2) else (-1) ** (-n + 1) * fib(-n) if n < 0 else fib(n - 1) + fib(n - 2)
N = int(input("Enter the number N: "))
neg_fib = []

for i in range(-N, N + 1):
    neg_fib.append(fib(i))

print(neg_fib)

