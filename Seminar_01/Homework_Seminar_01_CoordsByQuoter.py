# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quoter = 0
while quoter == 0 or quoter not in range(1, 5):
    quoter = int(input('Введите номер четверти координатной плоскости (от 1 до 4: '))

# не все консоли корректно показывают знак ∞, поэтому будет пользовать текстом
if quoter == 1:
    print("X ∈ {0, +infinity}, y ∈ {0, +infinity})")
if quoter == 2:
    print("X ∈ {0, -infinity}, y ∈ {0, +infinity})")
if quoter == 3:
    print("X ∈ {0, -infinity}, y ∈ {0, -infinity})")
if quoter == 4:
    print("X ∈ {0, +infinity}, y ∈ {0, -infinity})")
    