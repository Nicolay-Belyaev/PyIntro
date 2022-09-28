import csv
from CRUD import *
import os.path


def import_as(choice, param_format, name_file):
    if (choice == "добавить"):
        check = os.path.isfile(f"D:/EducationalProjects/03_Python/HomeWork/PyIntro/Seminar_07/Homework_Phonebook/{name_file}.{param_format}")
        if check:
            entry(name_file, param_format)
        else:
            print("Неправильно указано имя файла")
    elif (choice == "перезаписать"):
        options = Options()
        options.delete_all()
        check = os.path.isfile(
                f"D:/EducationalProjects/03_Python/HomeWork/PyIntro/Seminar_07/Homework_Phonebook/{name_file}.{param_format}")
        if check:
            entry(name_file, param_format)
        else:
            print("Неправильно указано имя файла")
    return [f"Импортировал из {name_file}"]

def entry(name_file, param_format):
    options = Options()
    with open(f'D:/EducationalProjects/03_Python/HomeWork/PyIntro/Seminar_07/Homework_Phonebook/{name_file}.{param_format}', 'r',
              encoding='UTF8') as file:
        if param_format == "csv":
            y = csv.reader(file, delimiter=";")
            data = [row for row in y]
            for i in range(1, len(data)):
                num = data[i][0].split(',')
                options.create(num[1], num[2], num[3])
        elif param_format == "txt":
            y = file.read()
            num = [y]
            num = num[0].split('\n')
            for i in range(len(num)):
                num[i] = num[i].split()
            print(num)
            for i in range(len(num)):
                if len(num[i]) == 4:
                    options.create(num[i][1], num[i][2], num[i][3])



