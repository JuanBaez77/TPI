import tkinter as tk
from tkinter import *
from modulos.Persona import Persona
import modulos.Raza as Raza
class MenuDesign(tk.Tk):
    def __init__(self, nombreVeterinaria):
        super().__init__()
        self.nombreVeterinaria = nombreVeterinaria
        self.configMenu()

    def configMenu(self):
        self.title(f"VETERINARIA {self.nombreVeterinaria.upper()}")
        self.geometry("650x350")
        lbl = Label(self, text="MENU")
        lbl.pack(pady=20)
        btn_persona = Button(self, text="Personas", command=menuPersona)
        btn_persona.pack(pady=10)
        btn_mascota = Button(self, text="Mascotas", command=menuMascota)
        btn_mascota.pack(pady=10)
        btn_tratamiento = Button(self, text="Tratamientos", command=menuTratamiento)
        btn_tratamiento.pack(pady=10)

def menuPersona():
    # CREAMOS LA VENTANA DE MENU PERSONA
    menuper= Toplevel()
    menuper.title("Menú Persona")
    menuper.geometry("650x350")
    # BOTONES PARA ACCEDER A LAS FUNCIONES DEL MENU PERSONA
    btnMostrarPersona = Button(menuper, text="Mostrar personas", command=Persona.mostrarPersona).pack()
    btnMostrarPersonaActiva = Button(menuper, text="mostrar personas activas", command=Persona.mostrarPersonaActiva).pack()
    btnRegistrarPersona = Button(menuper, text="Registrar personas", command=Persona.registrarPersona).pack()
    btncambiarEstado = Button(menuper, text="Cambiar estado de una persona", command=Persona.cambiarEstadoPersona).pack()


def menuMascota():
    # CREAMOS LA VENTANA DE MENU MASCOTA
    menumasc = Toplevel()
    menumasc.title("Menú Mascota")
    menumasc.geometry("650x350")
    # BOTONES PARA ACCEDER A LAS FUNCIONES DEL MENU MASCOTA
    btnMostrarMascotas = Button(menumasc, text="Mostrar mascotas activas").pack()
    btnNuevaMascota = Button(menumasc, text="Agregar nueva mascota").pack()
    btnMenuRaza = Button(menumasc, text="MENU DE RAZAS", command=Raza.menuRaza).pack()

def menuTratamiento():
    ventana_tratamiento = Toplevel()
    ventana_tratamiento.title("Menú Tratamiento")
    ventana_tratamiento.geometry("300x200")

    menu_tratamiento = Menu(ventana_tratamiento)
    ventana_tratamiento.config(menu=menu_tratamiento)

    menu_tratamiento.add_command(label="Tratamientos Disponibles", command=mostrar_tratamientos_disponibles)
    menu_tratamiento.add_command(label="Agenda de Tratamientos", command=mostrar_agenda_tratamientos)

