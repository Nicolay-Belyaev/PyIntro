# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random

N = int(input('Откуда начнем? '))
list_of_num = [0] * (N)
for i in range(N):
    list_of_num[i] = random.randint(-N, N)
print(list_of_num)

# заморочился с вводом немного / сомнительный вариант c try-except и break, но хотелось пощупать /
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

# хорошо бы сдеать возврат к вводу если что-то пошло не так. но получается какая-то рекурсивная ерунда.
# В дебаггере висит два инстанса функции, первый, где ввод некорректный, второй отрабаывает нормально,
# на нормальном вводе. Пока не знаю, что с этим делать.


def pos_in_string():
    input_string = input(f'Введите позиции через пробел.\nПозиции в диапазоне от 1 до {len(list_of_num)} и не должны повторяться: ')
    input_string_splited = input_string.split(' ')
    if len(input_string_splited) == 0:
        print('Не введено ниодной позиции')
        #pos_in_string()
    try:
        for k in range(len(input_string_splited)):
            input_string_splited[k] = int(input_string_splited[k])
    except ValueError:
        print(f'Похоже, вы ввели не число.')
        #pos_in_string()
    for o in input_string_splited:
        if o not in range(1, len(list_of_num) + 1):
            print(f"Какой-то номер позиции меньше 1 или больше {len(list_of_num)}.")
            #pos_in_string()
    for m in input_string_splited:
        if input_string_splited.count(m) >= 2:
            print(f'Похоже, какие-то позиции повторяются.')
            break
            #pos_in_string()
    result1 = 1
    for n in input_string_splited:
        result1 *= list_of_num[n - 1]
    return result1

res = pos_in_string()
print(res)