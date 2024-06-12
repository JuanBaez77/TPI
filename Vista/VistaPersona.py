import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label, StringVar, Entry, Button, OptionMenu
from Controllers.ControladorPersona import ControladorPersona

class VistaPersona(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.lista_personas = []
        self.controlador = ControladorPersona
    
        # CREAR UN ESTILO PARA LA TABLA
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="", foreground="red", font=("Roboto", 12, "bold"))
        
        # APLICO EL ESTILO
        self.treeview = ttk.Treeview(self.master, style="Treeview")
        
        # CREAR LA TABLA
        self.treeview = ttk.Treeview(self, columns=("Nombre", "Documento", "Telefono", "Estado"), show="headings")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Documento", text="Documento")
        self.treeview.heading("Telefono", text="Telefono")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.pack(fill="both", expand=True)
        
        # CONFIGURAR LA TABLA PARA CENTRAR LOS OBJETOS
        self.treeview.column("#0", width=0, stretch=tk.NO)


        
        self.treeview.column("Nombre", anchor=tk.CENTER, width=100)
        self.treeview.column("Documento", anchor=tk.CENTER, width=100)
        self.treeview.column("Telefono", anchor=tk.CENTER, width=100)
        self.treeview.column("Estado", anchor=tk.CENTER, width=100)
    
    def mostrar_persona(self, lista_personas):
        # LIMPIAR LA TABLA
        self.treeview.delete(*self.treeview.get_children())

        # LLENAR LA TABLA 
        for persona in lista_personas:
            nombre_completo = f"{persona.getNombre()} {persona.getApellido()}"
            estado_color = "green" if persona.getEstado() == "True" else "red"
            self.treeview.insert("", "end", values=(nombre_completo, persona.getDocumento(), persona.getTelefono(), persona.getEstado()), tags=('green' if persona.getEstado() == "True" else 'red'))

        # Aplicar estilos
        self.treeview.tag_configure('green', background='#f0f0f0', foreground='black')
        self.treeview.tag_configure('red', background='lightcoral', foreground='black')

    def cambiarPersona(self):
        ventana = Toplevel()
        ventana.geometry("300x350")
        ventana.title("Cambiar Persona")
        ventana.resizable(False, False)
        ventana.config(background="#2a3138")

        tituloVentana = Label(ventana, text="Cambiar Persona", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()
        idVar = StringVar()
        idEntry = Entry(ventana, textvariable=idVar, width="35"). place(x=22, y=80)
        Label(ventana, text="ID de la persona:", bg="#2a3138", fg="white").place(x=22, y=60)

        opciones = [
            "Nombre",
            "Apellido",
            "Documento",
            "Telefono"
        ]
        valor = StringVar()
        valor.set(opciones[0])

        OptionMenu(ventana, valor, *opciones).place(x=22, y=120)
        cambio = StringVar()
        entryCambio = Entry(ventana, textvariable=cambio, width="35").place(x=22, y=180)
        Label(ventana, text="Nuevo Valor:", bg="#2a3138", fg="white").place(x=22, y=160)
        label_mensaje = Label(ventana, text="", fg="white", bg="#2a3138", font=("roboto", 10))
        label_mensaje.place(x=22, y=260)
        def actualizarPersona(*args):
            seleccion = valor.get()
            if seleccion == "Nombre":
                selecCambio = 1
            elif seleccion == "Apellido":
                selecCambio = 2
            elif seleccion == "Documento":
                selecCambio = 4
            else:
                selecCambio = 5
            campo = selecCambio
            resultado = self.controlador.cambiarPersona(self.controlador.cargarPersona([]), idVar.get(), campo, cambio.get(),label_mensaje)

        Button(ventana, text="Cambiar", command=actualizarPersona, width=30).place(x=22, y=220)

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

        entryTipoPersona = OptionMenu(registro, tipoPersona, "CLI", "EMP")
        entryTipoPersona.place(x=22, y=400)
        entryTipoPersona.config(font=("Roboto", 9), bg="#2a3138", fg="white", highlightbackground="#3e444e", highlightcolor="#3e444e")

        entryTipoDocumento = OptionMenu(registro, tipoDocumento, "DNI", "PAS")
        entryTipoDocumento.place(x=22, y=210)
        
        entryTipoDocumento.config(font=("Roboto", 9), bg="#2a3138", fg="white", highlightbackground="#3e444e", highlightcolor="#3e444e")

        submit = Button(registro, text="Registrar", command=lambda: self.guardarPersona(newPersona, registro), width=30)
        submit.place(x=22, y=450)

    def guardarPersona(self, newPersona, registro):
        ControladorPersona.guardarPersona(newPersona, registro)