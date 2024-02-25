import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        # numero = 1
        # variable_sumando= 0

        # while numero <= 10 :
        #     if numero % 2 == 0 :
        #         variable_sumando += variable_sumando
        #     numero = numero + 1
        # alert ("UTN", f"La suma del 1 al 10 de numeros pares es {variable_sumando}")
        '''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''



        bandera = True

        while bandera == True: 

            nombre = input("Ingrese", "Ingrese su nombre: ")
            edad = input("Ingresar", "Ingrese su edad: ")
            edad = int(edad)
            while edad < 18:
                edad = input ("Reingrese", "Reingrese su edad: ")
                edad = int(edad)

            genero = input ("Ingreso", "Ingrese su genero: ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input ("Ingreso", "Ingrese su genero: ")

            tecnologia = input ("Ingreso", "Ingrese tecnologia: ")
            while tecnologia != "IA" and tecnologia != "IOT" and tecnologia != "RV/RA":
                tecnologia = input ("Ingreso", "Ingrese tecnologia: ")

            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()