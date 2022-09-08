# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


array_of_numbers = [2, 3, 5, 6]


def product_of_pairs(array):
    array_of_product = []
    # отсюда начинается костыль
    corrector = 0
    if len(array) % 2 != 0:
        corrector = 1
    for i in range(len(array) // 2 + corrector):  # здесь костыль заканчивается
        product = array[i] * array[len(array) - (i + 1)]
        array_of_product.append(product)
    return array_of_product


print(product_of_pairs(array_of_numbers))
