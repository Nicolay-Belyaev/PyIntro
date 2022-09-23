import CRUD
import UI
import sqlite3 as sql

# TODO подумать над механизмом возврата результатов в UI

def logic():
    UI.intro()
    command_and_param = UI.get_command_parm()

    def CRUD_request_handler():
        match command_and_param[0]:
            case "запись":
                return CRUD.create(command_and_param[1], command_and_param[2], command_and_param[3])
            case "поиск":
                return CRUD.read(command_and_param[1], command_and_param[2])
            case "изменение":
                return CRUD.update(command_and_param[1], command_and_param[2], command_and_param[3])
            case "удаление":
                return CRUD.delete(command_and_param[1])
