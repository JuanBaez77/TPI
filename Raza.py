import csv
from tkinter import *
class Raza:
    def __init__(self, raza="", estado=1):
        self.__raza = raza.lower()
        self.__estado = estado
        
    # Getters
    def get_raza(self):
        return self.__raza
    
    def get_estado(self):
        return self.__estado
    
    # Setters
    def set_raza(self,raza):
        self.__raza = raza 
        
    def set_estado(self,estado):
        self.__estado = estado   
        
    def __str__(self):
        return self.__raza    

def menuRaza():
    ventana = Tk()
    ventana.title("Menu Razas")
    ventana.iconbitmap("TPI/img/404022.ico")
    ventana.geometry("300x250")

    Button(ventana, text="Mostrar Razas", command=mostrarRaza).pack(pady=10)
    Button(ventana, text="Agregar Raza", command=crearRaza).pack(pady=10)
    Button(ventana, text="Modificar Estado de Raza", command=modificarEstadoRaza).pack(pady=10)
    Button(ventana, text="Salir", command=ventana.quit).pack(pady=10)

    ventana.mainloop()
    
def mostrarRaza():
    
    #mostrar por pantalla las razas almacenadas en el csv
    
    with open("TPI/razas.csv", "r", encoding="UTF-8", newline="") as lectura:
        razasAlmacenadas = csv.reader(lectura)
        print("\n🐶 Razas Almacenadas🐶\n")
        for linea in razasAlmacenadas:
            print(", ".join(linea))
                
def crearRaza():
    
    #Permitir al usuario añadir una raza al csv
    
    nombre_raza = input("Ingrese el nombre de la raza --> ")
    raza = Raza(nombre_raza)

    with open("TPI/razas.csv", mode='a', newline='') as archivo:
        razaNueva = csv.writer(archivo)
        razaNueva.writerow([raza.get_raza(), "1"])

    print(f"Raza '{raza.get_raza()}' guardada en razas.csv")

def modificarEstadoRaza():
    
    #Permitir al usuario modificar el estado de una raza en el csv
    
    nombreRaza = input("Ingrese el nombre de la raza --> ").lower()
    nuevoEstado = input("Ingrese el nuevo estado\n(0) Deshabilitado\n(1) Habilitado\n--> ")

    while nuevoEstado not in ["0","1"]:
        nuevoEstado = input("Estado inválido. Ingrese (0) Deshabilitado o (1) Habilitado\n--> ")

    encontrado = False
    filas = []


    with open("TPI/razas.csv", "r", encoding="UTF-8", newline="") as archivo:
        contenido = csv.reader(archivo)
        for linea in contenido:
            if linea[0] == nombreRaza:
                linea[1] = nuevoEstado
                encontrado = True
            filas.append(linea)

    if encontrado:
        with open("TPI/razas.csv", "w", encoding="UTF-8", newline="") as archivo:
            estadoActualizado = csv.writer(archivo)
            estadoActualizado.writerows(filas)
        print(f"Estado de la raza {nombreRaza} actualizado a {nuevoEstado}")
    else:
        print(f"La raza {nombreRaza} no se encontró en el archivo.")