# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

file = open('1.txt', 'r')
poly1 = file.read()

file = open('2.txt', 'r')
poly2 = file.read()


splited_poly1 = poly1.split(' + ')
splited_poly2 = poly2.split(' + ')

print(splited_poly1, splited_poly2)
