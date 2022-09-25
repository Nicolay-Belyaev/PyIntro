# Задача модели - предоставить методы создания, чтения, модификации и удаление записей в базу данных (CRUD)

import sqlite3 as sql
import export_parametric

# TODO: обернуть функции в класс, вынести словарь для read и update в __поля класса__(?);
# TODO: переписать коннекторы через with as;
# TODO: модифицировать возвраты функций что бы они более информативны (например, create возвращает созданную запись);
# TODO: запилить функции импорта/экспорта из SQL в JSON, TXT и во что угодно еще;
# TODO: модифицировать функцию поиска на: "пустые параметры -> возврат всех записей __построчно__(!)";
# TODO: зациклить основную логику что бы программа после выполнения 1 запроса возвращалась на принятие следующего.
# TODO: подумать над обработкой исключений (разделить логику функций на подключение и работу и обложить try-excet'ами(?))


def create(first_name, second_name, phone_number):
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    request = f'''
    INSERT INTO Phonebook 
        (FirstName, SecondName, Phonenumber) 
    VALUES 
        ("{first_name}", "{second_name}", "{phone_number}");
    '''
    cursor.execute(request).fetchall()
    connection.commit()
    return str('Запись произведена')


def read(key, value):
    keys_dict = {
        'ID': 'ID',
        'ИМЯ': 'FirstName',
        'ФАМИЛИЯ': 'SecondName',
        'ТЕЛЕФОН': 'Phonenumber'
    }
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    request = f'''
    SELECT * FROM Phonebook WHERE {keys_dict.get(key)} = "{value}";'''
    result = (cursor.execute(request).fetchall())
    connection.close()

    export_parametric.export_as_txt(result)
    export_parametric.export_as_csv(result)
    return result


def update(key, new_value, i):
    keys_dict = {
        'ID': 'ID',
        'ИМЯ': 'FirstName',
        'ФАМИЛИЯ': 'SecondName',
        'ТЕЛЕФОН': 'Phonenumber'
    }
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    request = f'''
        UPDATE Phonebook SET {keys_dict.get(key)} = "{new_value}" WHERE ID = "{i}";
        '''
    cursor.execute(request).fetchall()
    connection.commit()
    connection.close()
    return str(f'В запись с ID {i} внесены изменения. Новое значение поля {key} = {new_value}.')


def delete(i):
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    request = f'''
         DELETE FROM Phonebook WHERE ID = {i};
         '''
    cursor.execute(request).fetchall()
    connection.commit()
    connection.close()
    return str(f'Запись с ID {i} удалена.')
