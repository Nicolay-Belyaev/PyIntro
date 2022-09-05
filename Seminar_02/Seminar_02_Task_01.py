# Напишите программу, которая принимает
# на код число N и выдаёт последовательность из N членов.
# Пример:
# # - Для
# N = 5: 1, -3, 9, -27, 81

N = int(input('Введите число: '))

result_list = [1] * N

for i in range(1, N):
    result_list[i] = result_list[i-1] * -3

print(result_list)

result_list2 = [1] * N

j = 1
while j < N:
    result_list2[j] = result_list2[j - 1] * -3
    j += 1

print(result_list2)