import csv
import sqlite3 as sql


def export_as(extension, filepath):
    """
    Функция принимает от пользователя формат файла (csv/txt) и экспортирует весь справочник в заданный формат.
    """
    with sql.connect('database.db') as connection:
        cursor = connection.cursor()
        request = f'''
        SELECT * FROM Phonebook'''
        result = (cursor.execute(request).fetchall())

    filepath += '.' + extension
    with open(filepath, 'w', encoding='UTF16', newline='') as f:
        match extension:
            case "txt":
                for row in result:
                    f.write(' '.join([str(s) for s in row]) + '\n')
            case "csv":
                header = ["ID", "имя", "фамилия", "телефон"]
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(result)
    return [f"Экспортировал в {filepath}"]
