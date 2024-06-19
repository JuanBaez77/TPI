class Tratamiento:
    def __init__(self, nombre, descripcion, estado):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__estado = estado

    #GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def get_estado(self):
        return self.__estado

    # SETTERS
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_destino(self, descripcion):
        self.__descripcion = descripcion

    def set_estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f"Nombre:{self.__nombre}, Descripcion:{self.__descripcion}"
    
    def __repr__(self):
        return f"Nombre:{self.__nombre}, Descripcion:{self.__descripcion}"