"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""

number = int(input("Enter the number: "))
i = 2
simpie_multiplier = []
while i <= number:
    if number % i == 0:
        simpie_multiplier.append(i)
        number //= i
    else:
        i += 1
print(simpie_multiplier)
