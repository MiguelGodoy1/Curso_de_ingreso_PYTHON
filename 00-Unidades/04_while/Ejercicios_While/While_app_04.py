import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_04
---
Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
        validacion = int(prompt ("UTN", "ingrese un numero entre el 0 y el 9 :"))

        while validacion < 0 or validacion > 9 :
            alert ("UTN", "ingrese otro numero")
            validacion = prompt ("UTN", "ingrese un numero entre el 0 y el 9 :")
            validacion = int(validacion)

        alert ("UTN", "Fin")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()