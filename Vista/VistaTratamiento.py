import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label, StringVar, Entry, Button, OptionMenu
from Controllers.ControladorTratamiento import ControladorTratamiento

class VistaTratamiento(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.lista_mascotas = []
    
        # CREAR UN ESTILO PARA LA TABLA
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="", foreground="red", font=("Roboto", 12, "bold"))
        
        # APLICO EL ESTILO
        self.treeview = ttk.Treeview(self.master, style="Treeview")
        
        # CREAR LA TABLA
        self.treeview = ttk.Treeview(self, columns=("Nombre", "Destino", "Estado"), show="headings")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Destino", text="Destino")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.pack(fill="both", expand=True)
        
        # CONFIGURAR LA TABLA PARA CENTRAR LOS OBJETOS
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Nombre", anchor=tk.CENTER, width=100)
        self.treeview.column("Destino", anchor=tk.CENTER, width=100)
        self.treeview.column("Estado", anchor=tk.CENTER, width=100)

    def mostrar_tratamientos(self, lista_tratamientos):
        # LIMPIAR LA TABLA
        self.treeview.delete(*self.treeview.get_children())

        # LLENAR LA TABLA 
        for tratamiento in lista_tratamientos:
            estado_color = "green" if tratamiento.get_estado() == "True" else "red"
            self.treeview.insert("", "end", values=(tratamiento.get_nombre(),tratamiento.get_destino(),tratamiento.get_estado()), tags=('#2dc426' if tratamiento.get_estado() == "True" else 'red')) 
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
        nuevaRaza = Label(registro, text="Agregar una Raza nueva:", bg="#2a3138", fg="white").place(x=390, y=130)
        raza = Label(registro, text="Selecciona una Raza:", bg="#2a3138", fg="white").place(x=22, y=130)
        propietario = Label(registro, text="Propietario:", bg="#2a3138", fg="white").place(x=22, y=190)

        nuevaRaza = StringVar()
        nombre = StringVar()
        raza = StringVar()
        raza.set("Raza")
        propietario = StringVar()
        propietario.set("Propietario")
        
        # CREAMOS LA LISTA PARA LUEGO CREAR EL OBJETO
        newMascota = [nombre, raza, propietario, True]
        newRaza = raza

        entryNombre = Entry(registro, textvariable=nombre, width="35").place(x=22, y=100)
        entryRaza = Entry(registro, textvariable=raza, width="35").place(x=350, y=160)

        listaPropietario = self.monstrarPropietario()
        entryPropietario = OptionMenu(registro, propietario, *listaPropietario)
        entryPropietario.place(x=22, y=220)
        entryPropietario.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138", highlightcolor="#2a3138")


        # BOTON PARA MOSTRAR LAS RAZAS ALMACENADAS EN EL CSV
        listaRaza = self.mostrarRaza()
        entryTipoRaza = OptionMenu(registro, raza, *listaRaza) 
        entryTipoRaza.place(x=22, y=155)
        entryTipoRaza.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138", highlightcolor="#2a3138")
        
        # BOTON PARA GUARDAR LAS RAZA EN EL CSV
        enviarRaza = Button(registro, text="Cargar Raza", command=lambda: self.guardarRaza(newRaza), width=20, bg="#18BC9C")
        enviarRaza.place(x=380, y=190)
        
        # BOTON PARA GUARDAR LA MASCOTA EN EL CSV
        enviar = Button(registro, text="Registrar", command=lambda: self.guardarMascota(newMascota, registro), width=30, bg="#18BC9C")
        enviar.place(x=22, y=450)

    def guardarMascota(self, newPersona, registro):
        # CON ESTE METODO GUARDAMOS LA MASCOTA EN EL CSV
        ControladorMascota.guardarMascota(newPersona, registro)
    
    def guardarRaza(self, newRaza):
        # CON ESTE METODO GUARDAMOS LA RAZA EN EL CSV
        ControladorMascota.guardarRaza(newRaza)
        
    def mostrarRaza(self):
        # CON ESTE METODO MOSTRAMOS LAS RAZAS ALMACENADAS 
        listaRazasDisponibles = []
        lista = ControladorMascota.cargarRazas(self) #LLAMAMOS AL METODO PARA OBTENER LA LISTA CON LAS RAZAS
        for raza in lista:
            # if raza.get_estado() == 1:
                listaRazasDisponibles.append(raza[0])
        return listaRazasDisponibles