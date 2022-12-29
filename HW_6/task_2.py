"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
lst = [1, 2, 3, 5, 1, 5, 3, 10]
#lst = list(map(int, input("Enter numbers separated by spaces:\n").split()))
print(lst)

new_lst_1 = [i for i in set(lst) if lst.count(i) == 1]
new_lst_2 = [i for i in set(lst) if lst.count(i) > 1]
new_lst_3 = [i for i in set(lst) if lst.count(i)]

print(new_lst_1)
print(new_lst_2)
print(new_lst_3)


