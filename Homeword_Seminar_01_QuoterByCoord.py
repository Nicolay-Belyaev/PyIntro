# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# [если ни X, ни Y != 0 точка не может находиться на оси]
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

X = 0
Y = 0
# мы же договорились, что нулевые координаты не берем?
while X == 0:
    X = float(input('Введите координату X, отличную от 0: '))
while Y == 0:
    Y = float(input('Введите координату Y, отличную от 0: '))

if X > 0 and Y > 0:
    print("1")
if X < 0 and Y > 0:
    print("2")
if X < 0 and Y < 0:
    print("3")
if X > 0 and Y < 0:
    print("4")

# ладно, ладно, сейчас сделаю

A = float(input('Введите координату A: '))
B = float(input('Введите координату B: '))

if A == 0 and B == 0:
    print("Мы в начале начал")
if A == 0 and B > 0:
    print("Мы на оси B выше начала начал")
if A == 0 and B < 0:
    print("Мы на оси B ниже начала начал")
if A > 0 and B == 0:
    print("Мы на оси A справа от начала начал")
if A < 0 and B == 0:
    print("Мы на оси A слева от начала начал")
if A > 0 and B > 0:
    print("1")
if A  < 0 and B > 0:
    print("2")
if A  < 0 and B < 0:
    print("3")
if A  > 0 and B < 0:
    print("4")