# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

array_of_numbers = [2, 3, 5, 9, 3, 1, 1]


def sum_on_odd_pos(array):
    summ = 0
    for i in range(1, len(array), 2):
        summ += array[i]
    return summ


print(sum_on_odd_pos(array_of_numbers))
