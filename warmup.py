# встроенные функции
# переменные
# условия
# циклы

# Проверяем числа на квадрат.

# a = int(input('Введите первую переменную: '))
# b = int(input('Введите вторую переменную: '))
#
# if a**2 == b:
#     print('Вторая переменная является квадратом первой.')
# elif b**2 == a:
#     print('Первая переменная является квадратом второй.')
# else:
#     print('Ни одно число не является квадратом другогой.')

# Ищем максимальное число из 5 вводных без использование стандартной библиотеки

list = []

for i in range(5):
    list.append(int(input('Введите число ')))
print(max(list))

# max = list[0]
# for i in range(1, 5):
#     if list[i] > max:
#         max = list[i]
#
# print(max)

