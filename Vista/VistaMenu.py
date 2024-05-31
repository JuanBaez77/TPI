import tkinter as tk
from tkinter import *
from Modulos.Persona import Persona
from .VistaMascota import VistaMascota
from Vista.VistaPersona import VistaPersona
from Controllers.ControladorMascota import ControladorMascota
from Controllers.ControladorPersona import ControladorPersona

# CREAMOS LAS LISTAS
listaMascotas = []
listaMascotasCompleta = ControladorMascota.cargarMascotas(listaMascotas)
listaPersonas = []
listaPersonasCompleta = ControladorPersona.cargarPersona(listaPersonas)
# CREAMOS COLORES PARA EL MENU
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
        self.labelTitulo.config(fg="#fff",bg="black", font=("Roboto", 20))
        self.labelTitulo.pack(fill="x")
        btn_persona = Button(self.menu_lateral, text="Personas", command=self.menuPersona, fg="white", font=("Roboto", 10), bd= 0, bg=COLOR_PRINCIPAL)
        btn_persona.pack(fill="x",pady=10, padx=10)
        btn_mascota = Button(self.menu_lateral, text="Mascotas", command=self.menuMascota, fg="white", font=("Roboto", 10), bd= 0, bg=COLOR_PRINCIPAL)
        btn_mascota.pack(fill="x", pady=10, padx=10)
        btn_tratamiento = Button(self.menu_lateral, text="Tratamientos", command=menuTratamiento, fg="white", font=("Roboto", 10), bd= 0, bg=COLOR_PRINCIPAL)
        btn_tratamiento.pack(fill="x", pady=10, padx=10)
        btn_salir = Button(self.menu_lateral, text="SALIR", font=("Roboto", 10), command=self.quit, fg="black", bd= 0, bg="red")
        btn_salir.pack(fill="x", pady=10, padx=10)
    
    def colores(self):
        self.menu_lateral = Frame(self, bg="#5C88C4", width=275,)
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

        self.pagina = Frame(self, bg=COLOR_PAGINA,width= 150)
        self.pagina.pack(side=tk.RIGHT, fill="both", expand=True)


    def menuPersona(self):
        # borrar contenido en pagina
        for widget in self.pagina.winfo_children():
            widget.destroy()
        # BOTONES PARA ACCEDER A LAS FUNCIONES DEL MENU PERSONA
        Label(self.pagina, text="LISTA DE PERSONAS", font=("Roboto", 12), bg=self.pagina['bg']).pack(pady=5)
        
        # INSTANCIAMOS LA CLASE "VISTA PERSONA"
        vista_personas = VistaPersona(self.pagina)
        vista_personas.pack(fill="both", expand=True)

        # MOSTRAMOS LAS PERSONAS ALMACENADAS
        vista_personas.mostrar_persona(listaPersonasCompleta)
        
        # BOTON PARA AGREGAR PERSONAS
        Button(self.pagina, text="Cargar Nueva Persona", command=vista_personas.registrarPersona, bg="white", fg="red", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")

        
    def menuMascota(self):
        # LIMPIAMOS EL CONTENIDO DE LA PAGINA
        for widget in self.pagina.winfo_children():
            widget.destroy()

        Label(self.pagina, text="LISTA DE MASCOTAS", font=("Roboto", 12), bg=self.pagina['bg']).pack(pady=5)
        
        # INSTANCIAMOS LA CLASE "VISTA MASCOTA"
        vista_mascotas = VistaMascota(self.pagina)
        vista_mascotas.pack(fill="both", expand=True)

        # MOSTRAMOS LAS MASCOTAS ALMACENADAS
        vista_mascotas.mostrar_mascotas(listaMascotasCompleta)
        
        # BOTON PARA AGREGAR MASCOTAS
        Button(self.pagina, text="Cargar Nueva Mascota", command=vista_mascotas.crearMascota, bg="white", fg="red", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")


def menuTratamiento():
    ventana_tratamiento = Toplevel()
    ventana_tratamiento.title("Menú Tratamiento")
    ventana_tratamiento.geometry("300x200")

    menu_tratamiento = Menu(ventana_tratamiento)
    ventana_tratamiento.config(menu=menu_tratamiento)

    menu_tratamiento.add_command(label="Tratamientos Disponibles", command=mostrar_tratamientos_disponibles)
    menu_tratamiento.add_command(label="Agenda de Tratamientos", command=mostrar_agenda_tratamientos)
