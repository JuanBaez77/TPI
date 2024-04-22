import csv

class Persona:
    def __init__(self,nombre,apellido,tipoDocumento,documento,telefono,estado):
        self.__nombre = nombre
        self.__apellido = apellido
        self.tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__telefono = telefono
        self.__estado = estado
    
# METODOS
    def registrarPersona(nombre,apellido,tipoDocumento,documento,telefono,estado):
        pass

    def eliminarPersona(nombre,apellido,estado):
        pass

    def mostrarPersona():
        print("\tLISTA PERSONAS\t")
        with open("persona.csv", encoding="UTF-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[5]) ==1:
                    print(f"{row[0]} {row[1]}        DOCUMENTO: {row[3]} \t")