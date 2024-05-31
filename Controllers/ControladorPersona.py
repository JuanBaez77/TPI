import csv
from tkinter import *
from tkinter import messagebox
from Modulos.Persona import Persona

class ControladorPersona:
    
    def __init__(self,vista):
        self._vista = vista
        self._listaPersonas = []
    
    def guardarPersona(list, registro):
        nombre_val = list[0].get()
        apellido_val = list[1].get()
        tipoDocumento_val = list[2].get()
        documento_val = list[3].get()
        telefono_val = list[4].get()
        tipoPersona_val = list[5].get()
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

    def cargarPersona(lista=list):
        with open("csv/persona.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            for linea in contenido:
                nombre = linea[0]
                apellido = linea[1]
                tipoDocumento = linea[2]
                documento = linea[3]
                telefono = linea[4]
                tipoPersona = linea[5]
                estado = linea[6]
                persona = Persona(nombre,apellido,tipoDocumento,documento,telefono,tipoPersona,estado)
                lista.append(persona)
        return lista
    
    def mostrarPersona(self):
        self._vista.mostrarPersona(self._listaPersonas)