'''
Задача модели - предоставить методы создания, чтения, модификации и удаление записей в базу данных (CRUD).
Все функции возвращают коллекцию для корректной работы функции UI.request_explorer().
'''

import sqlite3 as sql
# TODO: исключения!
# Основная задача - обработать возможные исключения, там где они могу быть.
# Особое внимание работе с БД пользовательскому вводу


class Options(object):
    # словарь используют функции read и update для перевода пользовательского ввода названий полей в понятный SQL
    keys_dict = {
        'ID': 'ID',
        'ИМЯ': 'FirstName',
        'ФАМИЛИЯ': 'SecondName',
        'ТЕЛЕФОН': 'Phonenumber'
    }

    def create(self, first_name, second_name, phone_number):
        """Создает в БД новую запись с параметрами first_name = имя, second_name = фамилия, phone_number - телефон"""
        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
            INSERT INTO Phonebook 
                (FirstName, SecondName, Phonenumber) 
            VALUES 
                ("{first_name}", "{second_name}", "{phone_number}");
            '''
            cursor.execute(request).fetchall()
            return [str(f'Произведена запись {first_name} {second_name} {phone_number}')]


    def read(self, key, value):
        """Поиск по БД по 1 параметру. Если оставить пару ключ-значение пустой ('') - вернет все записи БД"""
        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
            SELECT * FROM Phonebook WHERE {Options.keys_dict.get(key)} = "{value}";'''
            if (key == '') and (value == ''):
                request = 'SELECT * FROM Phonebook'
            result = (cursor.execute(request).fetchall())
            return result

    def update(self, key, new_value, i):
        """Изменяет 1 поле 1 записи за один вызов функции"""
        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
                UPDATE Phonebook SET {Options.keys_dict.get(key)} = "{new_value}" WHERE ID = "{i}";
                '''
            cursor.execute(request).fetchall()
            connection.commit()
            return [str(f'В запись с ID {i} внесены изменения. Новое значение поля {key} = {new_value}.')]

    def delete(self, i):
        """Удаляет запись из БД по ID. Не приводит к пересчету поля 'ID' в БД (остальные записи сохраняют свои ID)"""
        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
                 DELETE FROM Phonebook WHERE ID = {i};
                 '''
            cursor.execute(request).fetchall()
            connection.commit()
            return [str(f'Запись с ID {i} удалена.')]

    def delete_all(self):
        """Удаляет данный БД. (чистый лист)"""

        with sql.connect('database.db') as connection:
            cursor = connection.cursor()
            request = f'''
                 DELETE FROM Phonebook
                 '''
            cursor.execute(request).fetchall()
            connection.commit()
            return [str('Телефонный справочник очищен.')]
