# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# читаем файл, пишем в переменную и делаем предварительную подготовку (режем и разворачиваем)
def file_reader(file_name: str):
    file = open(f'{file_name}', 'r')
    poly = file.read()
    splitted_poly = poly.split(' + ')
    splitted_poly.reverse()
    return splitted_poly


def poly_adder(poly1, poly2):
    prep_array = []
    counter = min(len(poly1), len(poly2))
    
    # складываем (из строки в инт и обратно) переменные и собираем в предварительный список
    for i in range(counter):
        if i == 0:
            res_variable = f'{(int(poly1[i][:poly1[i].index(" ")]) + int(poly2[i][:poly1[i].index(" ")]))}'
        elif i == 1:
            res_variable = f'{str(int(poly1[i][:poly1[i].index("x")]) + int(poly2[i][:poly2[i].index("x")]))}x'
        else:
            res_variable = f'{str(int(poly1[i][:poly1[i].index("x")]) + int(poly2[i][:poly2[i].index("x")]))}x^{i}'
        prep_array.append(res_variable)
    # если один многочлен длиннее другого, дополняем итоговый многочлен старшими одночленами большего многочлена
    if len(poly1) != len(poly2):
        if len(poly1) > len(poly2):
            longer_poly = poly1
        else:
            longer_poly = poly2
        len_diff = max(len(poly1), len(poly2))
        for i in range(counter, len_diff):
            prep_array.append(longer_poly[i])
    # разворачиваем и собираем итоговую строку
    prep_array.reverse()
    joined_res_str = " + ".join(prep_array) + ' = 0'
    return joined_res_str


poly1 = file_reader('1.txt')
poly2 = file_reader('2.txt')
result = poly_adder(poly1, poly2)
print(result)

# вот эта задача гораздо лучше, чем задача с числом Пи.
#
# Должен заметить, что допустимый ввод ограничен: переменные могут быть только вида <коэффициент>x^<степень>,
# если на входе что-то вроде 12xy^2 программа выдаст некорректный результат, если вида 13yx^3 вообще упадет с ошибкой.
# эту проблему можно решить, если разбивать элементы заспличенных полиномов на коэффициент и остаток.
# Коэффициенты складывать, остаток где-то сохранять, потом собирать эут конструкцию обратно.
# Но мне уже немножечко лень.
