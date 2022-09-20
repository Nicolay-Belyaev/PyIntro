# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

string = input('Введите числа через пробел: ')
string_list = list(map(int, (string.split(" "))))   # это тоже напрашивается

# for i in range(len(string_list)):
#     string_list[i] = int(string_list[i])

res = (max(string_list), min(string_list))
print(res)
