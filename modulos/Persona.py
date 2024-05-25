import csv
class Persona:
    def __init__(self,nombre,apellido,tipoDocumento,documento,telefono,tipoPersona,estado):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__telefono = telefono
        self.__tipoPersona = tipoPersona
        self.__estado = estado

    # Getter y setter 
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre


    def getApellido(self):
        return self.__apellido
    def setApellido(self, apellido):
        self.__apellido = apellido


    def getTipoDocumento(self):
        return self.__tipoDocumento
    def setTipoDocumento(self, tipoDocumento):
        self.__tipoDocumento = tipoDocumento


    def getDocumento(self):
        return self.__documento
    def setDocumento(self, documento):
        self.__documento = documento


    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono


    def getTipoPersona(self):
        return self.__tipoPersona
    def setTipoPersona(self, tipoPersona):
        self.__tipoPersona = tipoPersona


    def getEstado(self):
        return self.__estado
    def setEstado(self, estado):
        self.__estado = estado

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
            with open("csv/persona.csv", "a", newline="") as file:
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
            with open("csv/persona.csv", encoding="UTF-8") as file:
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
            with open("csv/persona.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    print(f"{row[0]} {row[1]}        DOCUMENTO: {row[3]} \t TELEFONO: {row[4]}")
        except FileNotFoundError:
            print("No se encontró el archivo personas")
    @classmethod
    def cambiarEstadoPersona(cls):
        documento = input("DOCUMENTO DE LA PERSONA QUE DESEA CAMBIAR\n")
        personas = []
        encontrado = False
        with open("csv/persona.csv", encoding="UTF-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[3] == documento:
                    print(f"Nombre: {row[0]} {row[1]}")
                    estado_actual = row[6]
                    if estado_actual == "False":
                        row[6] = "True"
                        print("Exito al cambiar estado de Inactivo a Activo")                    
                    else:
                        row[6] = "False"
                        print("Exito al cambiar estado de Activo a Inactivo")    
                    encontrado = True
                personas.append(row)
            if encontrado == False:
                print("Error. Documento no encontrado")
            else:
                with open("csv/persona.csv", "w", newline= "", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(personas)