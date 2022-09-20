# 2. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# Следует использовать методы сокращенной обработки данных.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

incoming_list = [1, 2, 3, 5, 1, 5, 3, 10]
outcoming_list = [i for i in incoming_list if incoming_list.count(i) == 1]

print(outcoming_list)

outcoming_list2 = list(filter(lambda x: incoming_list.count(x) == 1, incoming_list))

print(outcoming_list2)