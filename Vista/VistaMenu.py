import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Modulos.Persona import Persona
from .VistaMascota import VistaMascota
from Vista.VistaPersona import VistaPersona
from Vista.VistaDiagnostico import VistaDiagnostico
from Controllers.ControladorMascota import ControladorMascota
from Controllers.ControladorPersona import ControladorPersona
from Controllers.ControladorDiagnostico import ControladorDiagnostico

COLOR_PRINCIPAL = "#2a3138"
COLOR_SECUNDARIO = "#18BC9C"
COLOR_PAGINA = "#e0e0e0"
COLOR_BOTON = "#3e444e"
COLOR_HOVER = "#2f88c5"

fuente = "FontAwesome"

class Vista(tk.Tk):
    def __init__(self, nombreVeterinaria):
        super().__init__()
        self.nombreVeterinaria = nombreVeterinaria
        self.colores()
        self.configMenu()

        self.controladorPersona = ControladorPersona(self, self.actualizarVistaPersonas)
        self.controladorMascota = ControladorMascota(self ,self.actualizarVistaMascota)
        self.controladorDiagnostico = ControladorDiagnostico(self,self.actualizarVistaDiagnostico)

        

    def configMenu(self):
        self.title(f"Veterinary {self.nombreVeterinaria}")
        self.geometry("1024x600")
        self.labelTitulo = Label(self.barra_superior, text="      MENU")
        self.labelTitulo.config(fg="#fff",bg="#1f2329", font=(fuente, 20))
        self.labelTitulo.pack(fill="both", side=tk.LEFT)
        
        self.icon_persona = ImageTk.PhotoImage(Image.open("TPI/assets/person_icon.png").resize((20, 20)))
        self.icon_mascota = ImageTk.PhotoImage(Image.open("TPI/assets/pet_icon.png").resize((20, 20)))
        self.icon_tratamiento = ImageTk.PhotoImage(Image.open("TPI/assets/treatment_icon.webp").resize((20, 20)))
        self.icon_Diagnotico = ImageTk.PhotoImage(Image.open("TPI/assets/icon_diagnostico.png").resize((20, 20)))
        self.icon_logo = ImageTk.PhotoImage(Image.open("TPI/assets/logo_nuevo.png").resize((100, 100)))
        self.fondo = ImageTk.PhotoImage(Image.open("TPI/assets/logo_nuevo.png").resize((600, 600)))
        
        logo = Label(self.menu_lateral, image=self.icon_logo, bg=COLOR_PRINCIPAL)
        logo.pack(side=tk.TOP, padx=10)
        
        fondo = tk.Label(self.pagina, image=self.fondo, bg=COLOR_PAGINA)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
        btn_persona = Button(self.menu_lateral, text="     Personas" ,image=self.icon_persona,compound="left", command=self.menuPersona, fg="white", font=(fuente, 12), bd= 0, bg=COLOR_PRINCIPAL,padx=20)
        btn_persona.pack(fill="x", anchor="w")
        btn_persona.bind("<Enter>", lambda event: btn_persona.config(bg=COLOR_HOVER, fg="white"))
        btn_persona.bind("<Leave>", lambda event: btn_persona.config(bg=COLOR_PRINCIPAL, fg="white"))
        
        btn_mascota = Button(self.menu_lateral, text="     Mascotas",image=self.icon_mascota,compound="left", command=self.menuMascota, fg="white", font=(fuente, 12), bd= 0, bg=COLOR_PRINCIPAL,padx=20)
        btn_mascota.pack(fill="x", anchor="w")
        btn_mascota.bind("<Enter>", lambda event: btn_mascota.config(bg=COLOR_HOVER, fg="white"))
        btn_mascota.bind("<Leave>", lambda event: btn_mascota.config(bg=COLOR_PRINCIPAL, fg="white"))

        btn_diagnostico = Button(self.menu_lateral, text="     Diagnostico",image=self.icon_Diagnotico,compound="left", command=self.menuDiagnostico, fg="white", font=(fuente, 12), bd= 0, bg=COLOR_PRINCIPAL,padx=5)
        btn_diagnostico.pack(fill="x", anchor="w")
        btn_diagnostico.bind("<Enter>", lambda event: btn_diagnostico.config(bg=COLOR_HOVER, fg="white"))
        btn_diagnostico.bind("<Leave>", lambda event: btn_diagnostico.config(bg=COLOR_PRINCIPAL, fg="white"))
        
        btn_tratamiento = Button(self.menu_lateral, text="Tratamientos",image=self.icon_tratamiento,compound="left", command=menuTratamiento, fg="white", font=(fuente, 12), bd= 0, bg=COLOR_PRINCIPAL, padx=20)
        btn_tratamiento.pack(fill="x", anchor="w")
        btn_tratamiento.bind("<Enter>", lambda event: btn_tratamiento.config(bg=COLOR_HOVER, fg="white"))
        btn_tratamiento.bind("<Leave>", lambda event: btn_tratamiento.config(bg=COLOR_PRINCIPAL, fg="white"))
        
        btn_salir = Button(self.menu_lateral, text="SALIR", font=(fuente, 14), command=self.quit, fg="white", bd= 0, bg=COLOR_PRINCIPAL)
        btn_salir.pack(fill="x", side=tk.BOTTOM)
        btn_salir.bind("<Enter>", lambda event: btn_salir.config(bg="red", fg="white"))
        btn_salir.bind("<Leave>", lambda event: btn_salir.config(bg=COLOR_PRINCIPAL, fg="white"))
    
    def colores(self):
        self.barra_superior = Frame(self, bg="#1f2329", height=50)
        self.barra_superior.pack(side=tk.TOP, fill="both")
        
        self.menu_lateral = Frame(self, bg=COLOR_PRINCIPAL, width=300, height=50)
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)
        
        self.pagina = Frame(self, bg=COLOR_PAGINA,width= 150)
        self.pagina.pack(side=tk.RIGHT, fill="both", expand=True)

    def menuPersona(self):
        for widget in self.pagina.winfo_children():
            widget.destroy()

        headerFrame = Frame(self.pagina, bg=self.pagina['bg'])
        headerFrame.pack(fill='x', pady=5)

        # GRID DEL FRAME DE ARRIBA
        headerFrame.columnconfigure(0, weight=1)
        headerFrame.columnconfigure(1, weight=1)
        headerFrame.columnconfigure(2, weight=1)

        label = Label(headerFrame, text="LISTA DE PERSONAS", font=("Roboto", 12), bg=self.pagina['bg'])
        label.grid(row=0, column=1, pady=5)

        # FILTRADORES
        opciones = [
            "Toda las Personas",
            "Solo Activos",
            "Propietarios",
            "Veterinarios"
        ]
        valor = StringVar()
        valor.set(opciones[1])

        def actualizarFiltro(*args):
            seleccion = valor.get()
            if seleccion == "Solo Activos":
                self.mostrarActivos()
            elif seleccion == "Propietarios":
                self.mostrarTipoPersona("CLI")
            elif seleccion == "Veterinarios":
                self.mostrarTipoPersona("EMP")
            else:
                self.actualizarVistaPersonas()

        valor.trace("w", actualizarFiltro) 

        menuFiltros = OptionMenu(headerFrame, valor, *opciones)
        menuFiltros.grid(row=0, column=2, padx=10, sticky='e') 

        self.vista_personas = VistaPersona(self.pagina)
        self.vista_personas.pack(fill="both", expand=True)

        self.mostrarActivos()

        Button(self.pagina, text="Cargar Nueva Persona", command=self.vista_personas.registrarPersona, bg="white", fg="red", font=("Roboto", 12), bd=0).pack(pady=8, padx=20, fill="x")

        Button(self.pagina, text="Cambiar Estado de Persona", command=self.abrir_cambiar_estado, bg="white", fg="red", font=("Roboto", 12), bd=0).pack(pady=3, padx=20, fill="x")

        Button(self.pagina, text="Cambiar Persona", command=self.vista_personas.cambiarPersona, bg="white", fg="red", font=("Roboto", 12), bd=0).pack(pady=3, padx=20, fill="x")


    
    def actualizarVistaPersonas(self):
        listaPersonas = ControladorPersona.cargarPersona([])
        self.vista_personas.mostrar_persona(listaPersonas)

    def mostrarActivos(self):
        listaPersonas = ControladorPersona.cargarActivos([])
        self.vista_personas.mostrar_persona(listaPersonas)

    def mostrarTipoPersona(self, condition):
        listaPersonas = ControladorPersona.cargarTipoPersona([], condition)
        self.vista_personas.mostrar_persona(listaPersonas)

    def menuMascota(self):
        for widget in self.pagina.winfo_children():
            widget.destroy()

        Label(self.pagina, text="LISTA DE MASCOTAS", font=(fuente, 12), bg=self.pagina['bg']).pack(pady=5)

        self.vista_mascotas = VistaMascota(self.pagina)
        self.vista_mascotas.pack(fill="both", expand=True)

        self.actualizarVistaMascota()

        Button(self.pagina, text="Cargar Nueva Mascota", command=self.vista_mascotas.crearMascota, bg="white", fg="red", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="Cambiar Estado", command=self.cambiarEstadoMascota, bg="white", fg="red", font=("Roboto", 10), bd=0).pack(pady=10, padx=20, fill="x")
        Button(self.pagina, text="Cambiar Mascota",command=self.vista_mascotas.cambiarMascota, bg="white", fg="red", font=("Roboto", 11), bd=0).pack(pady=3, padx=20, fill="x")

    def actualizarVistaMascota(self):
        listaMascota = ControladorMascota.cargarMascotas([])
        self.vista_mascotas.mostrar_mascotas(listaMascota)
        
    def cambiarEstadoMascota(self): 
        cambiar_estado_ventana = Toplevel(self)
        cambiar_estado_ventana.title("Cambiar Estado de Mascota")
        cambiar_estado_ventana.geometry("400x200")

        label_nombre = Label(cambiar_estado_ventana, text="NOMBRE DE LA MASCOTA QUE DESEA CAMBIAR")
        label_nombre.pack(pady=5)

        entry_nombre = Entry(cambiar_estado_ventana)
        entry_nombre.pack(pady=5)

        label_mensaje = Label(cambiar_estado_ventana, text="", fg="red")
        label_mensaje.pack(pady=5)

        btn_cambiar_estado = Button(cambiar_estado_ventana, text="Cambiar Estado", command=lambda: self.controladorMascota.cambiarEstadoMascota(entry_nombre.get(), label_mensaje))
        btn_cambiar_estado.pack(pady=20)    

    def abrir_cambiar_estado(self): #podriamos hacer polimosrfismo para usar esta ventana para cambiar los estados de todo
        cambiar_estado_ventana = Toplevel(self)
        cambiar_estado_ventana.title("Cambiar Estado de Persona")
        cambiar_estado_ventana.geometry("550x200")
        cambiar_estado_ventana.config(background=COLOR_PRINCIPAL)

        label_documento = Label(cambiar_estado_ventana, text="DOCUMENTO DE LA PERSONA QUE DESEA CAMBIAR", fg="white", bg=COLOR_PRINCIPAL, font=("robot", 10))
        label_documento.pack(pady=5)

        entry_documento = Entry(cambiar_estado_ventana)
        entry_documento.pack(pady=5)

        label_mensaje = Label(cambiar_estado_ventana, text="", fg="red", bg="#2a3138")
        label_mensaje.pack(pady=5)

        btn_cambiar_estado = Button(cambiar_estado_ventana, text="Cambiar Estado", command=lambda: self.controladorPersona.cambiarEstadoPersona(entry_documento.get(), label_mensaje))
        btn_cambiar_estado.pack(pady=20)

    def menuTratamiento(self):
        for widget in self.pagina.winfo_children():
            widget.destroy()
    def menuDiagnostico(self):
        for widget in self.pagina.winfo_children():
            widget.destroy()

        Label(self.pagina, text="LISTA DE DIAGNOSTICOS", font=("Roboto", 12), bg=self.pagina['bg']).pack(pady=5)

        self.vista_diagnostico = VistaDiagnostico(self.pagina)
        self.vista_diagnostico.pack(fill="both", expand=True)

        self.actualizarVistaDiagnostico()

        Button(self.pagina, text="Cargar Nuevo Diagnóstico", command=self.vista_diagnostico.cargarNuevoDiagnostico, bg="white", fg="red", font=("Roboto", 12), bd=0).pack(pady=8, padx=20, fill="x")

        Button(self.pagina, text="Cambiar Estado de Diagnóstico", command=self.cambiarEstadoDiagnostico, bg="white", fg="red", font=("Roboto", 12), bd=0).pack(pady=3, padx=20, fill="x")

    def actualizarVistaDiagnostico(self):
        listaDiagnostico = ControladorDiagnostico.cargarDiagnostico([])
        self.vista_diagnostico.mostrar_Diagnostico(listaDiagnostico)

    def cambiarEstadoDiagnostico(self): 
        cambiar_estado_ventana = Toplevel(self)
        cambiar_estado_ventana.title("Cambiar Estado de Diagnostico")
        cambiar_estado_ventana.geometry("450x250")

        label_nombre = Label(cambiar_estado_ventana, text="NOMBRE DE LA MASCOTA QUE DESEA CAMBIAR")
        label_nombre.pack(pady=5)

        entry_nombre = Entry(cambiar_estado_ventana)
        entry_nombre.pack(pady=5)

        label_propietario = Label(cambiar_estado_ventana, text="ID DEL DUEÑO DE LA MASCOTA")
        label_propietario.pack(pady=5)

        entry_propietario = Entry(cambiar_estado_ventana)
        entry_propietario.pack(pady=5)

        label_mensaje = Label(cambiar_estado_ventana, text="", fg="red")
        label_mensaje.pack(pady=5)

        btn_cambiar_estado = Button(cambiar_estado_ventana, text="Cambiar Estado", command=lambda: self.controladorDiagnostico.cambiarEstadoDiagnostico(entry_nombre.get(),entry_propietario.get(), label_mensaje))
        btn_cambiar_estado.pack(pady=20)    


def menuTratamiento():
    ventana_tratamiento = Toplevel()
    ventana_tratamiento.title("Menú Tratamiento")
    ventana_tratamiento.geometry("300x200")

        

    menu_tratamiento = Menu()
        

    menu_tratamiento.add_command(label="Tratamientos Disponibles")
    menu_tratamiento.add_command(label="Agenda de Tratamientos")
