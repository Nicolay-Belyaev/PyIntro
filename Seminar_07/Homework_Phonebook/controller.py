"""
У контроллера следующие задачи:
0. Вывести приветственное сообщение (ui.intro)
1. С помощью функции интерфейса ui.get_command_parm получить от пользователя команду и её параметры.
2. Выбрать, какая функция из модели (CRUD) должна быть вызвана. Для этого используется первый элемент
списка command_and_param, содержащий название команды пользователя. В зависимости от команды, подставить
в вызываемую из CRUD функцию параметры (элементы списка command_and_param со второго до последнего).
Эту механику реализует функция ui_request_handler.
3. Вернуть результаты работы функции из CRUD пользователю с помощью функции ui.request_explorer
"""
#
from CRUD import *
import UI as ui
import export as exp
import import_contact as imp


def ui_request_handler():
    """
    функция принимает аргументы от пользователя в виде списка [команда, параметры...],
    далее пробрасывает параметры в соответствующие функции.
    функции возвращают коллекцию-отчет, который затем передается в ui и далее в консоль.
    """
    command_and_param = ui.get_command_parm()
    options = Options()
    match command_and_param[0]:
        case "запись":
            return options.create(command_and_param[1], command_and_param[2], command_and_param[3])
        case "поиск":
            return options.read(command_and_param[1], command_and_param[2])
        case "изменение":
            return options.update(command_and_param[1], command_and_param[2], command_and_param[3])
        case "удаление":
            return options.delete(command_and_param[1])
        case "экспорт":
            return exp.export_as(command_and_param[1])
        case "импорт":
            return imp.import_as(command_and_param[1], command_and_param[2], command_and_param[3])
        case "выход":
            exit()


def logic():
    ui.intro()
    while True:
        request_result = ui_request_handler()
        ui.request_explorer(request_result)
