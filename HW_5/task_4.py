"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
"""
#arg = input()
arg = 'ыыыыыррррр   аааааагггггггг'
conut = 1
for i in range(len(arg)):
    if i == (len(arg) - 1):
        print(str(conut) + arg[i], end='')
    else:
        if arg[i] == arg[i + 1]:
            conut = conut + 1
        else:
            print(str(conut) + arg[i], end='')
            conut = 1
print()

#expect = input()
expect = '5ы5р3 6а8г'
for i in range(len(expect)):
    if expect[i].isdigit():
        for j in range(int(expect[i]) - 1):
            print(expect[i + 1], end='')
    else:
        print(expect[i], end='')
print()

