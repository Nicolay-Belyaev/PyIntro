# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# # Пример:
# # - [1.1, 1.2, 3.1, 10.01] => 0.19

def float_minmax_diff(array):
    cleared_from_int = list(map(lambda x: x - int(x), array))
    result = round(max(cleared_from_int) - min(cleared_from_int), 3)
    return result


array_of_float = [1.1, 1.2, 3.1, 10.01]
print(float_minmax_diff(array_of_float))
