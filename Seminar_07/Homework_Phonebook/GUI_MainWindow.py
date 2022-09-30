from GUI_CRUD import *


class MainWindow:
    window = Tk()
    w_ask = None
    gui_command_and_params = []
    _font = "Calibri"

    # базовые функции описаны в отдельном файле
    gui_create = gui_create_
    gui_search = gui_search_
    gui_update = gui_update_
    gui_quit = gui_quit_
    gui_delete = gui_delete_
    gui_export = gui_export_
    gui_import = gui_import_

    def opendialogue_find_file(self, n1):
        filename = filedialog.askopenfilename(
            filetypes=(('All files', '*.*'), ('text files', '*.txt'), ('Csv files', '*.csv')))

        n1.delete(0, END)
        n1.insert(0, filename)

    def opendialogue_save_file(self, n1, extension):
        filename = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt"), ("csv file", ".csv")])
        if filename:  # user selected file
            name, ext = filename.split('.')
            n1.delete(0, END)
            n1.insert(0, name)
            extension.set(ext)
        else:  # user cancel the file browser window
            print("No file chosen")

    def get_current_command(self):
        return self.gui_command_and_params.copy()

    def set_loop(self):
        self.window.mainloop()

    def draw_window(self):
        # window.geometry('1200x600')
        self.window.title("Телефонный справочник")
        menu = Menu(self.window)
        self.draw_menu(menu)
        self.draw_init_screen(self.window)

    def draw_init_screen(self, window):
        header = Label(window,
                       text="  Выбери в меню, что нужно сделать",
                       font=(self._font, 20),
                       height=2)
        header.pack(anchor="center", ipadx=20, ipady=20)

    def draw_menu(self, menu):
        first_item = Menu(menu, tearoff=0)
        second_item = Menu(menu, tearoff=0)

        first_item.add_command(label='Запись', command=lambda: self.gui_create(self.w_ask))
        first_item.add_command(label='Поиск', command=lambda: self.gui_search(self.w_ask))
        first_item.add_command(label='Изменение', command=lambda: self.gui_update(self.w_ask))
        first_item.add_command(label='Удаление', command=lambda: self.gui_delete(self.w_ask))
        first_item.add_command(label='Экспорт', command=lambda: self.gui_export(self.w_ask))
        first_item.add_command(label='Импорт', command=lambda: self.gui_import(self.w_ask))
        first_item.add_command(label='Выход', command=lambda: self.gui_quit())

        second_item.add_command(label='Авторы', command=self.draw_authors)

        menu.add_cascade(label='Меню', menu=first_item)
        menu.add_cascade(label='Авторы', menu=second_item)
        self.window.config(menu=menu)

    def set_command_and_params(self, w_ask, command, *params):
        self.gui_command_and_params = [command, ] + list(params)
        w_ask.destroy()
        self.window.quit()

    def draw_authors(self):
        messagebox.showinfo(title='Authors', message='Николай Беляев\n'
                                                     'Илья Самойлов\n'
                                                     'Сергей Маврин\n\nhave fun')
