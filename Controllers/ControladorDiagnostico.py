import csv
from tkinter import *
from tkinter import messagebox
from Modulos.Diagnostico import Diagnostico


class ControladorDiagnostico:
    
    def __init__(self,vista, update_callback=None):
        self._vista = vista
        self._listaDiagnostico = []
        self.update_callback = update_callback
    

    def guardarDiagnostico(lista, registro):
        try:
            with open("csv/diagnostico.csv", newline="", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                last_id = 0
                for row in reader:
                    last_id = int(row[0])
                identificador = last_id + 1
        except FileNotFoundError:
            identificador = 1  # Si el archivo no existe, empezar con el id 1

        nombre_val = lista[0].get()
        diagnostco_val = lista[1].get()
        propietario_val = lista[2].get()
        estado_val = lista[3].get()
        nuevo_diagnostico = Diagnostico(
            nombre_val, diagnostco_val, propietario_val,
            estado_val, True
        )
        with open("csv/diagnostico.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                identificador,
                nuevo_diagnostico.get_nombre(),
                nuevo_diagnostico.get_diagnostico(),
                nuevo_diagnostico.get_propietario(),
                nuevo_diagnostico.get_estado(),
            ])
        registro.destroy()
        messagebox.showinfo("Éxito", "Diagnostico registrado con éxito")

    def cargarDiagnostico(lista=list):
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
                label_mensaje.config(text="Error. ID no encontrado", fg="red")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def mostrarDiagnostico(self):
        self._vista.mostrar_Diagnostico(self._listaDiagnostico)