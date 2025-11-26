import tkinter as tk
from itertools import product


class ManageProductSetting(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Менажиране на продукти")
        self.geometry("500x350")
        with open("produkti.txt", "r", encoding="utf-8") as f:
            self.products = [line.strip().split(",")[0] for line in f.readlines()]


        # 🔹 Главен контейнер
        add_frame = tk.Frame(self, bg="#f9f9f9")
        add_frame.pack(fill="both", expand=True)


        # 🔹 Секция "Добави продукт"
        content_frame = tk.Frame(add_frame, bg="#f9f9f9")
        content_frame.pack(fill="x", pady=(10, 0))

        tk.Label(content_frame, text="Име на артикул:", bg="#f9f9f9").pack(anchor="w", padx=10)
        self.entry_name = tk.Entry(content_frame, width=40)
        self.entry_name.pack(anchor="w", padx=10, pady=5)



        # 🔹 Съобщения под първия модул
        self.label_message = tk.Label(add_frame, text="", fg="red", bg="#f9f9f9")
        self.label_message.pack(pady=(5, 0))

        # 🔹 Бутони само за "Добави"
        buttons_row = tk.Frame(add_frame, bg="#f9f9f9")
        buttons_row.pack(fill="x", pady=(10, 10))

        btn_save = tk.Button(
            buttons_row,
            text="Запази",
            command=self.save_new_product,
            width=10
        )
        btn_save.pack(side="right", padx=(0, 10), pady=5)

        btn_cancel = tk.Button(buttons_row, text="Откажи", command=self.cancel_add, width=10)
        btn_cancel.pack(side="right", padx=(0, 10), pady=5)

        # 🔹 Разделител между модулите
        separator = tk.Frame(add_frame, height=2, bg="#d9d9d9")
        separator.pack(fill="x", pady=(5, 10))

        # 🔹 Втори модул – "Редактирай"
        edit_frame = tk.Frame(add_frame, bg="#f9f9f9")
        edit_frame.pack(fill="both", expand=True)


        tk.Label(edit_frame, text="Редактирай", font=("Arial", 12, "bold"), bg="#f9f9f9").pack(anchor="w", padx=10, pady=(0, 5))

        tk.Label(edit_frame, text = "Потърси артикул: ", bg="#f9f9f9").pack(anchor="w")




        self.entry_art_edit = tk.Entry(edit_frame, width=40)
        self.entry_art_edit.pack(anchor="w", padx=10, pady=5)
        buttons_row = tk.Frame(add_frame, bg="#f9f9f9")
        buttons_row.pack(fill="x", pady=(10, 10))

        self.entry_art_edit.bind("<KeyRelease>", lambda event : self.update_suggestions())
        self.suggestions_frame = tk. Frame(edit_frame, bg="#f9f9f9")
        self.suggestions_frame.pack(anchor="w", padx=10, pady=(0, 5))

        self.listbox = tk.Listbox(edit_frame, width=40)
        self.listbox.pack(anchor="w", padx=10, pady = (0,5))
        self.listbox.config(height=0)

        btn_save = tk.Button(
            buttons_row,
            text="Запази",
            command=self.save_new_product,
            width=10
        )
        btn_save.pack(side="right", padx=(0, 10), pady=5)

        btn_cancel = tk.Button(buttons_row, text="Откажи", command=self.cancel_edit, width=10)
        btn_cancel.pack(side="right", padx=(0, 10), pady=5)



        # (тук по-късно ще добавим таблица или полета за редакция)


    def save_new_product(self):
        name = self.entry_name.get().strip()
        price = self.entry_price.get().strip()

        if not name or not price:
            self.show_message_add("Попълни всички полета!", color="red")
            return

        try:
            price = float(price)
        except ValueError:
            self.show_message_add("Невалидна цена!", color="red")
            return

        try:
            with open("produkti.txt", "r", encoding="utf-8") as file:
                products = [line.strip().split(",")[0].lower() for line in file.readlines()]
        except FileNotFoundError:
            products = []

        if name.lower() in products:
            self.show_message_add("⚠️ Артикул с това име вече съществува!", color="red")
            return

        with open("produkti.txt", "r", encoding="utf-8") as file:
            file.write(f"{name},{price}\n")

        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.show_message_add("✅ Артикулът е добавен успешно!", color="green")


    def show_message_add(self, text, color="black"):
        """Показва съобщение и го скрива след 5 секунди."""
        self.label_message.config(text=text, fg=color)
        self.after(5000, lambda: self.label_message.config(text=""))


    def cancel_add(self):
        """Изчиства въведените полета."""
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)

    def cancel_edit(self):
        self. entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)

    def update_suggestions(self):
        typed_text= self.entry_art_edit.get().lower()
        print("update", typed_text)


        self.listbox.delete(0, tk.END)
        if not typed_text:
            self.listbox.pack_forget()
            return

        matches = [p for p in self.products if typed_text in p.lower()]
        print(matches)
        if matches:
            if not self.listbox.winfo_ismapped():
                self.listbox.config(height=min(6,len(matches)))
            for item in matches:
                self.listbox.insert(tk.END, item)
        else:
            self.listbox.config(height=0)








