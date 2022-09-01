# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# Все задачи, связанные с временем, на практике всегда сложнее, чем кажутся.
# В этой, например, неочевидная сложность в том, что где первый день недели - понедeльник, а где-то - воскресенье.

# сделаем нашу программу чуть более устойчивой к некорректному вводу:
monday_first_day_of_week = None
number_of_day = None
while monday_first_day_of_week != 'y' and monday_first_day_of_week != 'n':
    monday_first_day_of_week = input("Понедельник первый день недели? y/n ").lower()  # хотя по факту - это bool
while number_of_day not in range(1, 8):
    number_of_day = int(input("Введите номер дня недели (от 1 до 7): "))

# Первый вариант
if (number_of_day == 7) or (monday_first_day_of_week == "y" and number_of_day == 6) or (monday_first_day_of_week == "n" and number_of_day == 1):
    print("Это выходной")
else:
    print("Это будний день")
# стремление к сокращению количества строк не всегда приводит к хорошему результату.

# Второй вариант
if number_of_day == 7:
    print("Это выходной")
elif monday_first_day_of_week == "y" and number_of_day == 6:
    print("Это выходной")
elif monday_first_day_of_week == "n" and number_of_day == 1:
    print("Это выходной")
else:
    print("Это будний день")
# приходится дублировать вывод, but i want to keep it DRY

# Третий вариант
def checker(list_of_weekends):
    if number_of_day in list_of_weekends:
        print("Это выходной")
    else:
        print("Это будний день")

if monday_first_day_of_week == 'y':
    checker(list_of_weekends=[6, 7])
else:
    checker(list_of_weekends=[1, 7])
# тут и остановимся.