import csv
from tkinter import messagebox
from Modulos.Tratamiento import Tratamiento

class ControladorTratamiento:
    def __init__(self,vista):
        self.vista = vista
        self.listaTratamientos = []
    
    # ESTE METODO ALMACENA LOS TRATAMIENTOS EN UNA LISTA Y LOS RETORNA
    def cargarTratramiento(lista = list):    
        with open("TPI/csv/persona.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido) 
            for linea in contenido:
                nombre = linea[0]
                destino = linea[1]
                estado = linea[2]
                tratamiento = Tratamiento(nombre,destino, estado)
                lista.append(tratamiento)
        return lista
    
    def guardarTratamiento(lista, registro):
        # ESTE METODO REGISTRA 
        def cambiarTratamiento(tratamiento_val):
            nombre_val = list[0].get()
            destino_val = list[1].get()
            tratamiento_val = cambiarTratamiento(tratamiento_val)
            estado_val = True
            nuevo_tratamiento = Tratamiento(nombre_val,destino_val,estado_val)
        
            with open("TPI/csv/tratamiento.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    nuevo_tratamiento.get_nombre(),
                    nuevo_tratamiento.get_destino(),
                    nuevo_tratamiento.get_estado(),
                ])
            registro.destroy()
            messagebox.showinfo("Éxito", "Tratamiento registrado con éxito")

    def cambiarEstadoTratamiento(self, nombre, label_mensaje):
        # ESTE METODO MODIFICARA EL ESTADO DEL TRATAMIENTO DE TRUE A FALSE Y VICEVERSA
        tratamiento = []
        encontrado = False

        try:
            with open("TPI/csv/tratamiento.csv", encoding="UTF-8") as file:
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
                with open("TPI/csv/tratamiento.csv", "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(tratamiento)
                label_mensaje.config(text=mensaje, fg="green")
                if self.update_callback:
                        self.update_callback()
                else:
                    label_mensaje.config(text="Error. Documento no encontrado", fg="red")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

