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

import CRUD as crud
import UI as ui
import export_parametric as exp


def logic():
    def ui_request_handler():
        command_and_param = ui.get_command_parm()
        match command_and_param[0]:
            case "запись":
                return crud.create(command_and_param[1], command_and_param[2], command_and_param[3])
            case "поиск":
                return crud.read(command_and_param[1], command_and_param[2])
            case "изменение":
                return crud.update(command_and_param[1], command_and_param[2], command_and_param[3])
            case "удаление":
                return crud.delete(command_and_param[1])
            case "экспорт":
                return exp.export_as(command_and_param[1])
            case "выход":
                exit()

    ui.intro()
    while True:
        request_result = ui_request_handler()
        ui.request_explorer(request_result)

