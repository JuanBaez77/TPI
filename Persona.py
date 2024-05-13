import csv

class Persona:
    def __init__(self,nombre,apellido,tipoDocumento,documento,telefono,tipoPersona,estado):
        self.nombre = nombre
        self.apellido = apellido
        self.tipoDocumento = tipoDocumento
        self.documento = documento
        self.telefono = telefono
        self.tipoPersona = tipoPersona
        self.estado = estado
    
# METODOS
    @classmethod
    def registrarPersona(cls):
        try:
            nombre = input("¿Cual es el nombre de la persona?\n-->")
            apellido = input("¿El apellido?\n-->")
            tipoDocumento = int(input("tipo de documento \n1. DNI\n2.Pasaporte\n-->"))
            if tipoDocumento == 1:
                tipoDocumento = "DNI"
            else:
                tipoDocumento = "PAS"
            documento = int(input("Numero de documento\n-->"))
            telefono = int(input("Numero de Telefono\n-->"))
            tipoPersona = int(input("¿Que tipo de persona es?\n 1. CLIENTE\n 2. EMPLEADO\n-->"))
            if tipoPersona == 1:
                tipoPersona = "CLI"
            else:
                tipoPersona = "EMP"
            estado = True
            nueva_persona = cls(nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado)
            with open("persona.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    nueva_persona.nombre,
                    nueva_persona.apellido,
                    nueva_persona.tipoDocumento,
                    nueva_persona.documento,
                    nueva_persona.telefono,
                    nueva_persona.tipoPersona,
                    nueva_persona.estado
                ])
            print("Persona registrada con éxito.")
        except ValueError:
            print("Error: introduzca un valor válido.")

    @classmethod
    def mostrarPersonaActiva(cls):
        try:
            print("\tLISTA PERSONAS\t")
            with open("persona.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row[6] == "True":
                        print(f"{row[0]} {row[1]}        DOCUMENTO: {row[3]} \t TELEFONO: {row[4]}")
        except FileNotFoundError:
            print("No se encontró el archivo personas")
    @classmethod
    def mostrarPersona(cls):
        try:
            print("\tLISTA PERSONAS\t")
            with open("persona.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    print(f"{row[0]} {row[1]}        DOCUMENTO: {row[3]} \t TELEFONO: {row[4]}")
        except FileNotFoundError:
            print("No se encontró el archivo personas")
    @classmethod
    def cambiarEstadoPersona(cls):
        documento = input("DOCUMENTO DE LA PERSONA QUE DESEA CAMBIAR\n")
        with open("persona.csv", encoding="UTF-8") as file:
            reader = csv.reader(file)
            next(reader)
            encontrado = 0
            for row in reader:
                if row[3] == documento:
                    print(f"Nombre: {row[0]} {row[2]}")
                    estado_actual = row[-1]
                    if estado_actual == "False":
                        row[-1] = "True"
                        print("Exito al cambiar estado de Inactivo a Activo")                    
                    else:
                        row[-1] = "False"
                        print("Exito al cambiar estado de Activo a Inactivo")    
                    encontrado = 1
            if encontrado == 0:
                print("Error. Documento no encontrado")