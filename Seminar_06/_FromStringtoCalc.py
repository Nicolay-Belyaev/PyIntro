# Напишите программу вычисления арифметического выражения, заданного строкой.
# Используются операторы +,-,*,/ . Приоритет стандартный.

# a = ['412', '*', '123', '+', '412']
# a = list(map(lambda x: int(x) if x.isdigit() else x, a))
# print(a)



incoming_string = "22+2*2+25*2-22"

intermediate_list = []
current_number = ''
for i in range(len(incoming_string)):
    if incoming_string[i].isdigit():
        current_number += incoming_string[i]
        if i == len(incoming_string) - 1:
            intermediate_list.append(current_number)
    if not incoming_string[i].isdigit():
        intermediate_list.append(int(current_number))
        intermediate_list.append(incoming_string[i])
        current_number = ''

long = len(intermediate_list)
j = 0
while j < long:
    if intermediate_list[j] == "*":
        inter_result = intermediate_list[j-1] * intermediate_list[j+1]
        intermediate_list[j] = inter_result
        del intermediate_list[i-j]
        del intermediate_list[i+j]
        long = len(intermediate_list)
        j += 1

print(intermediate_list)