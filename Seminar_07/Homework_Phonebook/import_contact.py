import csv
from CRUD import *
from pathlib import Path


def path_generator(path, filename):
    path: Path = Path(path)
    filename: Path = Path(filename)
    return path / filename


def import_as(rewrite: bool, full_path: str):
    """Импортирует в БД из TXT или CSV (структура файла должна быть аналогичной структуре файла экспорта модуля export)
    Принимает параметры:
    rewrite (True - удаляет все записи из БД и пишет новые данные из файла, False - дописывает данные из файла).
    file_path - путь до каталога с файлом из ОС,
    full_file_name - имя с файлом с расширением (вид file.csv или file.txt)"""

    options = Options()  # нужная для функции create и delete_all

    if rewrite:
        options.delete_all()

    _, extension = full_path.split('.')
    match extension:
        case 'csv':
            with open(full_path, 'r', encoding='UTF16') as target:
                reader = csv.reader(target, delimiter=";")
                string = [row for row in reader]
                for i in range(1, len(string)):
                    params = string[i][0].split(',')
                    options.create(params[1], params[2], params[3])
        case 'txt':
            with open(full_path, 'r') as target:
                reader = target.read()
                listed = [reader]
                listed = listed[0].split('\n')
                for i in range(len(listed)):
                    listed[i] = listed[i].split()
                for i in range(len(listed)):
                    if len(listed[i]) == 4:
                        options.create(listed[i][1], listed[i][2], listed[i][3])
    return ['Импорт произведен.']

