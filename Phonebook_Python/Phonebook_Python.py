phone_book = {}
path: str = 'phone.txt'
def open_file():
    phone_book.clear()
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        file.close()
        for contact in data:
            nc = contact.strip().split(':')
            phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
        print('\nТелефонная книга успешно загружена!')

def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print('\nТелефонная книга успешно сохранена!')
    print('=' * 200 + '\n')

def show_contacts(book: dict[int,dict]):
    print('\n' + '=' * 200)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 200 + '\n')

def add_contact():
    uid = max(phone_book.keys()) + 1
    while True:
        name = input('Введите имя контакта: ')
        if name.strip() != '':
            break
        print('Имя не может быть пустым, попробуйте еще раз.')
    while True:
        phone = input('Введите телефон контакта: ')
        if phone.strip() != '':
            break
        print('Телефон не может быть пустым, попробуйте еще раз.')
    comment = input('Введите комментарий контакта: ')
    phone_book[uid] = {'name': name, 'phone' : phone, 'comment' : comment}
    print(f'\nКонтакт {name} успешно добавлен в книгу!')
    print('=' * 200 + '\n')

def search():
    result = {}
    word = input('Введите слово по которому будет выполняться поиск: ')
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
              result[i] = contact
    return result

def change_contact(book: dict[int,dict]):
    print('\n' + '=' * 200)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 200 + '\n')
    f_name = input("Введите имя контакта который хотите изменить: ")
    if f_name in [x['name'] for x in phone_book.values()]:
        for key, value in phone_book.items():
            if value['name'] == f_name:
                new_name = input('Введите имя контакта: ')
                phone = input('Введите телефон контакта: ')
                comment = input('Введите комментарий контакта: ')
                phone_book[key] = {'name': new_name, 'phone': phone, 'comment': comment}
                print("Контакт изменен.")
                break
    else:
        print("Контакт не найден.")

def remove():
    while True:
        result = search()
        if result:
            show_contacts(result)
            index = int(input('Введите ID контакта, который хотите удалить: '))
            del_cnt = phone_book.pop(index)
            print(f'\nКонтакт {del_cnt.get("name")} успешно удален из книги!')
            print('=' * 200 + '\n')
            break
        else:
            print('Контакт не найден. Попробуйте еще раз.')

def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Ошибка ввода, введите ЧИСЛО от 1 до 8')

open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contacts(result)
        case 6:
            change_contact(phone_book)
        case 7:
            remove()
        case 8:
            print('До свидания! Хорошего вам дня!')
            break