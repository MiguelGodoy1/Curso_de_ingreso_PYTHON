import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        bandera = True
        seguir = True
        contador = 0
        suma_edades = 0
        suma_votos= 0
        while True:
            nombre= prompt ("Datos", "Ingrese su nombre: ")
            while nombre == None or nombre == "":
                nombre = prompt ("Error", "Reingrese su nombre: ")
            
            edad = prompt("Datos", "Ingrese su edad: ")
            while (edad == None or edad == "") or int(edad) < 25 :
                edad =  prompt ("Error", "Reingrese su edad: ")

            edad = int(edad)
            contador +=1
            suma_edades += edad


            cant_votos = prompt ("Datos", "Ingrese la cantidad de votos: ")
            while cant_votos == None or cant_votos == 0 :
                cant_votos = prompt ("Error", "Reingrese la cantidad de votos")
            cant_votos = int(cant_votos)
            suma_votos += cant_votos

            if bandera == True or cant_votos > cant_votos_mayor:
                cant_votos_mayor = cant_votos
                nombre_mas_votos = nombre

            if bandera == True or cant_votos < cant_votos_menor:
                cant_votos_menor = cant_votos
                
                nombre_menos_votado = nombre
            bandera = False

            seguir = question ("Pregunta", "¿Desea seguir?")

            promedio = suma_edades / contador
            if seguir == False or seguir == None:
                break    
        
        alert ("Mensaje", f"El candidato con mayor votos es {nombre_mas_votos}"
            f"\nEl candidato {nombre_menos_votado}, tiene menos votos"
            f"\nEl promedio de edad de los candidatos es {promedio}"
            f"\nLa cantidad de votos emitidos fue {suma_votos}")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
