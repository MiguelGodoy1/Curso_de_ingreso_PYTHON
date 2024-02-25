import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_02
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números DESCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = 5
        for i in range (0, 5):
            alert ("Mensaje", numero)
            numero -= 1
        # numero = 6
        # for i in range (0,5):
        #     numero -= 1
        #     alert ("Mensaje", numero)
       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()