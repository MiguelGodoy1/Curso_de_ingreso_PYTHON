import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        contador = 0
        contador_positivos = 0
        contador_negativos = 0

        while True : 
            numeros = prompt("UTN", "Ingrese numeros: ")
            if numeros == None:
                break

            numeros = int(numeros)

            
                

            if numeros > 0:
                suma_positivos = suma_positivos + numeros
                contador_positivos +=1
                

            elif numeros < 0:
                suma_negativos = suma_negativos + numeros
                contador_negativos +=1
            
            else :
                contador += 1 
        diferencia = suma_negativos - suma_positivos
        if diferencia < 0 :
                diferencia *= -1
        resultado = (f"La suma acumulada de los numeros negativos es {suma_negativos}"       
        f"\nLa suma acumulada de los numeros positivos es {suma_positivos}"
        f"\nLa cantidad de numeros positivos ingresados es {contador_positivos}"
        f"\nLa cantidad de numeros negativos ingresados es {contador_negativos}"
        f"\nLa cantidad de ceros ingresados es {contador}"
        f"\nLa diferencia entre la cantidad de numeros positivos y negativos es {diferencia}")


        alert ("Utn", resultado)



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
