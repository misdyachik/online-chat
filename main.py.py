

from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.is_menu = False
        self.menu_animation = 5
        self.geometry("500x400")
        self.title("LogiTalk")
        '''MENU'''
        self.menu_frame = CTkFrame(self, fg_color="#8abbff", width=150, height=400)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)
        #self.name_lbl = CTkLabel(self, text="Введіть ім'я", font=("helvetica", 20, "bold"))
        self.btn_menu = CTkButton(self.menu_frame, text="<", font=("helvetica", 20, "bold"))
        self.btn_menu.place(x=0, y=0, relwidth=1)
    def show_menu(self):
        self.menu_frame.configure(width=self.menu_frame.winfo_width(), + self.menu_animation)
        if self.is_menu and not self.menu_frame.winfo_width() >= 200:
            self.after(ms: 10, func: self.show_menu)
        elif not self.is_menu and self.menu_frame.winfo_width() >= 30:
            self.after(ms: 10, func: self.show_menu)
    def toggle_menu(self):
        if self.is_menu = False
            self.menu_animation *= -1
            self.btn_menu.configure(text = ">")
            self.show_menu()
        else:
            self.is_menu = True
            self.menu_animation *= -1
            self.btn_menu.configure(text = ">")
            self.show_menu()
            self.name_lbl = CTkLabel(self.menu_frame, text="Введіть ім'я", font("Helvetica", 20, bold))
            self.name_entry = CTkEntry(self.menu_frame, width=100, placeholder_text="Введіть ім'я")
            self.name_lbl.pack(pady=40)
            self.name_entry.pack()

app = App()
app.mainloop()
