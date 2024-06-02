class Mascota:
    def __init__(self, nombre, raza, propietario, estado):
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
        
    def __str__(self):
        return f"{self.get_nombre()},{self.get_raza()},{self.get_propietario()},{self.get_estado()}"

    def __repr__(self) -> str:
        return f"{self.get_nombre()},{self.get_raza()},{self.get_propietario()},{self.get_estado()}"