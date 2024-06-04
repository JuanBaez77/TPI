import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Toplevel, Label, StringVar, Entry, Button, OptionMenu
from Controllers.ControladorDiagnostico import ControladorDiagnostico


class VistaDiagnostico(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.lista_Diagnostico = []
    
        # CREAR UN ESTILO PARA LA TABLA
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="", foreground="red", font=("Roboto", 12, "bold"))
        
        # APLICAR EL ESTILO
        self.treeview = ttk.Treeview(self.master, style="Treeview")
        
        # CREAR LA TABLA
        self.treeview = ttk.Treeview(self, columns=("Nombre", "Diagnostico", "Propietario", "Estado"), show="headings")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Diagnostico", text="Diagnostico")
        self.treeview.heading("Propietario", text="Propietario")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.pack(fill="both", expand=True)
        
        # CONFIGURAR LA TABLA PARA CENTRAR LOS OBJETOS
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Nombre", anchor=tk.CENTER, width=100)
        self.treeview.column("Diagnostico", anchor=tk.CENTER, width=100)
        self.treeview.column("Propietario", anchor=tk.CENTER, width=100)
        self.treeview.column("Estado", anchor=tk.CENTER, width=100)

    def mostrar_Diagnostico(self, lista_Diagnostico):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        
        for diagnostico in lista_Diagnostico:
            nombre = diagnostico.get_nombre()
            diagnostico_val = diagnostico.get_diagnostico()
            propietario = diagnostico.get_propietario()
            estado = diagnostico.get_estado().strip().lower()
            estado_color = "green" if estado == "true" else "red"
            self.treeview.insert("", "end", values=(nombre, diagnostico_val, propietario, estado))
            self.treeview.item(self.treeview.get_children()[-1], tags=(estado_color,))
        
        self.treeview.tag_configure('green', background='#f0f0f0', foreground='black')
        self.treeview.tag_configure('red', background='lightcoral', foreground='black')

    def cargarNuevoDiagnostico(self):
        # CREAMOS LA VENTANA PARA EL REGISTRO DE DIAGNOSTICOS
        registro = Toplevel()
        registro.geometry("650x550")
        registro.title("Registrar Diagnostico")
        registro.resizable(False, False)
        registro.config(background="#2a3138")
        tituloRegistro = Label(registro, text="Registrar Diagnostico", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()

        # CREAMOS LAS ENTRADAS
        nombre = StringVar()
        diagnostico = StringVar()
        propietario = StringVar()
        
        newDiagnostico = [nombre,diagnostico,propietario,True]

        Label(registro, text="Nombre:", bg="#2a3138", fg="white").place(x=22, y=70)
        Label(registro, text="Agregar un nuevo diagnostico:", bg="#2a3138", fg="white").place(x=390, y=130)
        Label(registro, text="Selecciona un Diagnostico:", bg="#2a3138", fg="white").place(x=22, y=130)
        Label(registro, text="Propietario:", bg="#2a3138", fg="white").place(x=22, y=190)

        entryNombre = Entry(registro, textvariable=nombre, width="35").place(x=22, y=100)
        entryDiagnostico = Entry(registro, textvariable=diagnostico, width="35").place(x=350, y=160)

        listaPropietario = self.mostrarPropietario()
        entryPropietario = OptionMenu(registro, propietario, *listaPropietario)
        entryPropietario.place(x=22, y=220)
        entryPropietario.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138", highlightcolor="#2a3138")

        # BOTON PARA MOSTRAR LOS DIAGNOSTICOS ALMACENADOS EN EL CSV
        listaDiagnostico = self.mostrarDiagnostico()
        entryTipoDiagnostico = OptionMenu(registro, diagnostico, *listaDiagnostico) 
        entryTipoDiagnostico.place(x=22, y=155)
        entryTipoDiagnostico.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138", highlightcolor="#2a3138")
        
        # BOTON PARA GUARDAR EL DIAGNOSTICO EN EL CSV
        enviar = Button(registro, text="Registrar", command=lambda: self.guardarNuevoDiagnostico(newDiagnostico, registro), width=30, bg="#18BC9C")
        enviar.place(x=22, y=450)

    def guardarNuevoDiagnostico(self, newDiagnostico):
        # CON ESTE METODO GUARDAMOS EL DIAGNOSTICO EN EL CSV
        ControladorDiagnostico.guardarDiagnostico(newDiagnostico)
        
    def mostrarDiagnostico(self):
        # CON ESTE METODO MOSTRAMOS LOS DIAGNOSTICOS ALMACENADOS 
        listaDiagnosticosDisponibles = []
        lista = ControladorDiagnostico.cargarDiagnostico(self) 
        for diagnostico in lista:
            listaDiagnosticosDisponibles.append(diagnostico)  
        return listaDiagnosticosDisponibles
    
    def mostrarPropietario(self):
        # CON ESTE METODO MOSTRAMOS LOS DIAGNOSTICOS ALMACENADOS 
        listaPopietariosDisponibles = []
        lista = ControladorDiagnostico.cargarDiagnostico(self) 
        for propietario in lista:
            listaPopietariosDisponibles.append(propietario)  
        return listaPopietariosDisponibles