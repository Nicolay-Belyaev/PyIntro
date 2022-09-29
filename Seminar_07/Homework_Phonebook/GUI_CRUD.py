from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox


def gui_create_(self, w_ask):
    w_ask = Tk()
    w_ask.geometry('800x600')
    w_ask.grid_anchor("center")

    l1, l2, l3 = [Label(w_ask, text=t, font=(self._font, 20)) for t in
                  ["Введите имя", "Введите фамилию", "Введите номер"]]
    l1.grid(column=0, row=0)
    l2.grid(column=0, row=1)
    l3.grid(column=0, row=2)

    n1, n2, n3 = [Entry(w_ask, width=20, font=(self._font, 20)) for _ in range(3)]
    n1.grid(column=1, row=0)
    n2.grid(column=1, row=1)
    n3.grid(column=1, row=2)

    start_button = Button(w_ask,
                          text="Создать",
                          font=(self._font, 20),
                          bg='grey', fg='white',
                          command=lambda: self.set_command_and_params(w_ask, "запись", n1.get(), n2.get(), n3.get()),
                          height=2, width=10)
    start_button.grid(column=0, row=3)


def gui_search_(self, w_ask):
    w_ask = Tk()
    w_ask.geometry('800x600')
    w_ask.grid_anchor("center")

    l1, l2, l3, l4 = [Label(w_ask, text=t, font=(self._font, 20)) for t in
                      ["Введите ID", "Введите имя", "Введите фамилию", "Введите номер"]]
    l1.grid(column=0, row=1)
    l2.grid(column=0, row=2)
    l3.grid(column=0, row=3)
    l4.grid(column=0, row=4)

    n1, n2, n3, n4 = [Entry(w_ask, width=20, font=(self._font, 20)) for _ in range(4)]
    n1.grid(column=1, row=1)
    n2.grid(column=1, row=2)
    n3.grid(column=1, row=3)
    n4.grid(column=1, row=4)
    search_button = Button(w_ask,
                           text="Искать",
                           font=(self._font, 20),
                           bg='grey', fg='white',
                           command=lambda: self.set_command_and_params(w_ask, "поиск", n1.get(), n2.get(),
                                                                       n3.get(), n4.get()),
                           height=2, width=10)
    search_button.grid(column=1, row=5)


def gui_update_(self, w_ask):
    w_ask = Tk()
    w_ask.geometry('800x600')
    w_ask.grid_anchor("center")

    l1, l2, l3 = [Label(w_ask, text=t, font=(self._font, 20)) for t in
                  ["Укажи ID для изменения", "Что изменить?", "На что изменить?"]]
    l1.grid(column=0, row=1)
    l2.grid(column=0, row=2)
    l3.grid(column=0, row=3)

    n1, n3 = [Entry(w_ask, width=20, font=(self._font, 20)) for _ in range(2)]
    n1.grid(column=1, row=1)
    n3.grid(column=1, row=3)

    marker = Combobox(w_ask, font=(self._font, 16))
    marker['values'] = ("ИМЯ", "ФАМИЛИЯ", "ТЕЛЕФОН")
    marker.current(0)
    marker.grid(column=1, row=2)

    done_button = Button(w_ask,
                         text="Изменить",
                         font=(self._font, 20),
                         bg='grey', fg='white',
                         command=lambda: self.set_command_and_params(w_ask, "изменение", marker.get(), n3.get(),
                                                                     n1.get()),
                         height=2, width=10)
    done_button.grid(column=1, row=5)


def gui_quit_(self):
    messagebox.showinfo(message='Еще увидимся!')
    self.set_command_and_params(self.window, "выход")

    def gui_update(self, w_ask):
        w_ask = Tk()
        w_ask.geometry('800x600')
        w_ask.grid_anchor("center")

        l1, l2, l3 = [Label(w_ask, text=t, font=(self._font, 20)) for t in
                      ["Укажи ID для изменения", "Что изменить?", "На что изменить?"]]
        l1.grid(column=0, row=1)
        l2.grid(column=0, row=2)
        l3.grid(column=0, row=3)

        n1, n3 = [Entry(w_ask, width=20, font=(self._font, 20)) for _ in range(2)]
        n1.grid(column=1, row=1)
        n3.grid(column=1, row=3)

        marker = Combobox(w_ask, font=(self._font, 16))
        marker['values'] = ("ИМЯ", "ФАМИЛИЯ", "ТЕЛЕФОН")
        marker.current(0)
        marker.grid(column=1, row=2)

        done_button = Button(w_ask,
                             text="Изменить",
                             font=(self._font, 20),
                             bg='grey', fg='white',
                             command=lambda: self.set_command_and_params(w_ask, "изменение", marker.get(), n3.get(),
                                                                         n1.get()),
                             height=2, width=10)
        done_button.grid(column=1, row=5)
