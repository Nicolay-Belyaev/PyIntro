# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input('Задайте количество членов последовательности: '))

list_of_k = []
i = 1
while i <= k:
    list_of_k.append((1+1/i)**i)
    i += 1

list_of_k_sum = sum(list_of_k)
print(list_of_k_sum)