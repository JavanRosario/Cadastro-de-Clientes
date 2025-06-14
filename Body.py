import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl
import xlrd
import pathlib
from openpyxl import workbook

# Define tema e aparência
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.appearence()
        self.all_system()

    def layout_config(self):
        self.title('Sistema de Gestão de Clientes')
        self.geometry('700x500')

    def appearence(self):
        # Menu de seleção de tema
        self.layout = ctk.CTkLabel(self, text="Tema", bg_color="transparent", text_color=[
                                   '#000', '#fff']).place(x=50, y=430)
        self.option_teme = ctk.CTkOptionMenu(
            self, values=["Light", "Dark", "System"], command=self.change_teme).place(x=50, y=460)

    def all_system(self):
        # Cabeçalho do sistema
        frame = ctk.CTkFrame(self, width=700, height=70,
                             corner_radius=0, bg_color="teal", fg_color="teal")
        frame.place(x=0, y=0)

        title = ctk.CTkLabel(
            frame, text='Sistema de Gestão de Clientes', font=("Arial", 24), text_color="#fff")
        title.place(x=180, y=20)

        # Texto de instrução
        ctk.CTkLabel(
            self, text='Por favor, preencha todos os campos do formulário', font=("Arial", 16), text_color=["#000", "#fff"]).place(x=50, y=70)

    def change_teme(self, new_appearence):
        ctk.set_appearance_mode(new_appearence)


if __name__ == '__main__':
    app = App()
    app.mainloop()
