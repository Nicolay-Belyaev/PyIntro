import csv
from CRUD import *
import os.path


# def import_as(choice, param_format, name_file):
options = Options()
choice = "перезаписать"
param_format = "csv"
name_file = "contacts_exported"
if (choice == "добавить") and (param_format == "csv"):
    check = os.path.isfile(f"D:/EducationalProjects/03_Python/HomeWork/PyIntro/Seminar_07/Homework_Phonebook/{name_file}.csv")
    if check:
        with open(f'D:/EducationalProjects/03_Python/HomeWork/PyIntro/Seminar_07/Homework_Phonebook/{name_file}.csv', 'r', encoding='UTF8') as file:
            y = csv.reader(file, delimiter=";")
            data = [row for row in y]
            for i in range(1, len(data)):
                num = data[i][0].split(',')
                options.create(num[1], num[2], num[3])
    else:
        print("Неправильно указано имя файла или адресс")
elif (choice == "перезаписать") and (param_format == "csv"):
    options.delete_all()
    check = os.path.isfile(
            f"D:/EducationalProjects/03_Python/HomeWork/PyIntro/Seminar_07/Homework_Phonebook/{name_file}.csv")
    if check:
        with open(
                    f'D:/EducationalProjects/03_Python/HomeWork/PyIntro/Seminar_07/Homework_Phonebook/{name_file}.csv',
                    'r', encoding='UTF8') as file:
            y = csv.reader(file, delimiter=";")
            data = [row for row in y]
            for i in range(1, len(data)):
                num = data[i][0].split(',')
                options.create(num[1], num[2], num[3])


