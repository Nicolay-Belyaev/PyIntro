# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i - 1].Найдите это число.
# 1 2 4 5

with open('numbers1.txt', 'r') as file:
    list_numbers = file.read()

list_numbers = list(map(int, list_numbers.split(' ')))
lst = [(list_numbers[i] - 1) for i in range(1, len(list_numbers)) if list_numbers[i] - 1 != list_numbers[i-1]]
print(lst)

