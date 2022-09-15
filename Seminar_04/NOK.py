# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


def dividers_finder(number):
    dividers = []
    divider = 2
    while number != 1:
        if number % divider == 0:
            dividers.append(divider)
            number = number / divider
        else:
            divider += 1
    return dividers


dividers_of_a = dividers_finder(a)
dividers_of_b = dividers_finder(b)

print(dividers_of_a)
print(dividers_of_b)


uniques = set(dividers_of_a)

print(uniques)
# fot i in unique_dividers:
#     counter_a = dividers_of_a.count(i)
#     counter_b = dividers_of_b.count(i)
