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
n = int(input("Enter the number N: "))
def fib(n):
    a, b = 0, 1
    result = [0]
    for i in range(n):
        a, b = b, a + b
        result.append(a)
        result.insert(i, a*(-1))
        result.sort()
    return result
print(fib(n))

