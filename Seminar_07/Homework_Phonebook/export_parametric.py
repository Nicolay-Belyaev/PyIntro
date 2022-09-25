import csv
import sqlite3 as sql


# функция принимает необходимый формат и в зависимости от параметра
# создает файл в определенном формате
def export_as(required_format):
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    request = f'''
    SELECT * FROM Phonebook'''
    result = (cursor.execute(request).fetchall())
    connection.close()

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
    return f"Экспортировал в {filename}"
