# Дан список чисел.Создайте список, в который попадают числа, описываемые возрастающую
# последовательность.Порядок элементов менять нельзя.
#
# *Пример: *
# [1, 5, 2, 3, 4, 6, 1, 7] = > [1, 5, 6, 7]
# и
# т.д.

incoming_list = [1, 5, 2, 3, 4, 6, 1, 7]
outcoming_list = [incoming_list[i] for i in range(len(incoming_list)) if incoming_list[i] > incoming_list[i-1]]

print(outcoming_list)
