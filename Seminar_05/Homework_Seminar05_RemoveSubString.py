# Напишите программу, удаляющую
# из текста
# все слова, содержащие "абв".

my_string = 'Мы неабв очень любим Питон иабв Джавабв'.split()
res_list = [i for i in my_string if 'абв' not in i]
print(res_list)

