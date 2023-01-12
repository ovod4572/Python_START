import model
import view
from logger import log


@log
def start():
    """Стартовая функция"""
    view.greatings()
    button = view.menu()

    if button == 1:
        view.print_book(model.get_data())
        start()
    elif button == 2:
        model.add_data(view.add_record())
        start()
    elif button == 3:
        model.add_data(view.editor(model.get_data_id(view.request_id())))
        start()
    elif button == 4:
        view.print_book(model.get_data_last_name(view.request_last_name()))
        start()
    else:
        print('Работа окончена')
        exit
        print()

        
