import csv
from tkinter import messagebox, Toplevel, Label, StringVar, Entry, Button, OptionMenu
import tkinter as tk
from tkinter import ttk
from Controllers.ControladorConsulta import ControladorConsulta
from Controllers.ControladorDiagnostico import ControladorDiagnostico
from Controllers.ControladorPersona import ControladorPersona
from datetime import datetime

class VistaConsulta(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.consulta = ControladorConsulta

        # CREAR UN ESTILO PARA LA TABLA
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="", foreground="red", font=("Roboto", 12, "bold"))

        # APLICAR EL ESTILO
        self.treeview = ttk.Treeview(self.master, style="Treeview")

        # CREAR LA TABLA
        self.treeview = ttk.Treeview(self, columns=("Mascota", "Fecha", "Veterinario"), show="headings")
        self.treeview.heading("Mascota", text="Mascota")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Veterinario", text="Veterinario")
        self.treeview.pack(fill="both", expand=True)

        # CONFIGURAR LA TABLA PARA CENTRAR LOS OBJETOS
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Mascota", anchor=tk.CENTER, width=100)
        self.treeview.column("Fecha", anchor=tk.CENTER, width=100)
        self.treeview.column("Veterinario", anchor=tk.CENTER, width=100)

    def mostrarconsulta(self, lista_consulta):
        self.treeview.delete(*self.treeview.get_children())

        for consulta in lista_consulta:
            nombremascota = consulta.get_nombremascota()
            fecha = consulta.get_fecha()
            veterinario = consulta.get_veterinario()
            self.treeview.insert("", "end", values=(nombremascota,fecha,veterinario))

    def cargarNuevoConsulta(self):
        registro = Toplevel()
        registro.geometry("650x550")
        registro.title("Registrar Consulta")
        registro.resizable(False, False)
        registro.config(background="#2a3138")
        tituloRegistro = Label(registro, text="Registrar Consulta", font=("Roboto", 15), bg="#3e444e", fg="white", width="550", height="2").pack()

        # CREAMOS LAS ENTRADAS
        veterinario = StringVar()
        nombre = StringVar()
        diagnostico = StringVar()
        tratamiento = StringVar()
        vacunas = StringVar()
        observacion = StringVar()
        fecha = datetime.today()

        newConsulta = [fecha,nombre,diagnostico,veterinario,tratamiento,vacunas,observacion]

        Label(registro, text="Veterinario:", bg="#2a3138", fg="white").place(x=22, y=70)
        Label(registro, text="Tratamiento:", bg="#2a3138", fg="white").place(x=390, y=130)
        Label(registro, text="Mascota:", bg="#2a3138", fg="white").place(x=22, y=130)
        Label(registro, text="Diagnostico:", bg="#2a3138", fg="white").place(x=22, y=190)
        Label(registro, text="Vacuna:", bg="#2a3138", fg="white").place(x=390, y=180)
        Label(registro, text="Otra/Ninguna:", bg="#2a3138", fg="white").place(x=390, y=240)
        Label(registro, text="Observacion:",bg="#2a3138", fg="white").place(x=22, y=320)

        entryobservacion =  Entry(registro, textvariable=observacion, width="35").place(x=22, y=350)
        entryvacunas =  Entry(registro, textvariable=vacunas, width="35").place(x=390, y=260)
        
        listaTratamiento = self.mostrarTratamiento()
        entryTratamiento = OptionMenu(registro, tratamiento, *listaTratamiento)
        entryTratamiento.place(x=390, y=150)
        entryTratamiento.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138",
                                 highlightcolor="#2a3138")
        
        listaVacuna = self.mostrarVacunas()
        entryVacuna = OptionMenu(registro, vacunas, *listaVacuna)
        entryVacuna.place(x=390, y=200)
        entryVacuna.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138",
                                 highlightcolor="#2a3138")
        

        listaVeterinario = self.mostrarVeterinario()
        entryVeterinario = OptionMenu(registro, veterinario, *listaVeterinario)
        entryVeterinario.place(x=22, y=90)
        entryVeterinario.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138",
                                 highlightcolor="#2a3138")

        listamascota = self.mostrarMascota()
        entrynombre = OptionMenu(registro, nombre, *listamascota)
        entrynombre.place(x=22, y=155)
        entrynombre.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138",
                           highlightcolor="#2a3138")

        # BOTON PARA MOSTRAR LOS DIAGNOSTICOS ALMACENADOS EN EL CSV
        listaDiagnostico = self.mostrarDiagnostico()
        entryTipoDiagnostico = OptionMenu(registro, diagnostico, *listaDiagnostico)
        entryTipoDiagnostico.place(x=22, y=220)
        entryTipoDiagnostico.config(font=("Roboto", 9), bg="#3e444e", fg="white", highlightbackground="#2a3138",
                                    highlightcolor="#2a3138")

        # BOTON PARA GUARDAR EL DIAGNOSTICO EN EL CSV
        enviar = Button(registro, text="Registrar", command=lambda: self.guardarNuevaConsulta(newConsulta, registro),
                        width=30, bg="#18BC9C")
        enviar.place(x=22, y=450)

    def guardarNuevaConsulta(self, newConsulta, registro):
        ControladorConsulta.guardarConsulta(self, newConsulta, registro)

    def mostrarMascota(self):
        # CON ESTE METODO MOSTRAMOS LOS DIAGNOSTICOS ALMACENADOS
        listaMascotasDisponibles = []
        lista = ControladorDiagnostico.cargarMascota(self)
        for nombre in lista:
            listaMascotasDisponibles.append(nombre)
        return listaMascotasDisponibles

    def mostrarDiagnostico(self):
        # CON ESTE METODO MOSTRAMOS LOS DIAGNOSTICOS ALMACENADOS
        listaDiagnosticosDisponibles = []
        lista = ControladorDiagnostico.cargarDiagnosticos(self)
        for diagnostico in lista:
            listaDiagnosticosDisponibles.append(diagnostico)
        return listaDiagnosticosDisponibles

    def mostrarVeterinario(self):
        listaVeterinarioDisponibles = []
        lista = ControladorConsulta.cargarVeterinario(self)
        for veterinario in lista:
            listaVeterinarioDisponibles.append(veterinario)
        return listaVeterinarioDisponibles

    def mostrarTratamiento(self):
        listatratemientoDisponibles = []
        lista = ControladorConsulta.cargarTratamiento(self)
        for Tratamiento in lista:
            listatratemientoDisponibles.append(Tratamiento)
        return listatratemientoDisponibles
    
    def mostrarVacunas(self):
        listavacunasDisponibles = []
        lista = ControladorConsulta.cargarVacunas(self)
        for Vacunas in lista:
            listavacunasDisponibles.append(Vacunas)
        return listavacunasDisponibles