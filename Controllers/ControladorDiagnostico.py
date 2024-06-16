import csv
from tkinter import *
from tkinter import messagebox
from Modulos.Diagnostico import Diagnostico


class ControladorDiagnostico:
    
    def __init__(self,vista, update_callback=None):
        self._vista = vista
        self._listaDiagnostico = []
        self.update_callback = update_callback

    def guardarDiagnostico(self, lista, registro):
        def IDPropietario(propietario_val):
            with open("csv/persona.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if (row[0]) == (f"{propietario_val}"):
                        return row[0]
            return None
        try:
            with open("csv/diagnostico.csv", newline="", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)
                last_id = 0
                for row in reader:
                    last_id = int(row[4])
                identificador = last_id + 1
        except FileNotFoundError:
            identificador = 1  # Si el archivo no existe, empezar con el id 1

        nombre_val = lista[0].get()
        diagnostco_val = lista[1].get()
        propietario = lista[2].get()
        propietario_val = IDPropietario(propietario)
        id_val = identificador
        
        if propietario_val is None:
            messagebox.showerror("Error", "Propietario no encontrado en el archivo CSV")
            return

        estado_val = True
        nuevo_diagnostico = Diagnostico(
            nombre_val, diagnostco_val, propietario_val,
            estado_val,id_val
        )
        with open("csv/diagnostico.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                nuevo_diagnostico.get_nombre(),
                nuevo_diagnostico.get_diagnostico(),
                nuevo_diagnostico.get_propietario(),
                nuevo_diagnostico.get_estado(),
                nuevo_diagnostico.get_id()

            ])
        registro.destroy()
        messagebox.showinfo("Éxito", "Diagnóstico registrado con éxito")
        if self.update_callback:
            self.update_callback()

    def cambiarDiagnostico(cargardiagnostico,name,cambio,valor,label_mensaje):
        diagnostico = []
        encontrado = False
        with open("csv/diagnostico.csv", encoding="UTF-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[4] == name:
                    row[int(cambio)] = valor
                    encontrado = True
                diagnostico.append(row)

        if encontrado:
            with open("csv/diagnostico.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(diagnostico)
                mensaje = f"Éxito al cambiar el valor a {valor}"
        else:
            mensaje = "Error, Documento no encontrado."
        label_mensaje.config(text=mensaje)

    def cargarDiagnostico(lista=list):
        lista = []
        with open("csv/diagnostico.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)  # Omitir la primera fila (cabecera)
            for linea in contenido:
                nombre = linea[0]
                diagnostico = linea[1]
                propietario = linea[2]
                estado = linea[3]
                id = linea[4]
                diagnosticos = Diagnostico(nombre,diagnostico,propietario,estado,id)
                lista.append(diagnosticos)
        return lista

    def cargarID(self):
        listaIDCompleta = []
        with open("csv/persona.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                if row[6] == "CLI" and row[7] == "True":
                    listaIDCompleta.append(f"{row[0]}")
        return listaIDCompleta
    
    def cargarDiagnosticos(self):
        listaDiagnosticoCompleta = set()  # Usamos un conjunto en lugar de una lista
        
        with open("csv/diagnostico.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                listaDiagnosticoCompleta.add(row[1])  # Agregamos el diagnóstico al conjunto
        
        return list(listaDiagnosticoCompleta)
    
    def cargarMascota(self):
        listaMascotaCompleta = []
        with open("csv/mascota.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido)
            for row in contenido:
                    listaMascotaCompleta.append(f"{row[0]}")
        return listaMascotaCompleta
    
    def cambiarEstadoDiagnostico(self, nombre,propietario, label_mensaje):
        diagnosticos = []
        encontrado = False
        mensaje = ""
        nombre = str(nombre)
        propietario = str(propietario)

        try:
            with open("csv/diagnostico.csv", encoding="UTF-8") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row[0].strip() == nombre.strip():
                        if row[2].strip() == propietario.strip():
                            propietario = row[2]
                            estado_actual = row[3]
                            if estado_actual == "false":
                                row[3] = "true"
                                mensaje = f"Éxito al cambiar estado de Inactivo a Activo para {nombre} del dueño con ID:{propietario}"
                            else:
                                row[3] = "false"
                                mensaje = f"Éxito al cambiar estado de Activo a Inactivo para {nombre} del dueño con ID: {propietario}"
                            encontrado = True
                    diagnosticos.append(row)

            if encontrado:
                with open("csv/diagnostico.csv", "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(diagnosticos)
                label_mensaje.config(text=mensaje, fg="green")
                if self.update_callback:
                    self.update_callback()
            else:
                label_mensaje.config(text="Error. Nombre o ID no encontrado", fg="red")

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def cantidadRazasPorDiagnostico(self):
            razasmascotas = {}
            with open("csv/mascota.csv", mode='r', encoding="UTF-8", newline="") as archivo:
                contenido = csv.reader(archivo)
                next(contenido) 
                for linea in contenido:
                    nombre = linea[0]
                    raza = linea[1]
                    razasmascotas[nombre] = raza
            conteorazas = {}
            with open("csv/diagnostico.csv", mode='r', encoding="UTF-8", newline="") as archivo:
                contenido = csv.reader(archivo)
                next(contenido)
                for linea in contenido:
                    nombremascota = linea[0]
                    if nombremascota in razasmascotas:
                        raza = razasmascotas[nombremascota]
                        if raza not in conteorazas:
                            conteorazas[raza] = 0
                        conteorazas[raza] += 1
            return conteorazas
         
    def generarRanking(self):
        mascotas_diagnosticos = {}
        with open("csv/diagnostico.csv", mode='r', encoding="UTF-8", newline="") as archivo:
            contenido = csv.reader(archivo)
            next(contenido) 
            for linea in contenido:
                mascota = linea[0]
                clave_diagnostico = mascota 
                if clave_diagnostico in mascotas_diagnosticos:
                    mascotas_diagnosticos[clave_diagnostico] += 1
                else:
                    mascotas_diagnosticos[clave_diagnostico] = 1

        ranking_ordenado = sorted(mascotas_diagnosticos.items(), key=lambda x: x[1], reverse=True)
        with open("csv/ranking.csv", mode='w', encoding="UTF-8", newline="") as archivo_ranking:
            writer = csv.writer(archivo_ranking)
            writer.writerow(['Mascota','Cantidad de Diagnósticos'])
            for mascota, cantidad in ranking_ordenado:
                writer.writerow([mascota,cantidad]) 
        
        return ranking_ordenado
        
    def mostrarDiagnostico(self):
        self._vista.mostrar_Diagnostico(self._listaDiagnostico)