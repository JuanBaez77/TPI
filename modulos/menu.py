import tkinter as tk
from tkinter import *
from modulos.Persona import Persona
import modulos.Raza as Raza

# CREAMOS COLORES PARA EL MENU
COLOR_PRINCIPAL = "#2a3138"
COLOR_SECUNDARIO = "#3e444e"
COLOR_PAGINA = "#e0e0e0"
COLOR_BOTON = "#3e444e"

class MenuDesign(tk.Tk):
    def __init__(self, nombreVeterinaria):
        super().__init__()
        self.nombreVeterinaria = nombreVeterinaria
        self.colores()
        self.configMenu()

    def configMenu(self):
        self.title(f"VETERINARIA {self.nombreVeterinaria.upper()}")
        self.geometry("1024x600")
        self.labelTitulo = Label(self.menu_lateral, text="MENU PRINCIPAL")
        self.labelTitulo.config(fg="#fff",bg=COLOR_PRINCIPAL, font=("Roboto", 20))
        self.labelTitulo.pack(fill="x", pady=10, padx=5)
        btn_persona = Button(self.menu_lateral, text="Personas", command=self.menuPersona, fg="white", font=("Roboto", 10), bd= 0, bg=COLOR_PRINCIPAL)
        btn_persona.pack(fill="x",pady=10, padx=10)
        btn_mascota = Button(self.menu_lateral, text="Mascotas", command=self.menuMascota, fg="white", font=("Roboto", 10), bd= 0, bg=COLOR_PRINCIPAL)
        btn_mascota.pack(fill="x", pady=10, padx=10)
        btn_tratamiento = Button(self.menu_lateral, text="Tratamientos", command=menuTratamiento, fg="white", font=("Roboto", 10), bd= 0, bg=COLOR_PRINCIPAL)
        btn_tratamiento.pack(fill="x", pady=10, padx=10)
        btn_salir = Button(self.menu_lateral, text="SALIR", font=("Roboto", 10), command=self.quit, fg="white", bd= 0, bg="red")
        btn_salir.pack(fill="x", pady=10, padx=10)
    
    def colores(self):
        self.menu_lateral = Frame(self, bg=COLOR_PRINCIPAL, width=275)
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

        self.pagina = Frame(self, bg=COLOR_PAGINA,width= 150)
        self.pagina.pack(side=tk.RIGHT, fill="both", expand=True)


    def menuPersona(self):
        # borrar contenido en pagina
        for widget in self.pagina.winfo_children():
            widget.destroy()
        # BOTONES PARA ACCEDER A LAS FUNCIONES DEL MENU PERSONA
        Button(self.pagina, text="Mostrar personas", command=lambda: Persona.mostrarPersona(self.pagina), bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="Mostrar personas activas", command=lambda: Persona.mostrarPersonaActiva(self.pagina), bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="Registrar personas", command=Persona.registrarPersona, bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="Cambiar estado de una persona", command=Persona.cambiarEstadoPersona, bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        

    def menuMascota(self):
        # borrar contenido en pagina
        for widget in self.pagina.winfo_children():
            widget.destroy()
        # BOTONES PARA ACCEDER A LAS FUNCIONES DEL MENU MASCOTA
        Button(self.pagina, text="Mostrar mascotas activas", bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="Agregar nueva mascota", bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="MENU DE RAZAS", command=Raza.menuRaza, bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")


def menuTratamiento():
    ventana_tratamiento = Toplevel()
    ventana_tratamiento.title("Menú Tratamiento")
    ventana_tratamiento.geometry("300x200")

    menu_tratamiento = Menu(ventana_tratamiento)
    ventana_tratamiento.config(menu=menu_tratamiento)

    menu_tratamiento.add_command(label="Tratamientos Disponibles", command=mostrar_tratamientos_disponibles)
    menu_tratamiento.add_command(label="Agenda de Tratamientos", command=mostrar_agenda_tratamientos)