import csv
from tkinter import *
from tkinter import messagebox
from Modulos.Raza import Raza
from Modulos.Mascota import Mascota

class ControladorMascota:
    
    def __init__(self,vista):
        self._vista = vista
        self._listaPersonas = []
        self._listaRazas = []
    
    def guardarMascota(list, registro):
        nombre_val = list[0].get()
        raza_val = list[1].get()
        propietario_val = list[2].get()
        estado_val = list[3].get()
        nueva_mascota = Mascota(nombre_val,raza_val,propietario_val,estado_val)
        
        with open("csv/mascota.csv", "a", newline="") as file:
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
        with open("razas.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            for id_raza, estado in contenido:
                self._listaRazas[int(estado)] = id_raza
        return self._listaRazas
    
    def mostrarRaza(self):
        self._vista.mostrarRazas(self._listaRazas)
        
    def crearRaza():
        """
        Permitir al usuario añadir una raza al csv
        """
        def guardarRaza():
            nombre_raza = raza_entry.get().lower()
            if nombre_raza:
                raza = Raza(nombre_raza)
                try:
                    with open("csv/razas.csv", mode='a', newline='') as archivo:
                        razaNueva = csv.writer(archivo)
                        razaNueva.writerow([raza.get_raza(), "1"])
                    messagebox.showinfo("Éxito", f"Raza '{raza.get_raza()}' guardada en razas.csv")
                    raza_entry.delete(0, END)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar la raza: {e}")
            else:
                messagebox.showerror("Error", "Por favor ingrese un nombre de raza.")

        top = Toplevel()
        top.title("Agregar Raza")
        top.geometry("300x150")

        Label(top, text="Ingrese el nombre de la raza:").pack(pady=10)
        raza_entry = Entry(top)
        raza_entry.pack(pady=5)
        Button(top, text="Guardar", command=guardarRaza).pack(pady=20)

    def cargarMascotas(lista=list):
        with open("csv/mascota.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            for linea in contenido:
                nombre = linea[0]
                raza = linea[1]
                propietario = linea[2]
                estado = int(linea[3])
                mascota = Mascota(nombre, raza, propietario, estado)
                lista.append(mascota)
        return lista

    def mostrarMascota(self):
        self._vista.mostrarMascotas(self._listaMascotas)
    
    