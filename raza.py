class Razas:
    def __init__(self,raza=""):
        self.raza = raza

    def set_raza(self,raza):
        if type(raza) == str:
            return raza
        
    """ METODOS """

    def add_raza(self):
        raza_existe = False
        with open("razas.txt", "r") as file:
            for linea in file:
                if self.raza.strip() == linea.strip():
                    raza_existe = True
                    print("La raza ya se encuentra en la base de datos...")
                    break
        
        if not raza_existe:
            with open("razas.txt", "a") as file:
                file.write(self.raza + "\n")
                print("La raza fue guardada con éxito...")