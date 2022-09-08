# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time


def rand_by_time(amount_of_digits):
    rnd = int((time.time() - int(time.time())) * (10**amount_of_digits))
    return rnd


amount_of_digits = int(input('Сколько разрядов? '))
print(rand_by_time(amount_of_digits))
