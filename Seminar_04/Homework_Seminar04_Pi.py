# Вычислить число π c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141

from decimal import *
from math import factorial


def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))*(13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


# https://habr.com/ru/post/309674/2
# я это нашел и лучше мне не сделать


def pi_with_accuracy(accuracy: int):
    str_of_zero = ["0" for i in range(accuracy)]
    # for i in range(accuracy):
    #     str_of_zero.append("0")
    zero = "".join(str_of_zero) # можно было бы строку через конкатенацию собрать, но конкатенация - неочевидная вещь.
    pi = (chudnovsky(4).quantize(Decimal(f"1.{zero}"), ROUND_FLOOR))
    return pi


# ну а это я сделал сам, Decimal прикольная штука
# вся эта история работает до 27 знаков после запятой (28 всех знаков), это настройка по умолчанию для Decimal.


zeros = int(input("Введите количество знаков после запятой (максимум - 27): "))
print(pi_with_accuracy(zeros))

# хотя мне в целом понятно, зачем нужны такие задачи, мне они никогда не нравились.
# это что-то вроде: "Изготовьте молоток. Да, молоток у вас уже есть, на изготовление вы потратите 50 баксов,
# но это хорошая практика. Практика изготовления молотков, которые у вас уже есть. Вы больше никогда не будете
# делать молотки, потому что если у вас нет молотка, вы купите его за 5 баксов."
