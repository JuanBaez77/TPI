import csv
from tkinter import *
from tkinter import messagebox
from Modulos.Raza import Raza
from Modulos.Mascota import Mascota

class ControladorMascota:
    
    def __init__(self,vista, update_callback=None):
        self._vista = vista
        self._listaMascotas = []
        self.listaRazas = []
        self.update_callback = update_callback
    
    def guardarMascota(list, registro):
        nombre_val = list[0].get()
        raza_val = list[1].get()
        propietario_val = list[2].get()
        estado_val = list[3].get()
        nueva_mascota = Mascota(nombre_val,raza_val,propietario_val,estado_val)
        
        with open("TPI/csv/mascota.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                nueva_mascota.get_nombre(),
                nueva_mascota.get_raza(),
                nueva_mascota.get_propietario(),
                nueva_mascota.get_estado(),
            ])
        registro.destroy()
        messagebox.showinfo("Éxito", "Mascota registrada con éxito")

    def cargarRazas(self):
        listaRazasCompleta = []
        with open("TPI/csv/razas.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            for i in contenido:
                listaRazasCompleta.append(i)
        return listaRazasCompleta

    def guardarRaza(newRaza):
        nombre_raza = newRaza.get().lower()
        if nombre_raza:
            raza = Raza(nombre_raza, 1)
            try:
                with open("TPI/csv/razas.csv", mode='a', newline='') as archivo:
                    razaNueva = csv.writer(archivo)
                    razaNueva.writerow([raza.get_raza(), "1"])
                messagebox.showinfo("Éxito", f"Raza '{raza.get_raza()}' guardada en razas.csv")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar la raza: {e}")
        else:
            messagebox.showerror("Error", "Por favor ingrese un nombre de raza.")

    def cargarMascotas(lista=list):
        with open("TPI/csv/mascota.csv", mode='r', encoding="utf-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido) 
            for linea in contenido:
                nombre = linea[0]
                raza = linea[1]
                propietario = linea[2]
                estado = linea[3]
                mascota = Mascota(nombre, raza, propietario, estado)
                lista.append(mascota)
        return lista

    def cambiarEstadoPersona(cls,):
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

    def cambiarEstadoMascota(self, nombre, label_mensaje):
        mascotas = []
        encontrado = False
        with open("TPI/csv/mascota.csv", encoding="UTF-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == nombre:
                    estado_actual = row[3]
                    if estado_actual == "False":
                        row[3] = "True"
                        mensaje = f"Éxito al cambiar estado de Inactivo a Activo para {nombre}"
                    else:
                        row[3] = "False"
                        mensaje = f"Éxito al cambiar estado de Activo a Inactivo para {nombre}"
                    encontrado = True
                mascotas.append(row)

        if encontrado:
            with open("TPI/csv/mascota.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(mascotas)
            label_mensaje.config(text=mensaje, fg="green")
            if self.update_callback:
                    self.update_callback()
            else:
                label_mensaje.config(text="Error. Documento no encontrado", fg="red")