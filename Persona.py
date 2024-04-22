import csv

class Persona:
    def __init__(self,nombre,apellido,tipoDocumento,documento,telefono,tipoPersona,estado):
        self.__nombre = nombre
        self.__apellido = apellido
        self.tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__telefono = telefono
        self.__tipoPersona = tipoPersona
        self.__estado = estado
    
# METODOS
    def registrarPersona():
        nombre = input("¿Cual es el nombre de la persona?\n-->")
        apellido = input("¿El apellido?\n-->")
        tipoDocumento = int(input("tipo de documento \n1. DNI\n2.Pasaporte\n-->"))
        if tipoDocumento == 1:
            tipoDocumento = "DNI"
        elif tipoDocumento == 2:
            tipoDocumento = "PAS"
        else:
            tipoDocumento = None
        documento = int(input("Numero de documento\n-->"))
        telefono = int(input("Numero de Telefono\n-->"))
        tipoPersona = input("¿Que tipo de persona es?\n 1. CLIENTE\n 2. EMPLEADO\n-->")
        if tipoPersona == 1:
            tipoPersona = "CLI"
        elif tipoPersona == 2:
            tipoPersona = "EMP"
        else:
            tipoPersona = None
        personas = [
            nombre,apellido,tipoDocumento,documento,telefono,tipoPersona,1
        ]
        with open ("persona.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(personas)


    def mostrarPersona():
        print("\tLISTA PERSONAS\t")
        with open("persona.csv", encoding="UTF-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[5]) ==1:
                    print(f"{row[0]} {row[1]}        DOCUMENTO: {row[3]} \t TELEFONO: {row[4]}")