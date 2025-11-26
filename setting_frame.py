import tkinter as tk
from  tkinter import ttk
class SettingStaff (tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_menu_bar()
        header = tk.Frame(self, bg="#ffffff")
        header.pack(side="top", fill="x", pady=5)

        self.left_panel = tk.Frame(self, bg="#f0f0f0", width=200)
        self.left_panel.pack(side="left", fill="y")

        self.btn_general = tk.Button(
            self.left_panel,
            text="Общи",
            anchor="w",
            command=self.show_general

        )
        self.btn_general.pack(padx=10, pady=(20, 5), fill="x")

        self.btn_setting = tk.Button(
            self.left_panel,
            text = "Продукти",
            anchor = "w",
            command = self.show_products_staff
        )
        self.btn_setting.pack(padx=10, pady=5, fill="x")

        self.btn_files_staff = tk.Button(
        self.left_panel,
        text = "Управление на файлове",
        anchor = "w",
        command = self.show_files_staff
        )
        self.btn_files_staff.pack(fill="x", padx=10, pady=5)

        self.content_panel = tk.Frame(self, bg = "#ffffff")
        self.content_panel.pack(fill="both", side="right", expand=True)


    def show_general(self):
        for widget in self.content_panel.winfo_children():
            widget.destroy()

        label = tk.Label(self.content_panel, text = "Общи", font = ("Arial", 14))
        label.pack(pady=20)

    def show_products_staff(self):
        for widget in self.content_panel.winfo_children():
            widget.destroy()

        label = tk.Label(self.content_panel, text = "Продукти", font = ("Arial", 14))
        label.pack(pady=20)
        manage_btn = tk.Button(self.content_panel,text = "Менажиране на артикули",command = self.open_manage_products)
        manage_btn.pack(pady=10)





    def show_files_staff(self):
        for widget in self.content_panel.winfo_children():
            widget.destroy()

            label = tk.Label(self.content_panel, text = "Управление на файлове", font = ("Arial", 14))
            label.pack(pady=20)

    def create_menu_bar(self):
            self.parent.config(menu=None)
            menu_bar = tk.Menu(self.parent)
            self.parent.config(menu=menu_bar)

            options_menu = tk.Menu(menu_bar, tearoff=False)
            menu_bar.add_cascade(label=":", menu=options_menu)

            options_menu.add_command(label = "Назад", command = self.go_back_brak)

    def go_back_brak(self):
        self.parent.show_brak()

    def open_manage_products(self):
        from manage_product_setting import ManageProductSetting
        ManageProductSetting(self)

