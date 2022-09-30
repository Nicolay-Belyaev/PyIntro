from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog


def init_second_window(w_ask):
    w_ask = Tk()
    w_ask.geometry('1200x600')
    w_ask.grid_anchor("center")
    w_ask.focus()
    return w_ask


def gui_create_(self, w_ask):
    w_ask = init_second_window(w_ask)

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
    w_ask = init_second_window(w_ask)

    l1, l2 = [Label(w_ask, text=t, font=(self._font, 20)) for t in
              ["Что будем искать?", "Введите значение"]]
    l1.grid(column=0, row=0)
    l2.grid(column=0, row=1)

    marker = Combobox(w_ask, font=(self._font, 16))
    marker['values'] = ("Вывести все значения", "ID", "ИМЯ", "ФАМИЛИЯ", "ТЕЛЕФОН")
    marker.current(0)
    marker.grid(column=1, row=0)

    n1 = Entry(w_ask, width=20, font=(self._font, 20))
    n1.grid(column=1, row=1)

    search_button = Button(w_ask,
                           text="Искать",
                           font=(self._font, 20),
                           bg='grey', fg='white',
                           command=lambda: self.set_command_and_params(w_ask, "поиск",
                                                                       "" if marker.get() == "Вывести все значения" else marker.get(),
                                                                       n1.get()),
                           height=2, width=10)
    search_button.grid(column=1, row=5)


def gui_update_(self, w_ask):
    w_ask = init_second_window(w_ask)

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


def gui_delete_(self, w_ask):
    w_ask = init_second_window(w_ask)

    l1 = Label(w_ask, text="Укажи ID записи для удаления", font=(self._font, 20))
    l1.grid(column=0, row=0)
    n1 = Entry(w_ask, width=20, font=(self._font, 20))
    n1.grid(column=1, row=0)
    delete_button = Button(w_ask,
                           text="Удалить",
                           font=(self._font, 20),
                           bg='grey', fg='white',
                           command=lambda: self.set_command_and_params(w_ask, "удаление", n1.get()),
                           height=2, width=10)
    delete_button.grid(column=1, row=5)


def gui_export_(self, w_ask):
    w_ask = init_second_window(w_ask)

    l1 = Label(w_ask, text="Укажи куда и как экспортировать.\n"
                           "Можно оставить поле пустым,\n"
                           "тогда сохраню в текущую папку", font=(self._font, 20))
    l1.grid(column=0, row=0)
    n1 = Entry(w_ask, width=40, font=(self._font, 14))
    n1.grid(column=0, row=1)

    extension = Combobox(w_ask, width=5, font=(self._font, 16))
    extension['values'] = ("txt", "csv")
    extension.current(1)
    extension.grid(column=1, row=1)

    saveas_button = Button(w_ask,
                           text="Выбрать папку",
                           font=(self._font, 20),
                           bg='grey', fg='white',
                           command=lambda: self.opendialogue_save_file(n1, extension),
                           height=2, width=15)
    saveas_button.grid(column=0, row=2)
    ready_button = Button(w_ask,
                          text="Экспорт",
                          font=(self._font, 20),
                          bg='grey', fg='white',
                          command=lambda: self.set_command_and_params(w_ask, "экспорт", extension.get(),
                                                                      n1.get() if len(n1.get()) else "exported"),
                          height=2, width=10)
    ready_button.grid(column=1, row=2)


def gui_import_(self, w_ask):
    w_ask = init_second_window(w_ask)
    l1 = Label(w_ask, text="Укажи что импортировать", font=(self._font, 20))
    l1.grid(column=0, row=0)
    n1 = Entry(w_ask, width=50, font=(self._font, 14))
    n1.grid(column=0, row=1)

    var = IntVar()
    var.set(0)
    Radiobutton(w_ask, text="Дописать к текущему справочнику", command=lambda: var.set(0),
                variable=var, value=0).grid(column=0, row=3)
    Radiobutton(w_ask, text="удалить текущий справочник", command=lambda: var.set(1),
                variable=var, value=1).grid(column=0, row=4)

    askpath_button = Button(w_ask,
                            text="Выбрать файл",
                            font=(self._font, 20),
                            bg='grey', fg='white',
                            command=lambda: self.opendialogue_find_file(n1),
                            height=2, width=15)
    askpath_button.grid(column=0, row=2)
    ready_button = Button(w_ask,
                          text="Импорт",
                          font=(self._font, 20),
                          bg='grey', fg='white',
                          command=lambda: messagebox.showinfo(title='Ошибка',
                                                              message="Выберите файл") if not len(n1.get()) else
                          self.set_command_and_params(w_ask, "импорт",
                                                      var.get(),
                                                      n1.get()),
                          height=2, width=10)
    ready_button.grid(column=1, row=2)
