import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label, StringVar, Entry, Button, OptionMenu
from Controllers.ControladorTratamiento import ControladorVacuna
class VistaVacuna(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.lista_vacuna = []
        self.controlador = ControladorVacuna(self, self.mostrar_vacunas)
    
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

    def cambiarVacuna(self):
        ventana = Toplevel()
        ventana.geometry("300x400")
        ventana.title("Cambiar Vacuna")
        ventana.resizable(False,False)
        ventana.config(background="#2a3138")

        tituloVentana = Label(ventana, text="Cambiar Vacuna", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()
        cambio = StringVar()
        entryCambio = Entry(ventana,textvariable=cambio, width="35").place(x=22, y=340)

        opciones = [
            "Nombre",
            "Descripcion"
        ]
        valor = StringVar()
        valor.set(opciones[0])
        def actualizarVacuna(*args):
            seleccion = valor.get()
            if seleccion == "Nombre":
                selecCambio = "nombre"
            else:
                selecCambio = "Descripcion"
            return selecCambio
        cambioEntry = actualizarVacuna() 

        menuCambios = OptionMenu(ventana, valor, *opciones).pack()
        submit = Button(cambio, text="Cambiar", command=lambda: self.controlador.guardarVacuna(cambioEntry, ventana), width=30)

    def mostrar_vacunas(self, lista_vacunas):
        # LIMPIAR LA TABLA
        self.treeview.delete(*self.treeview.get_children())

        # LLENAR LA TABLA 
        for vacuna in lista_vacunas:
            estado_color = "green" if vacuna.get_estado() == "True" else "red"
            self.treeview.insert("", "end", values=(vacuna.get_nombre(),vacuna.get_descripcion(),vacuna.get_estado()), tags=('#2dc426' if vacuna.get_estado() == "True" else 'red')) 
        # APLICAR ESTILOS
            self.treeview.tag_configure('green', background='lightgreen', foreground='black')
            self.treeview.tag_configure('red', background='lightcoral', foreground='black')

    def crearVacuna(self):
        # CREAMOS LA VENTANA PARA EL REGISTRO DE VACUNAS
        registro = Toplevel()
        registro.geometry("650x550")
        registro.title("Registro")
        registro.resizable(False, False)
        registro.config(background="#2a3138")
        tituloRegistro = Label(registro, text="Registrar Vacuna", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()

        # CREAMOS LAS ENTRADAS
        nombre = Label(registro, text="Nombre:", bg="#2a3138", fg="white").place(x=22, y=70)
        descripcion = Label(registro, text="Descripción:", bg="#2a3138", fg="white").place(x=22, y=170)
        
        nombre = StringVar()
        descripcion = StringVar()
        
        # CREAMOS LA LISTA PARA LUEGO CREAR EL OBJETO
        newVacuna = [nombre, descripcion, True]

        entryNombre = Entry(registro, textvariable=nombre, width="35").place(x=22, y=100)
        entryDescripcion = Entry(registro, textvariable=descripcion, width="35").place(x=22, y=200)

        # BOTON PARA GUARDAR LOS TRATAMIENTOS EN EL CSV
        enviarVacuna = Button(registro, text="Cargar Vacuna", command=lambda: self.controlador.guardarVacuna(newVacuna,registro), width=20, bg="#18BC9C")
        enviarVacuna.place(x=22, y=400)
        
    def guardarVacuna(self, newVacuna, registro):
        # CON ESTE METODO GUARDAMOS LA VACUNA EN EL CSV
        ControladorVacuna.guardarVacuna(newVacuna, registro)
        
    def mostrarVacuna(self):
        # CON ESTE METODO MOSTRAMOS LAS VACUNAS ALMACENADAS 
        listaVacunasDisponibles = []
        lista = ControladorVacuna.cargarVacunas(self) #LLAMAMOS AL METODO PARA OBTENER LA LISTA CON LAS VACUNAS
        for vacuna in lista:
                listaVacunasDisponibles.append(vacuna[0])
        return listaVacunasDisponibles