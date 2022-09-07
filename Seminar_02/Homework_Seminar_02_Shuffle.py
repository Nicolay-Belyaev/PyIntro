# Реализуйте алгоритм перемешивания списка.
import random

# не буду писать свой рандомайзер. все равно приду к какому-нибудь варианту использования UNIX Timestamp

in_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result_array = []

# проблема этого метода в том, что чем дальше к концу массива, тем чаще будет срабатывать else
# у этой задачи точно больше одного решения
while len(result_array) != len(in_array):
    rnd_elem = in_array[random.randint(0, len(in_array)-1)]
    if rnd_elem not in result_array:
        result_array.append(rnd_elem)
    else:
        continue

print(in_array)
print(result_array)
