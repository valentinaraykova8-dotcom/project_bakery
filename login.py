import tkinter as tk

class LoginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        header = tk.Frame(self, bg="#ffffff")
        header.pack(side="top", fill="x", pady=10)
        exit_button = tk.Button(
            header,
            text="⏻",
            fg="#e74c3c",
            bg="#ffffff",
            bd=0,
            font=("Ariel", 14, "bold"),
            command=self.exit_app
        )

        exit_button.pack(side="left", padx=10)

        footer = tk.Frame(self)
        footer.pack(side="bottom", pady=20)
        label_phone_left= tk.Label(footer, text="Телефон", fg="grey", font=("Arial", 9))
        label_phone_left.grid(row=1, column=0, sticky="w", padx=5)
        label_phone_right= tk.Label(footer, text="087 874 7054", fg="black", font=("Arial", 9))
        label_phone_right.grid(row=1, column=1, sticky="w", padx=5)

        label_email_left = tk.Label(footer, text="Email", fg="grey", font=("Arial", 9))
        label_email_left.grid(row=2, column=0, sticky="w", padx=5)
        label_email_right = tk.Label(footer, text="bakerbrak@gmail.com",fg="black", font=("Arial", 9))
        label_email_right.grid(row=2, column=1, sticky="w", padx=5)

        label_error_often_left = tk.Label(footer, text="Често допускани грешки", fg="grey", font=("Arial", 9))
        label_error_often_left.grid(row=3, column=0, sticky="w", padx=5)
        label_error_often_right = tk.Label(footer, text="bakerbrakSava", fg="black", font=("Arial", 9))
        label_error_often_right.grid(row=3, column=1, sticky="w", padx=5)


        self.entry_code = tk.Entry(self, width=60, justify="center")
        self.entry_code.insert(0, "Въведи парола")
        self.entry_code.pack(expand=True, pady=20)
        print(self.entry_code.get())

        self.button = tk.Button(self, text="Вход" , command=self.on_logic_click)
        self.button.pack(expand=True, pady=20)

        self.entry_code.bind("<FocusIn>", self.clear_placeholder)
        self.entry_code.bind("<FocusOut>", self.add_placeholder)
        self.entry_code.bind("<Return>",lambda event:self.on_logic_click())





    def exit_app(self):
        self.parent.destroy()


    def on_logic_click(self):

        password = self.entry_code.get()
        ADMIN_PASS = "admin"
        STAFF_PASS = "1"


        if password == "admin":
            print("Вход като админ")
        elif password == "1":
            self.parent.show_staff_menu()
            print("Вход като персонал")

        else:
            print("Грешна парола")
    def clear_placeholder(self, event):
        if  self.entry_code.get() == "Въведи парола":
                self.entry_code.delete(0, tk.END)
                self.entry_code.config(fg="black")
    def add_placeholder(self, event):
        if self.entry_code.get() == "":

            self.entry_code.insert(0, "Въведи парола")
            self.entry_code.config(fg="gray")

































