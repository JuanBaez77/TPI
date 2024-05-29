import tkinter as tk
from tkinter import *
from tkinter import messagebox
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
        Button(self.pagina, text="Registrar personas", command=self.registrarPersona, bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="Cambiar estado de una persona", command=Persona.cambiarEstadoPersona, bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")

    
    def menuMascota(self):
        # borrar contenido en pagina
        for widget in self.pagina.winfo_children():
            widget.destroy()
        # BOTONES PARA ACCEDER A LAS FUNCIONES DEL MENU MASCOTA
        Button(self.pagina, text="Mostrar mascotas activas", bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="Agregar nueva mascota", bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="MENU DE RAZAS", command=Raza.menuRaza, bg=COLOR_SECUNDARIO, fg="white", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")

    def registrarPersona(self):
        registro = Toplevel()
        registro.geometry("650x550")
        registro.title("Registro")
        registro.resizable(False, False)
        registro.config(background="#2a3138")
        tituloRegistro = Label(registro, text="Registrar Persona", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()

        # Crear los widgets de entrada
        lNombre = Label(registro, text="Nombre:", bg="#2a3138", fg="white").place(x=22, y=70)
        lApellido = Label(registro, text="Apellido:", bg="#2a3138", fg="white").place(x=22, y=130)
        lTipoDocumento = Label(registro, text="Tipo de documento:", bg="#2a3138", fg="white").place(x=22, y=190)
        lDocumento = Label(registro, text="Documento:", bg="#2a3138", fg="white").place(x=22, y=250)
        lTelefono = Label(registro, text="Telefono:", bg="#2a3138", fg="white").place(x=22, y=310)
        lTipoPersona = Label(registro, text="Tipo de Persona", bg="#2a3138", fg="white").place(x=22, y=370)

        nombre = StringVar()
        apellido = StringVar()
        documento = StringVar()
        telefono = StringVar()
        tipoDocumento = StringVar()
        tipoDocumento.set("DNI")
        tipoPersona = StringVar()
        tipoPersona.set("CLI")

        newPersona = [nombre, apellido, tipoDocumento, documento, telefono, tipoPersona]

        entryNombre = Entry(registro, textvariable=nombre, width="35").place(x=22, y=100)
        entryApellido = Entry(registro, textvariable=apellido, width="35").place(x=22, y=160)
        entryDocumento = Entry(registro, textvariable=documento, width="35").place(x=22, y=280)
        entryTelefono = Entry(registro, textvariable=telefono, width="35").place(x=22, y=340)
        entryTipoPersona = OptionMenu(registro, tipoPersona, "CLI", "EMP").place(x=22, y=400)
        entryTipoDocumento = OptionMenu(registro, tipoDocumento, "DNI", "PAS").place(x=22, y=210)

        submit = Button(registro, text="Registrar", command=lambda: self.guardar_persona(newPersona, registro), width=30)
        submit.place(x=22, y=450)

    def guardar_persona(self, newPersona, registro):
        Persona.guardar_persona(newPersona, registro)

def menuTratamiento():
    ventana_tratamiento = Toplevel()
    ventana_tratamiento.title("Menú Tratamiento")
    ventana_tratamiento.geometry("300x200")

    menu_tratamiento = Menu(ventana_tratamiento)
    ventana_tratamiento.config(menu=menu_tratamiento)

    menu_tratamiento.add_command(label="Tratamientos Disponibles", command=mostrar_tratamientos_disponibles)
    menu_tratamiento.add_command(label="Agenda de Tratamientos", command=mostrar_agenda_tratamientos)
