import csv
from tkinter import *
from tkinter import messagebox
from Modulos.Diagnostico import Diagnostico


class ControladorDiagnostico:
    
    def __init__(self,vista, update_callback=None):
        self._vista = vista
        self._listaDiagnostico = []
        self.update_callback = update_callback
    

    def guardarDiagnostico(self, lista, registro):
        def IDPropietario(propietario_val):
            with open("csv/persona.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if (row[0]) == (f"{propietario_val}"):
                        return row[0]
            return None

        nombre_val = lista[0].get()
        diagnostco_val = lista[1].get()
        propietario = lista[2].get()
        propietario_val = IDPropietario(propietario)
        
        if propietario_val is None:
            messagebox.showerror("Error", "Propietario no encontrado en el archivo CSV")
            return

        estado_val = True
        nuevo_diagnostico = Diagnostico(
            nombre_val, diagnostco_val, propietario_val,
            estado_val
        )
        with open("csv/diagnostico.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                nuevo_diagnostico.get_nombre(),
                nuevo_diagnostico.get_diagnostico(),
                nuevo_diagnostico.get_propietario(),
                nuevo_diagnostico.get_estado(),
            ])
        registro.destroy()
        messagebox.showinfo("Éxito", "Diagnóstico registrado con éxito")
        if self.update_callback:
            self.update_callback()

    def cargarDiagnostico(lista=list):
        lista = []
        with open("csv/diagnostico.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)  # Omitir la primera fila (cabecera)
            for linea in contenido:
                nombre = linea[0]
                diagnostico = linea[1]
                propietario = linea[2]
                estado = linea[3]
                diagnosticos = Diagnostico(nombre,diagnostico,propietario,estado)
                lista.append(diagnosticos)
        return lista

    def cargarID(self):
        listaIDCompleta = []
        with open("csv/persona.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                if row[6] == "CLI" and row[7] == "True":
                    listaIDCompleta.append(f"{row[0]}")
        return listaIDCompleta
    
    def cargarDiagnosticos(self):
        listaDiagnosticoCompleta = set()  # Usamos un conjunto en lugar de una lista
        
        with open("csv/diagnostico.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                listaDiagnosticoCompleta.add(row[1])  # Agregamos el diagnóstico al conjunto
        
        return list(listaDiagnosticoCompleta)
    
    def cargarMascota(self):
        listaMascotaCompleta = []
        with open("csv/mascota.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                    listaMascotaCompleta.append(f"{row[0]}")
        return listaMascotaCompleta
    
    def cambiarEstadoDiagnostico(self, nombre,propietario, label_mensaje):
        diagnosticos = []
        encontrado = False
        mensaje = ""
        nombre = str(nombre)
        propietario = str(propietario)

        try:
            with open("csv/diagnostico.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row[0].strip() == nombre.strip():
                        if row[2].strip() == propietario.strip():
                            propietario = row[2]
                            estado_actual = row[3]
                            if estado_actual == "false":
                                row[3] = "true"
                                mensaje = f"Éxito al cambiar estado de Inactivo a Activo para {nombre} del dueño con ID:{propietario}"
                            else:
                                row[3] = "false"
                                mensaje = f"Éxito al cambiar estado de Activo a Inactivo para {nombre} del dueño con ID: {propietario}"
                            encontrado = True
                    diagnosticos.append(row)

            if encontrado:
                with open("csv/diagnostico.csv", "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(diagnosticos)
                label_mensaje.config(text=mensaje, fg="green")
                if self.update_callback:
                    self.update_callback()
            else:
                label_mensaje.config(text="Error. Nombre o ID no encontrado", fg="red")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def cargarRanking(self):
            diagnosticos = {}
            
            with open("csv/diagnostico.csv", mode='r', encoding="UTF-8", newline="") as archivo:
                contenido = csv.reader(archivo)
                next(contenido, None)  
                for linea in contenido:
                    propietario = linea[2] 
                    nombre_mascota = linea[0]
                    clave = (propietario, nombre_mascota) 
                    if clave in diagnosticos:
                        diagnosticos[clave] += 1
                    else:
                        diagnosticos[clave] = 1
        
            ranking = sorted(diagnosticos.items(), key=lambda x: x[1], reverse=True)
            
            ranking_lista = [[item[0][0], item[0][1], item[1]] for item in ranking]  
            
            return ranking_lista

    def cantidadRazasPorDiagnostico(self):
        try:
            razas_mascotas = {}
            with open("csv/mascota.csv", mode='r', encoding="UTF-8", newline="") as archivo:
                contenido = csv.reader(archivo)
                next(contenido) 
                for linea in contenido:
                    raza = linea[1]
                    if raza not in razas_mascotas:
                        razas_mascotas[raza] = 0

            with open("csv/diagnostico.csv", mode='r', encoding="UTF-8", newline="") as archivo:
                contenido = csv.reader(archivo)
                next(contenido)  
                for linea in contenido:
                    raza_diagnostico = linea[1]
                    if raza_diagnostico in razas_mascotas:
                        razas_mascotas[raza_diagnostico] += 1

            return razas_mascotas
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo de diagnósticos no se encuentra.")
            return {}
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")
            return {}

    def mostrarDiagnostico(self):
        self._vista.mostrar_Diagnostico(self._listaDiagnostico)