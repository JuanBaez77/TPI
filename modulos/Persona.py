import csv
from tkinter import *
from tkinter import messagebox
class Persona:
    def __init__(self,nombre,apellido,tipoDocumento,documento,telefono,tipoPersona,estado):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__telefono = telefono
        self.__tipoPersona = tipoPersona
        self.__estado = estado

    # Getter y setter 
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre


    def getApellido(self):
        return self.__apellido
    def setApellido(self, apellido):
        self.__apellido = apellido


    def getTipoDocumento(self):
        return self.__tipoDocumento
    def setTipoDocumento(self, tipoDocumento):
        self.__tipoDocumento = tipoDocumento


    def getDocumento(self):
        return self.__documento
    def setDocumento(self, documento):
        self.__documento = documento


    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono


    def getTipoPersona(self):
        return self.__tipoPersona
    def setTipoPersona(self, tipoPersona):
        self.__tipoPersona = tipoPersona


    def getEstado(self):
        return self.__estado
    def setEstado(self, estado):
        self.__estado = estado

# METODOS


    def guardar_persona(list, registro):
        nombre_val = list[0].get()
        apellido_val = list[1].get()
        tipoDocumento_val = list[2].get()
        documento_val = list[3].get()
        telefono_val = list[4].get()
        tipoPersona_val = list[5].get()
        print(f"{nombre_val}, {apellido_val}, {tipoDocumento_val}")
        nueva_persona = Persona(
            nombre_val, apellido_val, tipoDocumento_val,
            documento_val, telefono_val, tipoPersona_val, True
        )
        with open("csv/persona.csv", "a", newline="") as file:
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
    @classmethod
    def mostrarPersonaActiva(cls, parent_frame):
        try:
            # Limpiar el frame antes de mostrar nuevas personas
            for widget in parent_frame.winfo_children():
                widget.destroy()
            
            Label(parent_frame, text="LISTA DE PERSONAS ACTIVAS", font=("Roboto", 12), bg=parent_frame['bg']).pack(pady=10)
            
            text_frame = Frame(parent_frame, bg=parent_frame['bg'])
            text_frame.pack(fill='both', expand=True)
            text_box = Text(text_frame, wrap="none", font=("Roboto", 10), bg="#f1f1f1", state='disabled')
            text_box.pack(side="left", fill="both", expand=True)
            scrollbar_y = Scrollbar(text_frame, command=text_box.yview)
            scrollbar_y.pack(side="right", fill="y")
            scrollbar_x = Scrollbar(text_frame, command=text_box.xview, orient="horizontal")
            scrollbar_x.pack(side="bottom", fill="x")
            text_box.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
            text_box.config(state='normal')
            
            # Agregar encabezados
            headers = f"{'Nombre':<20}{'Documento':<20}{'Teléfono':<20}\n"
            text_box.insert("end", headers)
            text_box.insert("end", "-"*60 + "\n")
            
            with open("csv/persona.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row[6] == "True":
                        persona_info = f"{row[0] + ' ' + row[1]:<20}{row[3]:<20}{row[4]:<20}\n"
                        text_box.insert("end", persona_info)
            text_box.config(state='disabled')
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo personas")

    @classmethod
    def mostrarPersona(cls, parent_frame):
        try:
            # Limpiar el frame antes de mostrar nuevas personas
            for widget in parent_frame.winfo_children():
                widget.destroy()
            
            Label(parent_frame, text="LISTA DE PERSONAS", font=("Roboto", 12), bg=parent_frame['bg']).pack(pady=10)
            
            text_frame = Frame(parent_frame, bg=parent_frame['bg'])
            text_frame.pack(fill='both', expand=True)
            text_box = Text(text_frame, wrap="none", font=("Roboto", 10), bg="#f1f1f1", state='disabled')
            text_box.pack(side="left", fill="both", expand=True)
            scrollbar_y = Scrollbar(text_frame, command=text_box.yview)
            scrollbar_y.pack(side="right", fill="y")
            scrollbar_x = Scrollbar(text_frame, command=text_box.xview, orient="horizontal")
            scrollbar_x.pack(side="bottom", fill="x")
            text_box.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
            text_box.config(state='normal')
            
            # Agregar encabezados
            headers = f"{'Nombre':<20}{'Documento':<20}{'Teléfono':<20}\n"
            text_box.insert("end", headers)
            text_box.insert("end", "-"*60 + "\n")
            
            with open("csv/persona.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    persona_info = f"{row[0] + ' ' + row[1]:<20}{row[3]:<20}{row[4]:<20}\n"
                    text_box.insert("end", persona_info)
            text_box.config(state='disabled')
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo personas")
    @classmethod
    def cambiarEstadoPersona(cls):
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


# STR
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.tipoDocumento}: {self.documento}, Tel: {self.telefono}, Tipo: {self.tipoPersona}, Estado: {self.estado}"