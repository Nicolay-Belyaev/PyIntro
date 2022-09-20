# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

array = [1, 1, 2, 3, 4, 5, 5]
uniques = [i for i in array if array.count(i) == 1]  # очевидное применение

# for i in array:
#     if array.count(i) == 1:
#         uniques.append(i)

print(array)
print(uniques)
