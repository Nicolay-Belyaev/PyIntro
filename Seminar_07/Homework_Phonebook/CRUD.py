# Задача модели - предоставить методы создания, чтения, модификации и удаление записей в базу данных (CRUD)

import sqlite3 as sql
# TODO: модифицировать возвраты функций что бы они более информативны (например, create возвращает созданную запись);
# TODO: подумать над обработкой исключений (разделить логику функций на подключение и работу и обложить try-excet'ами(?))


class Options(object):

    keys_dict = {
        'ID': 'ID',
        'ИМЯ': 'FirstName',
        'ФАМИЛИЯ': 'SecondName',
        'ТЕЛЕФОН': 'Phonenumber'
    }

    def create(self, first_name, second_name, phone_number):
        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
            INSERT INTO Phonebook 
                (FirstName, SecondName, Phonenumber) 
            VALUES 
                ("{first_name}", "{second_name}", "{phone_number}");
            '''
            cursor.execute(request).fetchall()
            return [str('Запись произведена')]

    def read(self, key, value):
        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
            SELECT * FROM Phonebook WHERE {Options.keys_dict.get(key)} = "{value}";'''
            if (key == '') and (value == ''):
                request = 'SELECT * FROM Phonebook'
            result = (cursor.execute(request).fetchall())
            return result

    def update(self, key, new_value, i):
        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
                UPDATE Phonebook SET {Options.keys_dict.get(key)} = "{new_value}" WHERE ID = "{i}";
                '''
            cursor.execute(request).fetchall()
            connection.commit()
            return [str(f'В запись с ID {i} внесены изменения. Новое значение поля {key} = {new_value}.')]

    def delete(self, i):
        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
                 DELETE FROM Phonebook WHERE ID = {i};
                 '''
            cursor.execute(request).fetchall()
            connection.commit()
            return [str(f'Запись с ID {i} удалена.')]
