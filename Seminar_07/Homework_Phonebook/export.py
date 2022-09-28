import csv
import sqlite3 as sql


def export_as(required_format):
    """
    Функция принимает от пользователя формат файла и экспортирует весь справочник в заданный формат.
    """
    with sql.connect('database.db') as connection:
        cursor = connection.cursor()
        request = f'''
        SELECT * FROM Phonebook'''
        result = (cursor.execute(request).fetchall())

    filename = "contacts_exported"
    match required_format:
        case "txt":
            filename += ".txt"
            with open(filename, 'w') as f:
                for row in result:
                    f.write(' '.join([str(s) for s in row]) + '\n')
        case "csv":
            filename += ".csv"
            header = ["ID", "имя", "фамилия", "телефон"]
            with open(filename, 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(result)
    return [f"Экспортировал в {filename}"]
