class Tratamiento:
    def __init__(self, nombre, destino, estado):
        self.__nombre = nombre
        self.__destino = destino
        self.__estado = estado

    #GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_destino(self):
        return self.__destino

    def get_estado(self):
        return self.__estado

    # SETTERS
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_destino(self, destino):
        self.__destino = destino

    def set_estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f"Nombre:{self.nombre},{self.destino}"
    
    def __repr__(self):
        return f"Nombre:{self.nombre},{self.destino}"
        

    def estadoTratamiento(self):
        pass

    def modificarTratamiento(self):
        pass

    def mostrarTratamiento(self):
        pass

    def añadirTratamiento(self):
        pass