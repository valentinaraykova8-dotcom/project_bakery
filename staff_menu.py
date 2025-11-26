import tkinter as tk
from statistics import kde_random


class StaffMenuFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.create_menu_bar()
        self.create_ui()


    def create_menu_bar(self):
        self.parent.config(menu=None)
        menu_bar = tk.Menu(self.parent)
        self.parent.config(menu=menu_bar)

        options_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="⋮", menu=options_menu)


        options_menu.add_command(label="Назад", command=self.go_back)
        help_menu=tk.Menu(options_menu, tearoff=False)
        options_menu.add_cascade(label="Помощ", menu=help_menu)
        help_menu.add_command(label="Email: bakerbrak@gmail.com")
        help_menu.add_command(label="Телефон 087 874 7054")
        help_menu.add_command(label="Чести грешки : BakerBrakSava")
        options_menu.add_separator()
        options_menu.add_command(label="Изход", command=self.exit_app)





    def create_ui(self):
        frame_center = tk.Label(self)
        frame_center.pack(expand=True)



        button_brak = tk.Button(frame_center,text = "Брак", bd=2, relief="groove", padx=30, pady=30, command=self.open_brak)
        button_brak.grid(row=0, column=0, padx=40, pady=20)
        button_sales = tk.Button(frame_center,text = "Продажби", bd=2, relief="groove", padx=30, pady=30)
        button_sales.grid(row=0, column=1, padx=40, pady=20)








    def go_back(self):
        self.parent.config(menu=tk.Menu(self.parent))
        self.parent.show_login()



    def open_help(self):
        help_window = tk.Toplevel(self)
        tk.Label(help_window, text="Email: bakwebrak@gmail.com").pack(pady=5)
        tk.Label(help_window, text=" Тел: 087 874 7054"). pack(pady=5)

    def exit_app(self):
        self.parent.destroy()

    def open_brak(self):
        from brak_vavejdane import BrakFrame
        self.parent.show_brak()

    def open_sales(self):
        from sales import SalesFrame
        self.parent.show_sales()




