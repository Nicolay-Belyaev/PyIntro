# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def coefficients_generator():  # так-то вообще здесь не нужная штука. но по условиям задачи нужен список.
    array_of_coefficients = []
    for i in range(101):
        array_of_coefficients.append(random.randint(0, 100))
    random_coefficients = array_of_coefficients[1]
    return random_coefficients


def str_polynomial_generator(k):
    result_array = []
    for i in range(k+1):
        if i == 0:
            variable = f"{coefficients_generator()}"
        elif i == 1:
            variable = f"{coefficients_generator()}x"
        else:
            variable = f"{coefficients_generator()}x^{i}"
        result_array.append(variable)
    result_array.reverse()
    result_string = " + ".join(result_array) + " = 0"
    return result_string

power = int(input('Введите степень многочлена: '))
file = open('result.txt', 'w')
file.write(str_polynomial_generator(power))
