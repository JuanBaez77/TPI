import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Toplevel, Label, StringVar, Entry, Button, OptionMenu
from Controllers.ControladorDiagnostico import ControladorDiagnostico
from Controllers.ControladorPersona import ControladorPersona

class VistaDiagnostico(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.lista_Diagnostico = []
        self.controlador = ControladorDiagnostico
    
        # CREAR UN ESTILO PARA LA TABLA
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="", foreground="red", font=("Roboto", 12, "bold"))
        
        # APLICAR EL ESTILO
        self.treeview = ttk.Treeview(self.master, style="Treeview")
        
        # CREAR LA TABLA
        self.treeview = ttk.Treeview(self, columns=("Nombre", "Diagnostico", "Propietario", "Estado","ID"), show="headings")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Diagnostico", text="Diagnostico")
        self.treeview.heading("Propietario", text="Propietario")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.heading("ID", text="ID")
        self.treeview.pack(fill="both", expand=True)
        
        # CONFIGURAR LA TABLA PARA CENTRAR LOS OBJETOS
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Nombre", anchor=tk.CENTER, width=100)
        self.treeview.column("Diagnostico", anchor=tk.CENTER, width=100)
        self.treeview.column("Propietario", anchor=tk.CENTER, width=100)
        self.treeview.column("Estado", anchor=tk.CENTER, width=100)
        self.treeview.column("ID", anchor=tk.CENTER, width=100)

    def mostrar_Diagnostico(self, lista_Diagnostico):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        
        for diagnostico in lista_Diagnostico:
            nombre = diagnostico.get_nombre()
            diagnostico_val = diagnostico.get_diagnostico()
            propietario = diagnostico.get_propietario()
            estado = diagnostico.get_estado().strip().lower()
            id = diagnostico.get_id()
            estado_color = "green" if estado == "true" else "red"
            self.treeview.insert("", "end", values=(nombre, diagnostico_val, propietario, estado,id))
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

        entryDiagnostico = Entry(registro, textvariable=diagnostico, width="35").place(x=350, y=160)

        listamascota = self.mostrarMascota()
        entrynombre = OptionMenu(registro, nombre, *listamascota)
        entrynombre.place(x=22, y=95)
        entrynombre.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138", highlightcolor="#2a3138")

        listaPropietario = self.mostrarID()
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

    def guardarNuevoDiagnostico(self, newDiagnostico, registro):
        ControladorDiagnostico.guardarDiagnostico(self,newDiagnostico, registro)
        
    def mostrarDiagnostico(self):
        # CON ESTE METODO MOSTRAMOS LOS DIAGNOSTICOS ALMACENADOS 
        listaDiagnosticosDisponibles = []
        lista = ControladorDiagnostico.cargarDiagnosticos(self) 
        for diagnostico in lista:
            listaDiagnosticosDisponibles.append(diagnostico)  
        return listaDiagnosticosDisponibles
    
    def mostrarID(self):
        # CON ESTE METODO MOSTRAMOS LOS DIAGNOSTICOS ALMACENADOS 
        listaPopietariosDisponibles = []
        lista = ControladorDiagnostico.cargarID(self) 
        for propietario in lista:
            listaPopietariosDisponibles.append(propietario)  
        return listaPopietariosDisponibles

    def mostrarMascota(self):
        # CON ESTE METODO MOSTRAMOS LOS DIAGNOSTICOS ALMACENADOS 
        listaMascotasDisponibles = []
        lista = ControladorDiagnostico.cargarMascota(self) 
        for nombre in lista:
            listaMascotasDisponibles.append(nombre)  
        return listaMascotasDisponibles
    
    def mostrarRanking(self, ranking):
        ranking_window = tk.Toplevel(self.master)
        ranking_window.title("Ranking de Diagnósticos")

        treeview_ranking = ttk.Treeview(ranking_window, columns=("Diagnostico", "Cantidad de Diagnósticos"), show="headings")
        treeview_ranking.heading("Diagnostico", text="Diagnostico")
        treeview_ranking.heading("Cantidad de Diagnósticos", text="Cantidad de Diagnósticos")
        treeview_ranking.pack(fill="both", expand=True)

        # Agregar los datos del ranking a la tabla
        for mascota, cantidad in ranking:
            treeview_ranking.insert("", "end", values=(mascota, cantidad))

    def mostrarCantidadRazasPorDiagnostico(self, razas_por_diagnostico):
        raza_window = tk.Toplevel(self.master)
        raza_window.title("Cantidad de Diagnósticos por Raza")

        treeview_raza = ttk.Treeview(raza_window, columns=("Raza", "Cantidad"), show="headings")
        treeview_raza.heading("Raza", text="Raza")
        treeview_raza.heading("Cantidad", text="Cantidad")
        treeview_raza.pack(fill="both", expand=True)

        for raza, cantidad in razas_por_diagnostico.items():
            treeview_raza.insert("", "end", values=(raza, cantidad))

    def cambiarDiag(self):
        ventana = Toplevel()
        ventana.geometry("300x350")
        ventana.title("Cambiar Persona")
        ventana.resizable(False, False)
        ventana.config(background="#2a3138")

        tituloVentana = Label(ventana, text="Cambiar Diagnostico", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()
        idVar = StringVar()
        idEntry = Entry(ventana, textvariable=idVar, width="35"). place(x=22, y=80)
        Label(ventana, text="ID de la mascota:", bg="#2a3138", fg="white").place(x=22, y=60)

        opciones = [
            "Diagnostico"
        ]
        valor = StringVar()
        valor.set(opciones[0])

        OptionMenu(ventana, valor, *opciones).place(x=22, y=120)
        cambio = StringVar()
        entryCambio = Entry(ventana, textvariable=cambio, width="35").place(x=22, y=180)
        Label(ventana, text="Nuevo Valor:", bg="#2a3138", fg="white").place(x=22, y=160)
        label_mensaje = Label(ventana, text="", fg="white", bg="#2a3138", font=("roboto", 10))
        label_mensaje.place(x=22, y=260)
        def actualizarDiag(*args):
            seleccion = valor.get()
            if seleccion == "Diagnostico":
                selecCambio = 1
            campo = selecCambio
            resultado = self.controlador.cambiarDiagnostico(self.controlador.cargarDiagnostico([]), idVar.get(), campo, cambio.get(),label_mensaje)
        Button(ventana, text="Cambiar", command=actualizarDiag, width=30).place(x=22, y=220)