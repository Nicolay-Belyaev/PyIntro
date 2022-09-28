import csv
from CRUD import *
import os.path
from pathlib import Path

def path_generator(path, filename):
    path: Path = Path(path)
    filename: Path = Path(filename)
    return path / filename

def import_as(rewrite: bool, file_path, file_name: str):
    """ """
    options = Options()

    if rewrite:
        options.delete_all()

    file_name_split = file_name.split('.')
    match file_name_split[1]:
        case 'csv':
            with open(f'{path_generator(file_path, file_name)}', 'r') as target:





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
            print("Неправильно указано имя файла или адрес")
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


