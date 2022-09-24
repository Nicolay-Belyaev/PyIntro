import CRUD as crud
import UI as interface
import sqlite3 as sql

# TODO подумать над механизмом возврата результатов в UI


def logic():
    def ui_request_handler():
        command_and_param = interface.get_command_parm()
        match command_and_param[0]:
            case "запись":
                return crud.create(command_and_param[1], command_and_param[2], command_and_param[3])
            case "поиск":
                return crud.read(command_and_param[1], command_and_param[2])
            case "изменение":
                return crud.update(command_and_param[1], command_and_param[2], command_and_param[3])
            case "удаление":
                return crud.delete(command_and_param[1])

    interface.intro()
    request_result = ui_request_handler()
    interface.request_explorer(request_result)
