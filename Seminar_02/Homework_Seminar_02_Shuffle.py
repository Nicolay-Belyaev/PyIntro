# Реализуйте алгоритм перемешивания списка.
import random

# я пока не буду писать свой рандомайзер. все равно приду к какому-нибудь варианту использования UNIX Timestamp

array = [0, 1, 2, 3, 4]
result_array = [] * len(array)

for i in range(0, len(array)):
    rnd = random.randint(0, 4)
    result_array.append(array[rnd])

