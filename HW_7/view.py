from logger import log


@log
def greatings():
    '''Вывод приветствия.'''

    print('Справочник')
    pass


@log
def menu() -> int:
    """
    Вывод меню, запрос данных от пользователя.
    :return:
    0 - (5 - 9) Выход
    1 - Просмотр справочника
    2 - Добавить новую запись
    3 - Редактировать запись по id
    4 - Поиск по фамилии
    """
    print('Меню')
    print(
        '0 - (5-9) Выход  \n1 - Просмотр списка абонентов \n2 - Добавить новую запись \n3 - Редактировать запись по id \n4 - Поиск по фамилии \n')
    return int(input("Введите пункт меню: "))


@log
def print_book(data: list) -> object:
    """
    Вывод в консоль данных содержимого справочника
    """
    for my_dict in data:
        print(f' {my_dict["id"]}   | {my_dict["first_name"]}     | {my_dict["last_name"]}      | '
              f' {my_dict["phone_number"]}       | {my_dict["birthday"]}  | {my_dict["workplace"]} ')
        print('_' * 82)
    if not data:
        print("<-Нет данных для отображения->")
        print()


@log
def add_record() -> dict:
    """
    Диалог добавления записи.
    :return Cловарь с данными записи.:
    """
    my_dict = {}

    my_dict['first_name'] = input('Введите имя : ')
    my_dict['last_name'] = input('Введите фамилию : ')
    my_dict['phone_number'] = input('Введите номер телефона')
    my_dict['birthday'] = input('Дата рождения: ')
    my_dict['workplace'] = input('Место работы: ')
    return my_dict


@log
def request_id() -> int:
    """
    Запрос id от пользователя
    :return id:
    """
    return int(input('Введите id: '))


@log
def editor(data: dict) -> dict:
    """
    :param data: Выбранная запись
    :return отредактированная запись:
    """
    new_dict = {}
    data['first_name'] = input(
        f"Имя: {data['first_name']}. Введите новое имя: ")

    data['last_name'] = input(
        f"Фамилия: {data['last_name']} Введите новую фамилию: ")
    data['phone_number'] = input(
        'Введите номер телефона (для выхода нажмите Enter) : ')
    data['birthday'] = input(
        f"Дата рождения: {data['birthday']} Введите новую дату: ")
    data['workplace'] = input(
        f"Место работы: {data['workplace']} Введите новое место работы: ")

    return data


@log
def request_last_name() -> str:
    """
    Запрос фамилии от пользователя
    :return фамилия:
    """
    return input('Введите Фамилию: ')


