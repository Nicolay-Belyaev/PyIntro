# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# # Пример:
# # - [1.1, 1.2, 3.1, 10.01] => 0.19

def float_minmax_diff(array):
    for i in range(len(array)):
        array[i] = array[i] - int(array[i])
    result = round(max(array) - min(array), 3)
    return result


array_of_float = [1.1, 1.2, 3.1, 10.01]
print(float_minmax_diff(array_of_float))
