# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Это задание выполнено при поддержке ИГХиК (института грязных хаков и костылей).


def base10_base2(base10):
    leftovers = []
    while True:
        division_result = base10 / 2
        if int(division_result) < 1:
            leftovers.append(str('1'))
            leftovers.reverse()
            break
        division_leftover = int(base10 % 2)
        leftovers.append(str(division_leftover))
        base10 = division_result
    base2 = int(''.join(leftovers))
    return base2


number = int(input('Введите число: '))
print(base10_base2(number))

# вся задача должна решаться в 2-3 строчки. но пока решаем вот так.
