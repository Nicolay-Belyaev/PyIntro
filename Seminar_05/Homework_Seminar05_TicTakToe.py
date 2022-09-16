# Создайте программу для игры в ""Крестики-нолики"".

from tkinter import *
import tkinter.font as font

# задача функции on_click - выдавать разные результаты в зависимости от того, четное или нечетное количество раз она
# была вызвана. значит, где-то вне этой функции об этом должна храниться информация.
# и хотя использование глобальных переменных не есть хорошая практика, по-другому я сделать пока не смог.
# вроде как тут меня могло выручить замыкание, но мне пока нехватает навыков, что бы его сюда вкорячить.

#TODO
# сделать винкондишины
# вероятный способ - создать наборы кнопок, значения текста в которых надо проверять на одинаковость
# возможно, придется все это засовывать в функции on_click, но лучше бы этого избежать


def on_click(event):
    global counter
    if counter % 2 != 0:
        event.widget["text"] = f'{event.widget} X'
    else:
        event.widget["text"] = f'{event.widget} 0'
    counter += 1


def field_filler(array_of_buttons):
    index = 0
    for row_numbers in range(3):
        for column_number in range(3):
            array_of_buttons[index].grid(column=column_number, row=row_numbers)
            index += 1

counter = 1 # вспомогательная переменная для функции on_click

window = Tk()
window.title('Крестики-нолики')
window.geometry('1100x990')


myFont = font.Font(size=30)
buttons = [Button(window, text='', width=15, height=6) for i in range(9)]
# скорее всего, можно прикрутить обработчик событий в генератор кнопок, но я не шмог.
for i in range(len(buttons)):
    buttons[i].bind('<Button-1>', on_click)
    buttons[i]['font'] = myFont

field_filler(buttons)

window.mainloop() # по сути, это такой местный while true

