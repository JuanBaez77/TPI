import csv
from tkinter import *
from tkinter import messagebox
from Modulos.Mascota import Mascota
class Persona:
    def __init__(self, nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__telefono = telefono
        self.__tipoPersona = tipoPersona
        self.__estado = estado

    # Getters y Setters
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

    @classmethod
    def mostrarPersonaActiva(cls, parent_frame):
        try:
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

    def __str__(self):
        return f"{self.__nombre} {self.__apellido}, {self.__tipoDocumento}: {self.__documento}, Tel: {self.__telefono}, Tipo: {self.__tipoPersona}, Estado: {self.__estado}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado, mascota):
        super().__init__(nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado)
        self.__mascota = mascota

        #getters y setters
        def getMascota(self):
            return self.__mascota
        def setMascota(self,mascota):
            self.__mascota = mascota
            return f"{super().__str__(), Mascota: {self.__mascota}}"
class Empleado:
    def __init__(self, nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado):
        super().__init__(nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado)