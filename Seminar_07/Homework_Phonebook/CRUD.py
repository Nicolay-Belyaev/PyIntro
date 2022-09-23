# Задача модели - предоставить методы создания, чтения, модификации и удаление записей в базу данных (CRUD)

import sqlite3 as sql


def create(first_name, second_name, phone_number):  # TODO: переписать коннектор через with us
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


def read(key, value):
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    request = f'''
    SELECT * FROM Phonebook WHERE {key} = "{value};";
    '''
    print(cursor.execute(request).fetchall())
    connection.close()


def update(key, new_value, i):
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    request = f'''
        UPDATE Phonebook SET {key} = "{new_value}" WHERE ID = "{i};"
        '''
    cursor.execute(request).fetchall()
    connection.commit()
    connection.close()


def delete(i):
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    request = f'''
         DELETE FROM Phonebook WHERE ID = {i};
         '''
    cursor.execute(request).fetchall()
    connection.commit()
    connection.close()
