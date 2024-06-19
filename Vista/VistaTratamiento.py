import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label, StringVar, Entry, Button, OptionMenu
from Controllers.ControladorTratamiento import ControladorTratamiento

class VistaTratamiento(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.lista_tratamiento = []
        self.controlador = ControladorTratamiento(self, self.mostrar_tratamientos)
    
        # CREAR UN ESTILO PARA LA TABLA
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="", foreground="red", font=("Roboto", 12, "bold"))
        
        # APLICO EL ESTILO
        self.treeview = ttk.Treeview(self.master, style="Treeview")
        
        # CREAR LA TABLA
        self.treeview = ttk.Treeview(self, columns=("Nombre", "Descripcion", "Estado"), show="headings")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Descripcion", text="Descripcion")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.pack(fill="both", expand=True)
        
        # CONFIGURAR LA TABLA PARA CENTRAR LOS OBJETOS
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Nombre", anchor=tk.CENTER, width=100)
        self.treeview.column("Descripcion", anchor=tk.CENTER, width=100)
        self.treeview.column("Estado", anchor=tk.CENTER, width=100)

    def mostrar_tratamientos(self, lista_tratamientos):
        # LIMPIAR LA TABLA
        self.treeview.delete(*self.treeview.get_children())

        # LLENAR LA TABLA 
        for tratamiento in lista_tratamientos:
            estado_color = "green" if tratamiento.get_estado() == "True" else "red"
            self.treeview.insert("", "end", values=(tratamiento.get_nombre(),tratamiento.get_descripcion(),tratamiento.get_estado()), tags=('#2dc426' if tratamiento.get_estado() == "True" else 'red')) 
        # APLICAR ESTILOS
            self.treeview.tag_configure('green', background='lightgreen', foreground='black')
            self.treeview.tag_configure('red', background='lightcoral', foreground='black')

    def crearTratamiento(self):
        # CREAMOS LA VENTANA PARA EL REGISTRO DE TRATAMIENTOS
        registro = Toplevel()
        registro.geometry("650x550")
        registro.title("Registro")
        registro.resizable(False, False)
        registro.config(background="#2a3138")
        tituloRegistro = Label(registro, text="Registrar Tratamiento", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()

        # CREAMOS LAS ENTRADAS
        nombre = Label(registro, text="Nombre:", bg="#2a3138", fg="white").place(x=22, y=70)
        descripcion = Label(registro, text="Descripción:", bg="#2a3138", fg="white").place(x=22, y=170)

        nombre = StringVar()
        descripcion = StringVar()
        
        # CREAMOS LA LISTA PARA LUEGO CREAR EL OBJETO
        newTratamiento = [nombre, descripcion, True]

        entryNombre = Entry(registro, textvariable=nombre, width="35").place(x=22, y=100)
        entryDescripcion = Entry(registro, textvariable=descripcion, width="35").place(x=22, y=200)

        # BOTON PARA GUARDAR LOS TRATAMIENTOS EN EL CSV
        enviarTratamiento = Button(registro, text="Cargar Tratatamiento", command=lambda: self.controlador.guardarTratamiento(newTratamiento,registro), width=20, bg="#18BC9C")
        enviarTratamiento.place(x=22, y=400)
        

    def guardarTratamiento(self, newTratamiento, registro):
        # CON ESTE METODO GUARDAMOS EL TRATAMIENTO EN EL CSV
        ControladorTratamiento.guardarTratamiento(newTratamiento, registro)
        
    def mostrarTratamiento(self):
        # CON ESTE METODO MOSTRAMOS LOS TRATAMIENTOS ALMACENADOS 
        listaTratamientosDisponibles = []
        lista = ControladorTratamiento.cargarTratamiento(self) #LLAMAMOS AL METODO PARA OBTENER LA LISTA CON LOS TRATAMIENTOS
        for tratamiento in lista:
                listaTratamientosDisponibles.append(tratamiento[0])
        return listaTratamientosDisponibles