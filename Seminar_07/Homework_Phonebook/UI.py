"""
Задача UI (user interface) - принять от пользователя запрос с параметрами для работы со справочником,
передать его через контроллер в модель и получить от контроллера результаты обработки запроса.
"""


def intro():
    """ Выводит приветственное сообщение"""
    username = input('Привет, пользователь. Введи свое имя: ')
    print(f'''
    Приятно познакомиться, {username}!\n 
    Ты пользуешься  консольным телефонным справочником.\n
    Сейчас в справочнике доступны 5 действий: "запись", "поиск", "изменение", "удаление" и "экспорт", а также команда "выход".\n
    ''')


def get_command_parm():
    """Принимает у пользователя команду и параметры. Возвращает список ['команда', 'параметр_х', 'параметр_y', ...]"""
    command = input("Введи действие, которое хочешь совершить: ").lower()


    while command not in ["запись", "чтение", "поиск", "удаление", "экспорт", "выход"]:
        print('Извини, ты или опечатался, или я пока не знаю такой команды. Попробуй еще раз.\n')

        command = input("Введи действие, которое хочешь совершить: ").lower()

    match command:
        case "запись":
            param_first_name = input('Введи имя: ').capitalize()
            param_second_name = input('Введи фамилию: ').capitalize()
            param_phone_number = input('Введи номер телефона: ')
            return [command, param_first_name, param_second_name, param_phone_number]
        case "поиск":
            print('Для вывода всех записей справочника, оставь поля запроса пустыми\n')
            param_key = input('Введи 1 поле для поиска (ID/имя/фамилия/телефон): ').upper()
            param_value = input('Введи искомое значение: ')
            return [command, param_key, param_value]
        case "изменение":
            param_id = input('Укажи ID записи для изменения: ')
            param_key = input('Введи 1 поле для изменения (ID/имя/фамилия/телефон): ').upper()
            param_new_value = input('Введи новое значение этого поля: ')
            return [command, param_key, param_new_value, param_id]
        case "удаление":
            param_id = input('Укажи ID записи для удаления: ')
            return [command, param_id]
        case "экспорт":
            param_format = input("Во что сохранить? (txt/csv): ").lower()
            while param_format not in ["txt", "csv"]:
                param_format = input("Неверный ввод: (txt или csv): ").lower()
            return [command, param_format]
        case "выход":
            print('Еще увидимся!\n')
            return ["выход"]


def request_explorer(result):
    """Выводит результат работы одной из CRUD-функций"""
    print(result)

