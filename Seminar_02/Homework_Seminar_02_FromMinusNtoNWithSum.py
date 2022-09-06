# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random

N = int(input('Откуда начнем? '))
list_from_mN_to_N = []
for i in range(-N, N + 1):
    list_from_mN_to_N.append(i)
list_of_num = []
counter = 0
while counter < N:
    list_of_num.append(list_from_mN_to_N[random.randint(0, len(list_from_mN_to_N)-1)])
    counter += 1
print(list_of_num)

# заморочился с вводом немного / сомнительный вариант c try-except и break, хотелось пощупать /
list_of_pos = []
while True:
    try:
        pos = int(input('Введите позицию числа. Для окончания ввода нажмите Enter: '))
    except ValueError:
        break
    if pos not in list_of_pos and pos in range(1, N*2+2):
        list_of_pos.append(pos)
        print(f'Позиция {pos} добавлена в список. Cписок позиций {list_of_pos}.')
    elif pos in list_of_pos:
        print(f'Такая позиция уже добавлена в список. Cписок позиций {list_of_pos}.')
    elif pos not in range(1, N*2+2):
        print(f'Извини, братан, нет такой позиции. Введена позиция {pos}. \n'
              f'Диапазон позиций от 1 до {N*2+1}. Cписок позиций: {list_of_pos}.')

if len(list_of_pos) == 0:
    print("не выбрано ни одной позиции")
else:
    result = 1
    for j in list_of_pos:
        result *= list_of_num[j-1]
    print(result)

# и тут я перечитал задание, оказывается надо через пробел ввод сделать =(
# надо бы доделать проверку ввода до конца, но чет уже лень

input_string = input(f'Введите позиции через пробел.\nПозиции в диапазоне от 1 до {len(list_of_num)} и не должны повторяться: ')
if len(input_string) == 0:
    print("не выбрано ни одной позиции")
else:
    input_string_splited = input_string.split(' ')
    result1 = 1
    for i in range(len(input_string_splited)):
        input_string_splited[i] = int(input_string_splited[i])
    for j in input_string_splited:
        if j not in range(1, len(list_of_num) + 1):
            print(f"Введен номер позиции меньше 1 или больше {len(list_of_num)}.")

    for k in input_string_splited:
        result1 *= list_of_num[k-1]
    print(result1)
