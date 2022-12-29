"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""

# str = '(2 * (1 + 3) - 1) - (5 / 2)'
# print(eval(str))


action_dict = {'/': lambda a, b: str(int(a) / int(b)),
               '*': lambda a, b: str(int(a) * int(b)),
               '+': lambda a, b: str(int(a) + int(b)),
               '-': lambda a, b: str(int(a) - int(b))
               }


def parse_exp(exp: str):
    if len(exp) == 1:
        return float(exp)
    if not exp:
        return 0
    if '(' in exp:
        return brackets_sum(exp)
    print(exp)
    symbols = '-+*/'
    for symbol in symbols:
        if symbol in exp:
            a, b = exp.split(symbol, 1)
            return action_dict[symbol](parse_exp(a), parse_exp(b))


def find_bracket(data: str):
    bracket_start = 0
    bracket_end = 0
    for i, sym in enumerate(data):
        if sym == "(":
            bracket_start = i
        elif sym == ")":
            bracket_end = i
            return bracket_start, bracket_end
    return bracket_start, bracket_end


def brackets_sum(exp: str):
    if '(' in exp:
        print(exp)
        bracket_start, brascket_end = find_bracket(exp)
        exp = exp[0:bracket_start] + \
            parse_exp(exp[bracket_start + 1:brascket_end]) + \
            exp[brascket_end + 1:]
    return parse_exp(exp)


def start(exp: str):
    return parse_exp(''.join(exp.split()))


if __name__ == '__main__':

    exp = '(2 * (1 + 3) - 1) * (5 - 2)'
    print(start(exp))



    
