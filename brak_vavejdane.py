import tkinter as tk
from  tkinter import ttk
class BrakFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.create_menu_bar()

        with open("produkti.txt", "r", encoding = "utf-8") as file:
            products = [line.strip() for line in file.readlines() if line.strip()]

        header = tk.Frame(self, bg="#ffffff")
        header.pack(side="top", fill="x", pady=5)
        frame_table = tk.Frame(self, bg="#f4f4f4", width=450, height=400)
        frame_table.pack(side="left", fill = "both", expand = True)

        frame_form = tk.Frame(self, bg="#ffffff", width=450, height=400)
        frame_form.pack(side="right", fill="both", expand=True)

        form_inner = tk.Frame(frame_form, bg="#ffffff")
        form_inner.pack(expand=True)  # тази команда я центрира вертикално и хоризонтално

        label_art = tk.Label(form_inner, text="Въведи артикул:")
        label_art.pack(pady=5)

        entry_art = tk.Entry(form_inner, width=30, justify="center")
        entry_art.pack(pady=5)
        entry_art.bind("<Return>", lambda event: entry_qty.focus())

        listbox = tk.Listbox(form_inner, width=30, height=6)
        listbox.pack_forget()

        label_qty = tk.Label(form_inner, text="Въведи количество:")
        label_qty.pack(pady=5)

        entry_qty = tk.Entry(form_inner, width=15, justify="center")
        entry_qty.pack(pady=5)
        entry_qty.bind("<Return>", lambda event: entry_reason.focus())

        label_reason = tk.Label(form_inner, text="Причина (по желание):")
        label_reason.pack(pady=5)

        entry_reason = tk.Entry(form_inner, width=30, justify="center")
        entry_reason.pack(pady=5)
        entry_qty.bind("<Return>", lambda event:entry_reason.focus())
        entry_reason.bind("<Return>", lambda event: add_item())

        added_items = []
        def add_item():
            art = entry_art.get()
            qty = entry_qty.get()
            reason = entry_reason.get()
            if not art or not qty:
                return

            new_row=table.insert("", "end",  values=(art, qty, reason if reason else "-"))

            added_items.append({ "art": art, "qty": qty, "reason": reason if reason else "" })

            table.tag_configure("added_row", background="#555555", foreground="white")
            table.item(new_row, tags=("added_row",))
            button_add.config(bg="#555555", fg="white")


            print(f"Добавено: {art} - {qty}")

        def delete_row(event):

            selected = table.selection()
            if not selected:
                return
            row_id = selected[0]
            values = table.item(row_id, "values")
            art, qty,reason = values
            table.delete(row_id)
            for item in added_items:
                if item["art" ] == art and item["qty"] == qty and item["reason"] == reason:
                    added_items.remove(item)
                    break


            def reset_visuals():
                table.tag_configure("added_row", background="", foreground="")
                button_add.config(bg="SystemButtonFace", fg="black")

            self.after(400, reset_visuals)
            entry_art.delete(0, tk.END)
            entry_qty.delete(0, tk.END)
            entry_reason.delete(0, tk.END)
            entry_art.focus()
        def search_table(event):
            query = search_entry.get().lower()
            for row in table.get_children():
                table.delete(row)
            if not query:
                for item in added_items:
                    table.insert("", "end", values=(item ["art"], item["qty"], item["reason"]))

                return
            results = [
                item for item in added_items
                if query in item["art"].lower()
                or query in item["qty"].lower()
                or query in item["reason"].lower()
            ]
            for item in results:
                table.insert("", "end", values=(item["art"], item["qty"], item["reason"]))

        def update_suggestions(event):
            typed_text = entry_art.get().lower()
            print("Търси:",typed_text)
            print("Намерени:", [p for p in products if typed_text in p.lower()])


            listbox.delete(0, tk.END)
            if not typed_text:
                listbox.pack_forget()
                return

            matches = [p for p in products if typed_text in p.lower()]
            print("Съвпадение")
            if matches :
                if not listbox.winfo_ismapped():
                    listbox.pack(pady=10, after = entry_art)
                listbox.config(height=min(6, len(matches)))
                for item in matches:
                    listbox.insert(tk.END, item)
            else:
                listbox.pack_forget



                for item in matches:
                    listbox.insert(tk.END,item)

        def confirm_selection(idx=None):
            if idx is None:
                sel = listbox.curselection()
                if not sel:
                    return
                idx = sel[0]
            selected_item = listbox.get(idx)
            entry_art.delete(0, tk.END)
            entry_art.insert(0, selected_item)

            listbox.delete(0, tk.END)
            listbox.pack_forget()
            entry_art.focus_set()

        def focus_listbox_start(event):
            if listbox.size()>0:
                listbox.focus_set()
                listbox.selection_clear(0, tk.END)
                listbox.selection_set(0)
                listbox.activate(tk.END)
            return "break"
        entry_art.bind("<Down>", focus_listbox_start)

        def listbox_nav_up(event):
            sel = listbox.curselection()
            if sel and sel[0] == 0:
                entry_art.focus_set()
                return "break"

        listbox.bind("<Up>", listbox_nav_up)

        def listbox_return(event):
            confirm_selection()
            return "break"

        listbox.bind("<Return>", lambda event: confirm_selection())
        def on_listbox_click(event):
            idx = listbox.nearest(event.y)
            confirm_selection(idx)

            listbox.bind("<ButtonRelease-1>", lambda event: confirm_selection(listbox.nearest(event.y)))

        entry_art.bind("<KeyRelease>",update_suggestions)

        label_search = tk.Label(frame_table, text="Търсене", bg = "#f4f4f4",font=("Ariel", 11))
        label_search.pack(anchor="w" , padx=10)
        search_entry = tk.Entry(frame_table, width=30)
        search_entry.pack(anchor="w" , padx=10, pady=10)
        search_entry.bind("<KeyRelease>", search_table)

        def save_edit(event):
            new_value = edit_entry.get()
            if editing_col == "#2":
                try:
                    float(new_value)
                except ValueError:
                    return False

            table.set(editing_row, editing_col, new_value)
            edit_entry.destroy()
            entry_art.focus_set()
            table.set(editing_row, editing_col, new_value)
            edit_entry.destroy()
            entry_art.focus_set()
            return True

        def cancel_edit(event):
                edit_entry.destroy()
                table.focus(editing_row)
                table.selection_set(editing_row)

        def go_next_cell(event):
            global edit_entry, editing_row, editing_col


            new_value = edit_entry.get()
            if editing_col == "#2":
                try:
                    float(new_value)
                except ValueError:
                    return
            table.set(editing_row, editing_col, new_value)
            edit_entry.destroy()
            if editing_col == "#1":
                next_col = "#2"
            elif editing_col == "#2":
                next_col = "#3"
            else:
                entry_art.focus_set()
                return
            x, y, width, height = table.bbox(editing_row, next_col)
            old_value = table.set(editing_row, next_col)
            editing_col = next_col
            edit_entry = tk.Entry(table)
            edit_entry.place(x=x, y=y, width=width, height=height)
            edit_entry.insert(0, old_value)
            edit_entry.focus()
            edit_entry.select_range(0, tk.END)
            edit_entry.bind("<Escape>", cancel_edit)
            edit_entry.bind("<Return>", save_edit)
            edit_entry.bind("<space>", go_next_cell)
        def start_edit_cell(event):
            global edit_entry, editing_row, editing_col

            row_id = table.identify_row(event.y)
            col_id = table.identify_column(event.x)
            if "edit_entry" in globals() and edit_entry.winfo_exists():
                old_col = editing_col
                result = save_edit(event)
                if editing_col == old_col:
                    pass
                else:
                    return



            if not row_id or not col_id :
                return
            x,y, width, height = table.bbox (row_id, col_id)
            old_value = table.set(row_id, col_id)


            editing_row = row_id
            editing_col = col_id


            edit_entry = tk.Entry(table)
            edit_entry.place(x=x, y=y,width = width, height=height)
            edit_entry.insert(0, old_value)
            edit_entry.focus()
            edit_entry.select_range(0, tk.END)

            edit_entry.bind("<Escape>", cancel_edit)
            edit_entry.bind("<Return>", save_edit)
            edit_entry.bind("<space>", go_next_cell)
        columns = ("Артикул", "Количество", "Причина")

        table = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)
        table.heading("Артикул", text = "Артикул")
        table.heading("Количество", text = "Количество")
        table.heading("Причина", text = "Причина")

        table.column("Артикул", anchor="w", width=200)
        table.column("Количество", anchor="center", width=100)
        table.column("Причина", anchor="center", width=150)

        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        table.pack(fill="both", expand=True, padx=10, pady=10)
        table.bind("<Key>", delete_row)
        table.bind("<Button-1>", lambda e: table.focus_set())
        table.bind("<Double-1>", start_edit_cell)

    def create_menu_bar(self):
        self.parent.config(menu= None)
        menu_bar = tk.Menu(self.parent)
        self.parent.config(menu=menu_bar)

        options_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label = ":", menu = options_menu)

        options_menu.add_command (label = "Назад", command = self.go_back)
        options_menu.add_separator()
        options_menu.add_command(label = "Изход", command = self.exit_app)
        options_menu.add_separator()
        options_menu.add_command(label = "Настройки", command = self.open_setting_brak)

    def go_back(self):
        self.parent.show_staff_menu()

    def exit_app(self):
        self.parent.destroy()

    def open_setting_brak(self):
        from setting_frame import SettingStaff
        self.parent.show_setting()













