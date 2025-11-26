
import tkinter as tk

from PekarnaBrak.setting_frame import SettingStaff
from login import LoginFrame
from staff_menu import StaffMenuFrame
from brak_vavejdane import BrakFrame
from sales import SalesFrame

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BakerBrak")
        self.geometry("1000x600")

        self.current_frame = None
        self.show_login()

    def show_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_login(self):
        self.config(menu=None)
        self.show_frame(LoginFrame)

    def show_staff_menu(self):
        self.show_frame(StaffMenuFrame)

    def show_brak(self):
        self.show_frame(BrakFrame)

    def show_sales(self):
        self.show_frame(SalesFrame)

    def show_setting(self):
        self.show_frame(SettingStaff)






if __name__ == "__main__":
    app = MainApp()
    app.mainloop()






