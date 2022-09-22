# Вычислить число π c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141

from decimal import *
from math import factorial


def pi_with_accuracy(accuracy: int):
    def chudnovsky(n):
        long_pi = Decimal(0)
        k = 0
        while k < n:
            long_pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))*(13591409+545140134*k)/(640320**(3*k)))
            k += 1
        long_pi = long_pi * Decimal(10005).sqrt()/4270934400
        long_pi = long_pi**(-1)
        return long_pi

    def rounder(zeros: int):
        str_of_zero = ["0" for i in range(zeros)]
        zero = "".join(str_of_zero)
        pi = (chudnovsky(4).quantize(Decimal(f"1.{zero}"), ROUND_FLOOR))
        return pi

    return rounder(accuracy)


zeros = int(input("Введите количество знаков после запятой (максимум - 27): "))
print(pi_with_accuracy(zeros))

