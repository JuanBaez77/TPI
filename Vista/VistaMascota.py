import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label, StringVar, Entry, Button
from Controllers.ControladorMascota import ControladorMascota

class VistaMascota(tk.Frame):
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
        self.treeview = ttk.Treeview(self, columns=("Nombre", "Raza", "Propietario", "Estado"), show="headings")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Raza", text="Raza")
        self.treeview.heading("Propietario", text="Propietario")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.pack(fill="both", expand=True)
        
        # CONFIGURAR LA TABLA PARA CENTRAR LOS OBJETOS
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Nombre", anchor=tk.CENTER, width=100)
        self.treeview.column("Raza", anchor=tk.CENTER, width=100)
        self.treeview.column("Propietario", anchor=tk.CENTER, width=100)
        self.treeview.column("Estado", anchor=tk.CENTER, width=100)

    def mostrar_mascotas(self, lista_mascotas):
        # LIMPIAR LA TABLA
        self.treeview.delete(*self.treeview.get_children())

        # LLENAR LA TABLA 
        for mascota in lista_mascotas:
            self.treeview.insert("", "end", values=(mascota.get_nombre(),mascota.get_raza(),mascota.get_propietario(),mascota.get_estado())) 

    def crearMascota(self):
        registro = Toplevel()
        registro.geometry("650x550")
        registro.title("Registro")
        registro.resizable(False, False)
        registro.config(background="#2a3138")
        tituloRegistro = Label(registro, text="Registrar Mascota", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()

        # CREAMOS LAS ENTRADAS
        nombre = Label(registro, text="Nombre:", bg="#2a3138", fg="white").place(x=22, y=70)
        raza = Label(registro, text="Raza:", bg="#2a3138", fg="white").place(x=22, y=130)
        propietario = Label(registro, text="Propietario:", bg="#2a3138", fg="white").place(x=22, y=190)
        estado = Label(registro, text="Estado", bg="#2a3138", fg="white").place(x=22, y=250)
        
        nombre = StringVar()
        raza = StringVar()
        propietario = StringVar()
        estado = StringVar()
        
        newMascota = [nombre, raza, propietario, estado]

        entryNombre = Entry(registro, textvariable=nombre, width="35").place(x=22, y=100)
        entryApellido = Entry(registro, textvariable=raza, width="35").place(x=22, y=160)
        entryDocumento = Entry(registro, textvariable=propietario, width="35").place(x=22, y=280)
        entryTelefono = Entry(registro, textvariable=estado, width="35").place(x=22, y=340)
        
        submit = Button(registro, text="Registrar", command=lambda: self.guardarMascota(newMascota, registro), width=30)
        submit.place(x=22, y=450)

    def guardarMascota(self, newPersona, registro):
        ControladorMascota.guardarMascota(newPersona, registro)