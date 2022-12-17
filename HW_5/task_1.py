"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""

#arg = input("Enter text separated by a space:\n")
arg = "автобус генерал швабра итог арбуз вагон"
print(arg)


def new_text(arg):
    arg = list(filter(lambda x: "а" and "б" and "в" not in x, arg.split()))
    return " ".join(arg)

result = new_text(arg)
print(result)


# new_text = [i for i in arg.split() if not ("а" in i and "б" in i and "в" in i)]
# print(" ".join(new_text))


# text = arg.split()
# new_text = []

# for i in text:
#     if not ("а" in i and "б" in i and "в" in i):
#         new_text.append(i)

# result = ' '.join(new_text) 
# print(result)

