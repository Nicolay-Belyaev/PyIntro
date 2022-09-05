#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#  Пример:
#  Пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

# я не буду класть рекурсию в рекурсию

N = int(input('Введите число: '))

array = []
i = 1
while i <= N:
    array.append(factorial(i))
    i += 1
print(array)

# у нас же тут тренировочные задания


def recurrent_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recurrent_factorial(n - 1)


another_array = []
for i in range(1, N+1):
    another_array.append(recurrent_factorial(i))
print(another_array)
