from Modulos.Consulta import Consulta
import csv
from tkinter import *
from tkinter import messagebox
import datetime
class ControladorConsulta:
    def __init__(self, vista,update_callback=None):
        self.vistaConsulta = vista
        self.update_callback = update_callback

    def guardarConsulta(self, lista, registro):
        fecha_val = datetime.datetime.today().strftime("%Y-%m-%d")
        nombre_mascota_val = lista[1].get()
        diagnostico_val = lista[2].get()
        veterinario_val = lista[3].get()
        tratamiento_val = lista[4].get()
        vacunas_val = lista[5].get()
        observaciones_val = lista[6].get()

        nueva_consulta = Consulta(
            fecha_val, nombre_mascota_val, diagnostico_val, veterinario_val,
            tratamiento_val, vacunas_val, observaciones_val
        )

        nombre_mascota = nueva_consulta.get_nombremascota().replace(":", "_").replace(" ", "_")
        fecha_consulta = nueva_consulta.get_fecha().replace(" ", "_").replace(":", "_")
        filename_txt = f"{nombre_mascota}_{fecha_consulta}.txt"

        # Escribir en el archivo de texto
        with open(f"FichasMedicas/{filename_txt}", "w") as f:
            f.write("Ficha Medica\n")
            f.write(f"Nombre de la mascota: {nueva_consulta.get_nombremascota()}\n")
            f.write(f"Fecha de la consulta: {nueva_consulta.get_fecha()}\n")
            f.write(f"Veterinario que lo atendio: {nueva_consulta.get_veterinario()}\n")
            f.write(f"Diagnostico: {nueva_consulta.get_diagnostico()}\n")
            f.write(f"Tratamiento recomendado: {nueva_consulta.get_tratamiento()}\n")
            f.write(f"Vacunas: {nueva_consulta.get_vacunas()}\n")
            f.write(f"Observaciones: {nueva_consulta.get_observaciones()}\n")

        with open("csv/consultas.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                nueva_consulta.get_fecha(),
                nueva_consulta.get_nombremascota(),
                nueva_consulta.get_diagnostico(),
                nueva_consulta.get_veterinario(),
                nueva_consulta.get_tratamiento(),
                nueva_consulta.get_vacunas(),
                nueva_consulta.get_observaciones()
            ])

        registro.destroy()
        messagebox.showinfo("Éxito", "Consulta registrada con éxito")
        
    def cargarConsulta(lista=list):
        lista = []
        with open("csv/consultas.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)  
            for linea in contenido:
                fecha = linea[0]
                mascota = linea[1]
                diagnostico = linea[2]
                veterinario = linea[3]
                tratamiento = linea[4]
                vacunas = linea[0]
                observacion = linea[1]
                consultas = Consulta(fecha,mascota,diagnostico,veterinario,tratamiento,vacunas,observacion)
                lista.append(consultas)
        return lista

    def cargarVeterinario(self):
        # Cargar propietarios desde el archivo CSV
        listaPropietarioCompleta = []
        with open("csv/persona.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                if row[6] == "EMP" and row[7] == "True":
                    listaPropietarioCompleta.append(f"{row[1]} {row[2]}")
        return list(listaPropietarioCompleta)
    
    def cargarTratamiento(self):
        listaTratamiento = set()
        with open("csv/consultas.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                listaTratamiento.add(row[4])
        return listaTratamiento
    
    def cargarVacunas(self):
        listaVacunas = set()
        with open("csv/consultas.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                listaVacunas.add(row[5])
        return listaVacunas

