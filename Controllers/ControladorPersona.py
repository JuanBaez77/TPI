import csv
from tkinter import messagebox
from Modulos.Persona import Persona

class ControladorPersona:
    
    def __init__(self, vista, update_callback=None):
        self._vista = vista
        self._listaPersonas = []
        self.update_callback = update_callback
    
    @staticmethod
    def guardarPersona(lista, registro):
        nombre_val = lista[0].get()
        apellido_val = lista[1].get()
        tipoDocumento_val = lista[2].get()
        documento_val = lista[3].get()
        telefono_val = lista[4].get()
        tipoPersona_val = lista[5].get()
        nueva_persona = Persona(
            nombre_val, apellido_val, tipoDocumento_val,
            documento_val, telefono_val, tipoPersona_val, True
        )
        with open("TPI/csv/persona.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                nueva_persona.getNombre(),
                nueva_persona.getApellido(),
                nueva_persona.getTipoDocumento(),
                nueva_persona.getDocumento(),
                nueva_persona.getTelefono(),
                nueva_persona.getTipoPersona(),
                nueva_persona.getEstado()
            ])
        registro.destroy()
        messagebox.showinfo("Éxito", "Persona registrada con éxito")

    @staticmethod
    def cargarPersona(lista=list):
        with open("TPI/csv/persona.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)  # Omitir la primera fila (cabecera)
            for linea in contenido:
                nombre = linea[0]
                apellido = linea[1]
                tipoDocumento = linea[2]
                documento = linea[3]
                telefono = linea[4]
                tipoPersona = linea[5]
                estado = linea[6]
                persona = Persona(nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado)
                lista.append(persona)
        return lista
    
    def cambiarEstadoPersona(self, documento, label_mensaje):
        personas = []
        encontrado = False

        try:
            with open("TPI/csv/persona.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row[3] == documento:
                        nombre = f"{row[0]} {row[1]}"
                        estado_actual = row[6]
                        if estado_actual == "False":
                            row[6] = "True"
                            mensaje = f"Éxito al cambiar estado de Inactivo a Activo para {nombre}"
                        else:
                            row[6] = "False"
                            mensaje = f"Éxito al cambiar estado de Activo a Inactivo para {nombre}"
                        encontrado = True
                    personas.append(row)

            if encontrado:
                with open("TPI/csv/persona.csv", "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(personas)
                label_mensaje.config(text=mensaje, fg="green")
                if self.update_callback:
                    self.update_callback()
            else:
                label_mensaje.config(text="Error. Documento no encontrado", fg="red")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def mostrarPersona(self):
        self._vista.mostrar_persona(self._listaPersonas)
