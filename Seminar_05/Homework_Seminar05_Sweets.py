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
Для достижения этого результата первому игроку первым ходом необходимо
привести начальное количество конфет к числу, кратному x+1.
Тогда сколько бы его оппонент не взял конфет в свой ход, первый игрок ответным ходом всегда сможет
вернуть общее число конфет к кратному х+1. Что неминуемо приведет к победе первого игрока.
"""
import random


# функция хода для живых игроков. не очень хорошо, что она кроме собственно ходов, проверяет винкондишен
# и выводит победителя. получается, у функции как бы два назначения.
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


def computer_turn(max_per_turn: int, sweets_amount: int):  # функция хода для бота с шепоткой шутеечек
    target_amount = int(sweets_amount/(max_per_turn + 1)) * (max_per_turn + 1)
    turn = sweets_amount - target_amount
    if turn == 0 and sweets_amount != max_per_turn + 1:
        turn = random.randint(1, max_per_turn)  # если игрок берет правильное количество, бот пытается его запутать.
        print(f'{bot}: {phrases[random.randint(0, 5)]}')
    if sweets_amount == max_per_turn + 1:
        print(f'{bot}: Кажется это конец. Добей меня')
        turn = 1
    sweets_amount -= turn
    print(f'Ваш железный оппонент взял {turn} штук.')
    print(f'Осталось {sweets_amount} конфет.')
    return sweets_amount


def player_switcher(current_player):  # передатчик хода между живыми игроками. функция хода-то одна на двоих
    if current_player == first_player:
        current_player = second_player
    else:
        current_player = first_player
    return current_player
"""
свичер можно описать через лямба-функцию. Правда, она получается не сильно анонимная и PEP8 так делать не советует.
switcher = lambda x: first_player if (x == second_player) else second_player
current_player = switcher(current_player)
"""


sweets_amount = 100
max_per_turn = 28

print('Добро пожаловать в увлекательную игру "Конфетки".')
print(f'Игра заключается в следующем: вы с оппонентом по очереди берете не более {max_per_turn} конфеток.')
print(f'Кто сделал последний ход - победил и забирает всего конфеты себе. Начинаем с {sweets_amount} конфет.\n')
ai_mode_selector = input('Для игры против человека введите в консоль цифру 1. Для игры против бота - нажмите Enter. ')

# хотя можно было встроить игру с ботом в структуру кода с мультиплеером, это плохой путь. будут отдельно через if.

# секция кода для игры в мультиплеере
if ai_mode_selector == "1":
    players = [input('Введите имя игрока: ') for i in range(2)]
    keys = [-1, 1]
    dict_of_players = {i: j for (i, j) in zip(keys, players)}

    # незамысловатый вариант рандома через словарь. надо бы вынести в функцию.
    randomizer = random.randrange(-1, 2, 2)  # от -1 до 1 есть еще 0. нам он не нужен.
    first_player = dict_of_players[randomizer]
    second_player = dict_of_players[-randomizer]
    print(f'Волею Случая, первый ход за игроком {first_player}.')

    current_player = second_player  # потому что мы сразу делаем свич.

    while sweets_amount != 0:
        current_player = player_switcher(current_player)
        sweets_amount = turns(max_per_turn, sweets_amount, current_player)

# секция кода для игры с ботом
else:
    player = input('Привет, игрок! Введи свое имя: ')
    bot = str(f'{random.randint(134, 95248)}bot')
    print(f'\nТвоим противником будет могучий {bot}. Он благородно отдаёт тебе первый ход.')
    print(f'Но берегись, {player}. Твой противник умеет играть в эту игру. Одна ошибка - и ты ошибся.')
    phrases = ['А ты неплохо играешь. Но я готов к твоей ошибке...', 'Кажется, ты уже играл в эту игру.',
               'Удача? Или знания...', 'Мне хватит одного неверного шага!', "Сдавайся! Я считаю быстрее!",
               'Ты ошибся! Ха-ха. А нет, это я плохо посчитал.']

    # другая структура цикла. хотел сделать разный вывод для победы игрока/бота. заодно корректно завершает игру.
    while True:
        sweets_amount = turns(max_per_turn, sweets_amount, current_player=player)
        if sweets_amount == 0:
            print(f'Победа! {player}, ты одолел холодный алгоритм, все конфеты твои. Только не ешь все сразу.')
            break
        sweets_amount = computer_turn(max_per_turn, sweets_amount)
        if sweets_amount == 0:
            print(f'Поражение! {player}, цифровой мир победил, алгоритм оказался сильней. Увы, {bot} унёс все конфеты.')
            break
