# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# вещественные числа в Питоне (и не только в нем) строго не являются вещественными числами.
# float - это апроксимация вещественного числа с конечной точностью (память-то не бесконечная),
# хранящаяся в памяти в виде двоичной дроби (вроде бы).
# Это приводит к неточности десятичных представление. 0.123 -> 0.123000000045...

float_number = float(input('Введите вещественное число: '))
accuracy = int(input('Сколько знаков после запятой? '))  # возможно, для этого есть метод, но я не нашел.
# 123.321
left_side = int(float_number)  # 123
right_side = float_number - left_side # 0.321

sum_of_left_side = 0
while left_side % 10 != 0:
    sum_of_left_side += left_side % 10
    left_side //= 10

# 0.321 -> 3.21 -> sum + 3 -> 3.21 - 3 -> 0.21
sum_of_right_side = 0
i = 0
while i < accuracy:
    sum_of_right_side += int(right_side * 10)
    right_side = right_side * 10 - int(right_side * 10)
    i += 1

print(sum_of_left_side + sum_of_right_side)

# Но в этой задаче можно обойти проблемы хранения вещественных чисел. Правда, не очень изящно.

fake_float_number = input("Введите вещественное число: ")
fake_float_number_cleared = fake_float_number.replace(',', '').replace('.', '')

sum_of_fake_digits = 0
for i in fake_float_number_cleared:
    sum_of_fake_digits += int(i)
print(sum_of_fake_digits)
