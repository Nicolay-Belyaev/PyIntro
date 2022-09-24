# задача UI (user interface) - принять от пользователя запрос с параметрами для работы со справочником,
# передать его через контроллер в модель и получить от контроллера результаты обработки запроса.

def intro():
    username = input('Привет, пользователь. Введи свое имя: ')
    print(f'Приятно познакомиться, {username}!\n Ты пользуешься  консольным телефонным справочником.\n')


def get_command_parm():
    print('Сейчас в справочнике доступны 4 действия: "запись", "поиск", "изменение" и "удаление".\n')
    command = ''
    while command not in ["запись", "чтение", "поиск", "удаление"]:
        command = input("Введи действие, которое хочешь совершить: ").lower()
        match command:
            case "запись":
                param_first_name = input('Введи имя: ').capitalize()
                param_second_name = input('Введи фамилию: ').capitalize()
                param_phone_number = input('Введи номер телефона: ')
                return [command, param_first_name, param_second_name, param_phone_number]
            case "поиск":
                print('Для вывода всех записей справочника, оставь поля запроса пустыми\n')
                # TODO сделать что б работало
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
            case _:
                print('Извини, ты или опечатался, или я пока не знаю такой команды. Попробуй еще раз.\n')


def request_explorer(result):
    print(result)
