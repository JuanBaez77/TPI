import csv
from tkinter import messagebox
from Modulos.Tratamiento import Tratamiento
from Modulos.Vacuna import Vacuna

class ControladorTratamiento:
    def __init__(self,vista,update_callback):
        self.vista = vista
        self.listaTratamientos = []
        self.update_callback = update_callback
    
    # ESTE METODO ALMACENA LOS TRATAMIENTOS EN UNA LISTA Y LOS RETORNA
    def cargarTratamiento(self, lista=None):
        if lista is None:
            lista = []
        elif not isinstance(lista, list):
            raise ValueError("El argumento 'lista' debe ser de tipo list")    
        with open("csv/tratamiento.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido) 
            for linea in contenido:
                nombre = linea[0]
                descripcion = linea[1]
                estado = linea[2]
                tratamiento = Tratamiento(nombre, descripcion, estado)
                lista.append(tratamiento)
        return lista
    
    # ESTE METODO REGISTRA 
    def guardarTratamiento(self, lista, registro):
        nombre_val = lista[0].get()
        descripcion_val = lista[1].get()
        estado_val = True
        nuevo_tratamiento = Tratamiento(nombre_val, descripcion_val, estado_val)
        with open("csv/tratamiento.csv", "a", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                nuevo_tratamiento.get_nombre(),
                nuevo_tratamiento.get_descripcion(),
                nuevo_tratamiento.get_estado(),
            ])

        registro.destroy()
        messagebox.showinfo("Éxito", "Tratamiento registrado con éxito")
    
    def guardarcambio(self, listaTratamientos):
        with open("csv/tratamiento.csv", mode='w', encoding="utf-8", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Descripcion"])  # Escribir el encabezado
            for tratamiento in listaTratamientos:
                writer.writerow([tratamiento.get_nombre(), tratamiento.get_descripcion(), tratamiento.get_estado()])

    def cambiarEstadoTratamiento(self, nombre, label_mensaje):
        # ESTE METODO MODIFICARA EL ESTADO DEL TRATAMIENTO DE TRUE A FALSE Y VICEVERSA
        tratamiento = []
        encontrado = False
        with open("csv/tratamiento.csv", encoding="UTF-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == nombre:
                    estado_actual = row[2]
                    if estado_actual == "False":
                        row[2] = "True"
                        mensaje = f"Éxito al cambiar estado de Inactivo a Activo para {nombre}"
                    else:
                        row[2] = "False"
                        mensaje = f"Éxito al cambiar estado de Activo a Inactivo para {nombre}"
                    encontrado = True
                tratamiento.append(row)

        if encontrado:
            with open("csv/tratamiento.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(tratamiento)
            label_mensaje.config(text=mensaje, fg="green")
            if self.update_callback:
                    self.update_callback()
            else:
                label_mensaje.config(text="Error. Tratamiento no encontrado", fg="red")
    
    def cambiarTratamiento(self, nombre, atributo, nuevovalor):
        listaTratamientos = self.cargarTratamiento()
        for tratamiento in listaTratamientos:
            if tratamiento.get_nombre() == nombre:
                if atributo.lower() == "nombre":
                    tratamiento.set_nombre(nuevovalor)
                elif atributo.lower() == "descripcion":
                    tratamiento.set_descripcion(nuevovalor)
        self.guardarcambio(listaTratamientos)    

class ControladorVacuna:
    def __init__(self,vista,update_callback):
        self.vista = vista
        self.listaVacunas = []
        self.update_callback = update_callback

    # ESTE METODO ALMACENA LAS VACUNAS EN UNA LISTA Y LAS RETORNA
    def cargarVacunas(self, lista=None):
        if lista is None:
            lista = []
        elif not isinstance(lista, list):
            raise ValueError("El argumento 'lista' debe ser de tipo list")

        with open("csv/vacuna.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for linea in contenido:
                nombre = linea[0]
                descripcion = linea[1]
                estado = linea[2]
                vacuna = Vacuna(nombre, descripcion, estado)
                lista.append(vacuna)
        return lista
    
    # ESTE METODO REGISTRA 
    def guardarVacuna(self, lista, registro):
        nombre_val1 = lista[0].get()
        descripcion_val1 = lista[1].get()
        estado_val1 = True
        nueva_vacuna = Vacuna(nombre_val1, descripcion_val1, estado_val1)
        with open("csv/vacuna.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                nueva_vacuna.get_nombre(), 
                nueva_vacuna.get_descripcion(),
                nueva_vacuna.get_estado(),
            ])
        registro.destroy()
        messagebox.showinfo("Éxito", "Vacuna registrada con éxito")
        
    def guardarCambioVacuna(self, listaVacunas):
        with open("csv/vacuna.csv", mode='w', encoding="UTF-8", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Descripcion", "Estado"])
            for vacuna in listaVacunas:
                writer.writerow([vacuna.get_nombre(), vacuna.get_descripcion(), vacuna.get_estado()])
    def cambiarEstadoVacuna(self, nombre, label_mensaje):
        # ESTE METODO MODIFICARA EL ESTADO DE LA VACUNA DE TRUE A FALSE Y VICEVERSA
        vacuna = []
        encontrado = False
        with open("csv/vacuna.csv", encoding="UTF-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == nombre:
                    estado_actual = row[2]
                    if estado_actual == "False":
                        row[2] = "True"
                        mensaje = f"Éxito al cambiar estado de Inactivo a Activo para {nombre}"
                    else:
                        row[2] = "False"
                        mensaje = f"Éxito al cambiar estado de Activo a Inactivo para {nombre}"
                    encontrado = True
                vacuna.append(row)

        if encontrado:
            with open("csv/vacuna.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(vacuna)
            label_mensaje.config(text=mensaje, fg="green")
            if self.update_callback:
                    self.update_callback()
            else:
                label_mensaje.config(text="Error. Vacuna no encontrada", fg="red")

    def cambiarVacuna(self, nombre, atributo, nuevovalor):
        listaVacunas = self.cargarVacunas()
        for vacuna in listaVacunas:
            if vacuna.get_nombre() == nombre:
                if atributo.lower() == "nombre":
                    vacuna.set_nombre(nuevovalor)
                elif atributo.lower() == "descripcion":
                    vacuna.set_descripcion(nuevovalor)
        self.guardarCambioVacuna(listaVacunas)          

