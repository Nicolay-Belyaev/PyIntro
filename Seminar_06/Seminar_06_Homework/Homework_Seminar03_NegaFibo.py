# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#

def nego_fibo(border):
    def fibo(pos):
        if pos == 0:
            return 0
        if pos in (1, 2):
            return 1
        return fibo(pos - 1) + fibo(pos - 2)

    def fibo_filler(size: int):
        base_array = [fibo(i) for i in range(size + 1)]
        return base_array

    def mirror(array: list):
        array.remove(0)
        mirrored_array = list(map(lambda x: array[x]*-1 if x % 2 == 0 else array[x], range(len(array))))
        mirrored_array.reverse()
        return mirrored_array


    def glue(array1: list, array2: list):  # можно extend'ом, но когда начала делать костыли, сложно остановиться
        for i in range(len(array2)):
            array1.append(array2[i])
        return array1

    array_1 = fibo_filler(border)
    array_2 = mirror(fibo_filler(border))
    res = glue(array_2, array_1)
    return res

k = int(input('Введите границу: '))
res_array = nego_fibo(k)
print(res_array)
