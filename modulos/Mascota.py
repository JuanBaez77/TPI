import csv
import Raza
import Persona

listaMascotas = []
listaRaza = []

class Mascota:
    def _init_(self, nombre, raza, propietario, estado):
        self.__nombre = nombre
        self.__raza = raza
        self.__propietario = propietario
        self.__estado = estado

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    def get_propietario(self):
        return self.__propietario

    def get_estado(self):
        return self.__estado

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_raza(self, raza):
        self.__raza = raza

    def set_propietario(self, propietario):
        self.__propietario = propietario

    def set_estado(self, estado):
        self.__estado = estado
        
    def _str_(self):
        return f"{self.get_nombre()},{self.get_raza()},{self.get_propietario()},{self.get_estado()}"

def cargarRazas():
    listaRaza = {}
    with open("TPI/razas.csv", mode='r', encoding="UTF-8", newline="") as archivo:
        lector = csv.reader(archivo)
        for id_raza, estado in lector:
            listaRaza[int(estado)] = id_raza
    return listaRaza

def cargarMascotas():
    listaMascotas = []
    with open("TPI/mascota.csv", mode='r', encoding="UTF-8", newline="") as archivo:
        lector = csv.reader(archivo)
        for linea in lector:
            nombre = linea[0]
            raza = linea[1]
            propietario = linea[2]
            estado = int(linea[3])
            mascota = Mascota(nombre, raza, propietario, estado)
            listaMascotas.append(mascota)
    return listaMascotas

def mostrarMascotas():
    listaRaza = cargarRazas()
    listaMascotas = cargarMascotas()
    #mostrar por pantalla las mascotas activas almacenadas en el csv
    
    print("\n🐶 Mascotas Activas 🐶\n")
    for mascota in listaMascotas:
        if mascota.get_estado() == 1:
            raza_nombre = listaRaza.get(mascota.get_raza(), "Raza desconocida")
            print(f"Nombre: {mascota.get_nombre()}\nRaza: {raza_nombre}\nPropietario: {mascota.get_propietario()}\n\n")

def crearMascota():
    
    #Permitir al usuario añadir una raza al csv
    
    nombre = input("Ingrese el nombre de la mascota --> ")
    raza = input("Ingrese la raza de su mascota --> ")
    propietario = input("Ingrese el nombre del propietario --> ")
    estado = 1
    mascota = Mascota(nombre,raza,propietario,estado)

    with open("TPI/mascota.csv", mode='a', newline='') as archivo:
        linea = csv.writer(archivo)
        linea.writerow([mascota.get_nombre(), mascota.get_raza(), mascota.get_propietario(), mascota.get_estado()])

    print(f"{nombre} ya esta almacenado en mascota.csv")