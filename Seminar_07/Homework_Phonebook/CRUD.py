# Задача модели - предоставить методы создания, чтения, модификации и удаление записей в базу данных (CRUD)

import sqlite3 as sql

# TODO: сделать всем функция реторны, что бы они отдавали в контроллер результат своей работы, а тот,
# TODO: в свою очередь, передавал их в UI. +


def create(first_name, second_name, phone_number):  # TODO: переписать коннектор через with as
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
    # TODO вынести в поля класса (?) и дать доступ всем нуждающимся функциям
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
    return result


def update(key, new_value, i):
    # TODO вынести в поля класса (?) и дать доступ всем нуждающимся функциям
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
