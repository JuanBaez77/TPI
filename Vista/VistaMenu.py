import tkinter as tk
from tkinter import *
from Modulos.Persona import Persona
from .VistaMascota import VistaMascota
from Vista.VistaPersona import VistaPersona
from Controllers.ControladorMascota import ControladorMascota
from Controllers.ControladorPersona import ControladorPersona

listaMascotas = []
listaMascotasCompleta = ControladorMascota.cargarMascotas(listaMascotas)
listaPersonas = []
listaPersonasCompleta = ControladorPersona.cargarPersona(listaPersonas)

COLOR_PRINCIPAL = "#6890C5"
COLOR_SECUNDARIO = "#3e444e"
COLOR_PAGINA = "#e0e0e0"
COLOR_BOTON = "#3e444e"

class Vista(tk.Tk):
    def __init__(self, nombreVeterinaria):
        super().__init__()
        self.nombreVeterinaria = nombreVeterinaria
        self.colores()
        self.configMenu()

    def configMenu(self):
        self.title(f"VETERINARIA {self.nombreVeterinaria.upper()}")
        self.geometry("1024x600")
        self.labelTitulo = Label(self.menu_lateral, text="MENU PRINCIPAL")
        self.labelTitulo.config(fg="#fff", bg="black", font=("Roboto", 20))
        self.labelTitulo.pack(fill="x")
        btn_persona = Button(self.menu_lateral, text="Personas", command=self.menuPersona, fg="white", font=("Roboto", 10), bd=0, bg=COLOR_PRINCIPAL)
        btn_persona.pack(fill="x", pady=10, padx=10)
        btn_mascota = Button(self.menu_lateral, text="Mascotas", command=self.menuMascota, fg="white", font=("Roboto", 10), bd=0, bg=COLOR_PRINCIPAL)
        btn_mascota.pack(fill="x", pady=10, padx=10)
        btn_tratamiento = Button(self.menu_lateral, text="Tratamientos", command=menuTratamiento, fg="white", font=("Roboto", 10), bd=0, bg=COLOR_PRINCIPAL)
        btn_tratamiento.pack(fill="x", pady=10, padx=10)
        btn_salir = Button(self.menu_lateral, text="SALIR", font=("Roboto", 10), command=self.quit, fg="black", bd=0, bg="red")
        btn_salir.pack(fill="x", pady=10, padx=10)

    def colores(self):
        self.menu_lateral = Frame(self, bg="#5C88C4", width=275)
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

        self.pagina = Frame(self, bg=COLOR_PAGINA, width=150)
        self.pagina.pack(side=tk.RIGHT, fill="both", expand=True)

    def menuPersona(self):
        for widget in self.pagina.winfo_children():
            widget.destroy()

        Label(self.pagina, text="LISTA DE PERSONAS", font=("Roboto", 12), bg=self.pagina['bg']).pack(pady=5)

        vista_personas = VistaPersona(self.pagina)
        vista_personas.pack(fill="both", expand=True)

        vista_personas.mostrar_persona(listaPersonasCompleta)

        Button(self.pagina, text="Cargar Nueva Persona", command=vista_personas.registrarPersona, bg="white", fg="red", font=("Roboto", 12), bd=0).pack(pady=8, padx=20, fill="x")

        Button(self.pagina, text="Cambiar Estado de Persona", command=self.abrir_cambiar_estado, bg="white", fg="red", font=("Roboto", 12), bd=0).pack(pady=3, padx=20, fill="x")

    def menuMascota(self):
        for widget in self.pagina.winfo_children():
            widget.destroy()

        Label(self.pagina, text="LISTA DE MASCOTAS", font=("Roboto", 12), bg=self.pagina['bg']).pack(pady=5)

        vista_mascotas = VistaMascota(self.pagina)
        vista_mascotas.pack(fill="both", expand=True)

        vista_mascotas.mostrar_mascotas(listaMascotasCompleta)

        Button(self.pagina, text="Cargar Nueva Mascota", command=vista_mascotas.crearMascota, bg="white", fg="red", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")

    def abrir_cambiar_estado(self):
        cambiar_estado_ventana = Toplevel(self)
        cambiar_estado_ventana.title("Cambiar Estado de Persona")
        cambiar_estado_ventana.geometry("400x200")

        label_documento = Label(cambiar_estado_ventana, text="DOCUMENTO DE LA PERSONA QUE DESEA CAMBIAR")
        label_documento.pack(pady=5)

        entry_documento = Entry(cambiar_estado_ventana)
        entry_documento.pack(pady=5)

        label_mensaje = Label(cambiar_estado_ventana, text="", fg="red")
        label_mensaje.pack(pady=5)

        btn_cambiar_estado = Button(cambiar_estado_ventana, text="Cambiar Estado", command=lambda: ControladorPersona.cambiarEstadoPersona(entry_documento.get(), label_mensaje))
        btn_cambiar_estado.pack(pady=20)


def menuTratamiento():
    ventana_tratamiento = Toplevel()
    ventana_tratamiento.title("Menú Tratamiento")
    ventana_tratamiento.geometry("300x200")

    menu_tratamiento = Menu(ventana_tratamiento)
    ventana_tratamiento.config(menu=menu_tratamiento)

    menu_tratamiento.add_command(label="Tratamientos Disponibles", command=mostrar_tratamientos_disponibles)
    menu_tratamiento.add_command(label="Agenda de Tratamientos", command=mostrar_agenda_tratamientos)
