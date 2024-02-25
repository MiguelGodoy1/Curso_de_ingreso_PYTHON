import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        # contador = 1

        # while contador <= 10 :
        #     alert ("Utn", contador)
        #     contador = contador + 1
        #     #respuesta = question ("UTN", "Desea continuar?")
        #     #if not respuesta :
        #     #  break

        # alert ("Utn", "Fin")

#         UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
# que promete revolucionar el mercado. 
# Las posibles aplicaciones son las siguientes: 
# # Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 


# Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

# Los datos a ingresar por cada encuestado son:
#     * nombre del empleado
#     * edad (no menor a 18)
#     * genero (Masculino - Femenino - Otro)
#     * tecnologia (IA, RV/RA, IOT)   

# En esta opción, se ingresaran empleados hasta que el usuario lo desee.

# Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

            contador_masc_tecnologia = 0
            contador_masculino = 0
            contador_femenino = 0
            contador_otro = 0
            contador_IA = 0
            contador_IOT = 0
            contador_RV_RA = 0
            contador_IOT_rango = 0
            seguir = True

            while seguir == True: 
                nombre = input("Ingrese su nombre: ")
                


                edad = input("Ingrese su edad: ")
                edad = int(edad)
                while edad < 18:
                    edad = input ("Reingrese su edad: ")
                    edad = int(edad)
            #!X 3) - Porcentaje de empleados por cada genero
                genero = input ("Ingrese su genero: ")
                while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                    genero = input ("Reingrese su genero: ")
                    match genero :
                        case "Masculino":
                            contador_masculino += 1
            #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
                            if (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
                                contador_masc_tecnologia += 1

                        case "Femenino":
                            contador_femenino += 1
                        case "Otro":
                            contador_otro += 1
                tecnologia = input ("Ingrese tecnologia: ")
                while tecnologia != "IA" and tecnologia != "IOT" and tecnologia != "RV/RA":
                    tecnologia = input ("Reingrese tecnologia: ")

                
                if tecnologia == "IA":
                    contador_IA += 1
                else: 
                    if tecnologia == "IOT":
                        contador_IOT += 1
                        if (edad >=18 and edad <= 25) or (edad >=33 and edad <=42):
                            contador_IOT_rango += 1
                    else :
                        contador_RV_RA += 1
                        
                        
                seguir = question ("Continuar", "Desea continuar? ")
            #contador de tecnologia
            if contador_IOT > contador_RV_RA and contador_IOT > contador_IA:
                tecnologia_votada = "IOT"
            elif contador_IA > contador_RV_RA:
                tecnologia_votada = "IA"
            else :
                tecnologia_votada = "RV/RA"

            #porcentaje
            total_empleados = contador_otro + contador_femenino + contador_masculino
            porcentaje_femenino = (contador_femenino * 100)/ total_empleados
            porcentaje_masculino = (contador_masculino * 100 )/ total_empleados
            porcentaje_otro = (contador_otro * 100)/ total_empleados
            #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre
            #18 y 25 o entre 33 y 42.  
            porcentaje_IOT_rango = (contador_IOT_rango * 100) / total_empleados
            
            print (f"Cantidad de masculinos IOT/IA en rango de edad de 25 y 50 es {contador_masc_tecnologia}.")
            print (f"La tecnologia mas votada fue {tecnologia_votada}.")
            print (f"`{porcentaje_femenino}, {porcentaje_masculino}, {porcentaje_otro}")
            print (f"{porcentaje_IOT_rango}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()