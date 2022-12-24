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
#enc = input()
enc = 'ыыыыыррррр   аааааагггггггг'
conut = 1
for i in range(len(enc)):
    if i == (len(enc) - 1):
        print(str(conut) + enc[i], end='')
    else:
        if enc[i] == enc[i + 1]:
            conut = conut + 1
        else:
            print(str(conut) + enc[i], end='')
            conut = 1
print()

#dec = input()
dec = '5ы5р3 6а8г'
for i in range(len(dec)):
    if dec[i].isdigit():
        for j in range(int(dec[i]) - 1):
            print(dec[i + 1], end='')
    else:
        print(dec[i], end='')
print()

