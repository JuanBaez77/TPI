class Diagnostico:
    def __init__(self, nombre, diagnostico, propietario, estado):
        self.__nombre = nombre
        self.__diagnostico = diagnostico
        self.__propietario = propietario
        self.__estado = estado

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_diagnostico(self):
        return self.__diagnostico

    def get_propietario(self):
        return self.__propietario

    def get_estado(self):
        return self.__estado

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_diagnosticos(self, diagnostico):
        self.__diagnostico = diagnostico

    def set_propietario(self, propietario):
        self.__propietario = propietario 

    def set_estado(self, estado):
        self.__estado = estado


    # String representation
    def __str__(self):
        return f"{self.get_nombre()},{self.get_diagnostico()},{self.get_propietario()},{self.get_estado()}"

    def __repr__(self):
        return f"{self.get_nombre()},{self.get_diagnostico()},{self.get_propietario()},{self.get_estado()}"