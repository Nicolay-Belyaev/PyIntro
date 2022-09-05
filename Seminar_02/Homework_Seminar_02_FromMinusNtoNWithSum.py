# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

N = int(input('Откуда начнем? '))

list_of_N = []

for i in range(-N, N + 1):
    list_of_N.append(i)

print(list_of_N)

# заморочился с вводом немного
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
        print(f'Позиция за пределами допустимых значений. Введена позиция {pos}. \n'
              f'Диапаоз позиций от 1 до {N*2+1}. Cписок позиций: {list_of_pos}.')

# превращаем позиции в индексы и считаем результат
result = 0
for i in range(len(list_of_pos)):
    list_of_pos[i] -= 1
    result *= list_of_N[i]

print(result)