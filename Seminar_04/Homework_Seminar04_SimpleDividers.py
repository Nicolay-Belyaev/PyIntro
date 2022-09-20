# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 20" -> [2, 2, 5]

number = int(input("Введите число для распиливания на простые множители: "))

simple_dividers = []
divider = 2
while number != 1:
    if number % divider == 0:
        simple_dividers.append(divider)
        number /= divider
    else:
        divider += 1

print(simple_dividers)
