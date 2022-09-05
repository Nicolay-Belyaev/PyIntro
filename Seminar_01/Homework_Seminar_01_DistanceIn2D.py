# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coords_of_point_A = []
coords_of_point_B = []

for i in range(2):
    coords_of_point_A.append(float(input('Введите {} координату точки А: '.format(i+1))))
for i in range(2):
    coords_of_point_B.append(float(input('Введите {} координату точки B: '.format(i+1))))

distance_between_points = pow(pow(coords_of_point_B[0]-coords_of_point_A[0], 2)+pow(coords_of_point_B[1]-coords_of_point_A[1], 2), 0.5)

print(distance_between_points)