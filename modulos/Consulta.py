class Consulta:
    def __init__(self, fecha, nombremascota, diagnostico, veterinario, tratamiento, vacunas, observaciones):
        self.__fecha = fecha
        self.__nombremascota = nombremascota
        self.__diagnostico = diagnostico
        self.__veterinario = veterinario
        self.__tratamiento = tratamiento
        self.__vacunas = vacunas
        self.__observaciones = observaciones

    # Getters
    def get_fecha(self):
        return self.__fecha

    def get_nombremascota(self):
        return self.__nombremascota

    def get_diagnostico(self):
        return self.__diagnostico

    def get_veterinario(self):
        return self.__veterinario

    def get_tratamiento(self):
        return self.__tratamiento

    def get_vacunas(self):
        return self.__vacunas

    def get_observaciones(self):
        return self.__observaciones

    # Setters
    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_nombremascota(self, nombremascota):
        self.__nombremascota = nombremascota

    def set_diagnostico(self, diagnostico):
        self.__diagnostico = diagnostico

    def set_veterinario(self, veterinario):
        self.__veterinario = veterinario

    def set_tratamiento(self, tratamiento):
        self.__tratamiento = tratamiento

    def set_vacunas(self, vacunas):
        self.__vacunas = vacunas

    def set_observaciones(self, observaciones):
        self.__observaciones = observaciones

    def __str__(self):
        return f"{self.get_fecha()},{self.get_nombremascota()},{self.get_diagnostico()},{self.get_veterinario()},{self.get_tratamiento()},{self.get_vacunas()},{self.get_observaciones()}"

    def __repr__(self):
        return f"{self.get_fecha()},{self.get_nombremascota()},{self.get_diagnostico()},{self.get_veterinario()},{self.get_tratamiento()},{self.get_vacunas()},{self.get_observaciones()}"