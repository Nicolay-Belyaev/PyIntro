# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

array_of_strings = ["йцу", "фыв", "ячс", "цук", "йцукен"]
search = input('Введите строку: ')

if array_of_strings.count(search) >= 2:
    print(array_of_strings.index(search, 1))
else:
    print('Её нет')
