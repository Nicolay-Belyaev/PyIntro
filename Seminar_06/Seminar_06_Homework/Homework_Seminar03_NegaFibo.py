# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

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
        mirrored_array = list(map(lambda x: array[x]*-1 if x % 2 == 0 else array[x], range(len(array))))
        mirrored_array.remove(0)
        mirrored_array.reverse()
        return mirrored_array

    array_1 = fibo_filler(border)
    array_2 = mirror(array_1)
    array_2.extend(array_1)
    return array_2

k = int(input('Введите границу: '))
res_array = nego_fibo(k)
print(res_array)
