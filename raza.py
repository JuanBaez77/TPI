import csv

class Razas:
    def __init__(self, raza=""):
        self.__raza = raza.lower()
        
    # Getters
    def get_raza(self):
        return self.__raza
    
    # Setters
    def set_raza(self,raza):
        self.__raza = raza

    # Metodos
    def mostrarRaza():
        """
        Este metodo se encarga de mostrar al cliente/usuario las razas que tenemos 
        almacenadas en nuestra base de datos
        
        """
        with open("razas.csv", "r", encoding="UTF-8", newline="") as lectura:
            razasAlmacenadas = csv.reader(lectura)
            print("\n🐶 Razas Almacenadas🐶\n")
            for linea in razasAlmacenadas:
                print(", ".join(linea))
    
    def añadirRaza(self):
        """
        Este metodo permite al usuario agregar razas a la base de datos
        
        """
        razaEncontrada = False
        with open("razas.csv", "r", encoding="UTF-8", newline="") as lectura:
            razasAlmacenadas = csv.reader(lectura)
        for linea in razasAlmacenadas:
            if linea[0].lower() == self.__raza:
                print("La raza ya esta almacenada en la base de datos...")
                razaEncontrada = True
                break
        
        if not razaEncontrada:
            with open("razas.csv", "a", encoding="UTF-8", newline="") as escritura:
                agregarRaza = csv.writer(escritura, delimiter="\n")
                agregarRaza.writerow([(self.__raza)])
                print("Se almaceno la nueva raza con exito...")         

    def eliminarRaza(self):
        """
        Este método permite al usuario eliminar una raza de la base de datos
        """
        raza_encontrada = False
        with open("razas.csv", "r", encoding="UTF-8", newline="") as lectura:
            contenido = lectura.read()
            contenido = contenido.lower()
            if self.__raza in contenido:
                raza_encontrada = True
                contenido = contenido.replace(self.__raza, "")

        if raza_encontrada == True:
            contenido = "\n".join([linea for linea in contenido.split("\n") if linea.strip()])
            with open("razas.csv", "w", encoding="UTF-8", newline="") as escritura:
                escritura.write(contenido)
            print("Se eliminó la raza de la base de datos")

        else:
            print("La raza no está almacenada en la base de datos") 