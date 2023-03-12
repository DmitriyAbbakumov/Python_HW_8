import chek



def start():
    greetings = 'Привет! Это твоя телефонная книга. Давай расскажу что я умею\nМы можем создать новый контакт, найти его, изменить или удалить,\nа также показать все контакты.'

    print(f'{greetings}\n')


def menu():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    new_book = '0. Создать новую книгу или очистить существующую'
    new_contact = '1. Добавить новый контакт'
    change_number = '2. Изменить номер телефона'
    change_surname = '3. Изменить фамилию'
    delete_contact = '4. Удалить контакт'
    view_all_contact = '5. Показать все контакты'
    to_exit = '7. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{new_contact}\n{change_number}\n{change_surname}\n{delete_contact}\n{view_all_contact}\n{to_exit}')
    return chek.digit_check()