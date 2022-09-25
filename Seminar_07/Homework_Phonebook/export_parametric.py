import csv
from pathlib import Path


# функция принимает список кортежей, и построчно добавляет в текстовый файл каждый переданный контакт
def export_as_txt(contacts):
    filename = "contacts_exported.txt"
    with open(filename, 'a') as f:
        for contact in contacts:
            f.write(' '.join([str(s) for s in contact]) + '\n')


# функция принимает список кортежей, и построчно добавляет в файл csv каждый переданный контакт
# если файла csv нет, то он создается и первой строчкой записываются названия колонок
def export_as_csv(contacts):
    filename = "contacts_exported.csv"
    header = ["ID", "имя", "фамилия", "телефон"]
    my_file = Path(filename)
    if not my_file.exists():
        with open(filename, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

    with open(filename, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(contacts)
