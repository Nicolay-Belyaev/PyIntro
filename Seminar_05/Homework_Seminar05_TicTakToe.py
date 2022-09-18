# Создайте программу для игры в ""Крестики-нолики"".

'''
нужна структура более высокого уровня (над функциями). это классы скорее всего, но про них я пока знаю только то,
что они существуют.
'''

from tkinter import *
import tkinter.font as font
import tkinter.messagebox as mb


def buttons_generator():  # генератор списка кнопок из которых будет собираться игровое поле
    my_font = font.Font(size=30)
    buttons = [Button(window, text='', width=15, height=6) for i in range(9)]
    # скорее всего, можно прикрутить обработчик событий в генератор кнопок, но я не шмог.
    for i in range(len(buttons)):
        buttons[i].bind('<Button-1>', on_click)
        buttons[i]['font'] = my_font
    return buttons


def field_filler(array_of_buttons):  # заполняет поле кнопками из buttons_generator'а
    index = 0
    for row_numbers in range(3):
        for column_number in range(3):
            array_of_buttons[index].grid(column=column_number, row=row_numbers)
            index += 1


'''
задача функции on_click - выдавать разные результаты в зависимости от того, четное или нечетное количество раз она
была вызвана. значит, где-то вне этой функции об этом должна храниться информация.
и хотя использование глобальных переменных не есть хорошая практика, по-другому я сделать пока не смог.
вроде как тут меня могло выручить замыкание, но мне пока нехватает навыков, что бы его сюда вкорячить.
'''


def on_click(event):  # рисует крестик или нолик в нажатой кнопке, вызывает проверку условия победы
    global counter  # сюда будем складывать количество вызовов функции
    if counter % 2 != 0:
        event.widget["text"] = f'X'
    else:
        event.widget["text"] = f'0'
    counter += 1
    win_conditions()


'''
# функцию win_conditions можно оптимизировать. достаточно проверять только те строки/столбы/диагонали,
# в которые был поставлен последний крестик/нолик. но я не буду.
'''


def win_conditions():  # проверяет не закончилась ли у нас игра, вызывает всплывающие окно в случае победы
    conditions_pos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in conditions_pos:
        a, b, c = i
        if (l_buttons[a]['text'] == l_buttons[b]['text'] == l_buttons[c]['text']) and l_buttons[a]['text'] != '':
            for j in i:
                l_buttons[j].configure(bg='green')
            winner = 'Крестики' if l_buttons[a]['text'] == 'X' else 'Нолики'
            win_message(winner)


def win_message(winner):  # рисует всплывающее окно если сработал винкондишин
    global l_buttons  # а вот тут я не вижу ничего плохого в глобале
    answer = mb.askyesno(
        title='Игра окончена',
        message=f'Победили {winner}. Новая игра?')
    if answer:  # чистим кнопки и перезаполняем поле для новой игры
        l_buttons = buttons_generator()
        field_filler(l_buttons)
    else:  # закрываем окно игры, берем портвейн, идем домой.
        window.destroy()


counter = 1  # вспомогательная переменная для функции on_click, хранит количество вызовов функции

window = Tk()
window.title('Крестики-нолики')
window.geometry('1100x990')

l_buttons = buttons_generator()
field_filler(l_buttons)

window.mainloop()  # по сути, это такой местный while true