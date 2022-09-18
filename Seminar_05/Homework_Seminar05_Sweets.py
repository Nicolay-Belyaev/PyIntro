# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента:
# a) Добавьте игру против бота.
# b) Подумайте как наделить бота "интеллектом".

"""
Пусть количество конфет, который можно взять = x.
Первый игрок всегда выигрывает, если знает Правило.
Задача первого игрока - свести игру к ситуации, когда на ход его оппонента количество конфет будет = x+1.
Оппонент будет вынужден взять 1 конфету, и первый игрок заберет х конфет - победа.
Так как ходы не квантуются, для достижения этого результата первому игроку первым ходом необходимо
привести начальное количество конфет к числу, кратному x+1.
Тогда сколько бы его оппонент не взял конфет в свой ход, первый игрок ответным ходом всегда сможет
вернуть общее число конфет к кратному х+1. Что неминуемо приведет к победе первого игрока.
"""
import random


def turns(max_per_turn: int, sweets_amount: int, current_player: str):
    while True:
        current_player_turn = int(input(f'{current_player}, сколько конфеток возьмешь? '))
        if current_player_turn > sweets_amount or current_player_turn > max_per_turn or current_player_turn <= 0:
            print(f'Столько взять нельзя')
        else:
            sweets_amount -= current_player_turn
            if sweets_amount == 0:
                print(f'Конфет не осталось, победил игрок {current_player}')
                break
            else:
                print(f'Осталось {sweets_amount} конфет')
                break
    return sweets_amount


def player_switcher(current_player):
    if current_player == first_player:
        current_player = second_player
    else:
        current_player = first_player
    return current_player

# свичер можно описать через лямба-функцию. Правда, она получается не сильно анонимная и PEP8 так делать не советует.
# switcher = lambda x: first_player if (x == second_player) else second_player
# current_player = switcher(current_player)


sweets_amount = 285
max_per_turn = 28

print('Добро пожаловать в увлекательную игру "Конфетки".')
print(f'Игра заключается в следующем: вы с оппонентом по очереди берете не более {max_per_turn} конфеток.')
print(f'Кто сделал последний ход - победил и забирает всего конфеты себе. Начинаем с {sweets_amount} конфет.')

players = [input('Введите имя игрока: ') for i in range(2)]
keys = [-1, 1]
dict_of_players = {i: j for (i, j) in zip(keys, players)}

# незамысловатый вариант рандома через словарь. Нужен исключительно потому, что я хочу нормально определить игроков
randomizer = random.randrange(-1, 2, 2)
first_player = dict_of_players[randomizer]
second_player = dict_of_players[-randomizer]
print(f'Волею Случая, первый ход за игроком {first_player}.')

current_player = second_player  # потому что мы сразу делаем свич

while sweets_amount != 0:
    current_player = player_switcher(current_player)
    sweets_amount = turns(max_per_turn, sweets_amount, current_player)
