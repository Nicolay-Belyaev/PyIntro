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
import tkinter

#
from CRUD import *
import UI as ui
from GUI_MainWindow import MainWindow
import export as exp
import import_contact as imp


def ui_request_handler(command_and_param=None):
    """
    функция принимает аргументы от пользователя в виде списка [команда, параметры...],
    далее пробрасывает параметры в соответствующие функции.
    функции возвращают коллекцию-отчет, который затем передается в ui и далее в консоль.
    """

    # command_and_param будет None если мы работаем с консолью
    if command_and_param is None:
        command_and_param = ui.get_command_parm()
    crud = Options()
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
            return exp.export_as(command_and_param[1], command_and_param[2])
        case "импорт":
            return imp.import_as(command_and_param[1], command_and_param[2])
        case "выход":
            exit()


def logic_using_gui():
    win = MainWindow()  # создаем объект класса Окно
    win.draw_window()  # рисуем инициализирующее первое окно с приветствием и меню

    while win.window.state() == "normal":
        win.set_loop()  # позволяет не закрывать программу после сделанной операции
        l = win.get_current_command()  # получает список [операции, *параметров...]
        request_result = ui_request_handler(l if len(l) else ["выход"])  # передает список дальше в handler
        ui.request_explorer(request_result)


def logic_using_console():
    ui.intro()
    while True:
        request_result = ui_request_handler()
        ui.request_explorer(request_result)
