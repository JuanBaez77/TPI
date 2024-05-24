import csv
from tkinter import *
from tkinter import messagebox

class Raza:
    def __init__(self, raza="", estado=1):
        self.__raza = raza.lower()
        self.__estado = estado
        
    # Getters
    def get_raza(self):
        return self.__raza
    
    def get_estado(self):
        return self.__estado
    
    # Setters
    def set_raza(self, raza):
        self.__raza = raza 
        
    def set_estado(self, estado):
        self.__estado = estado   
        
    def _str_(self):
        return self.__raza

def mostrarRaza():
    """
    Mostrar por pantalla las razas almacenadas en el csv
    """
    try:
        with open("csv/razas.csv", "r", encoding="UTF-8", newline="") as lectura:
            razasAlmacenadas = csv.reader(lectura)
            top = Toplevel()
            top.title("Razas Almacenadas")
            top.geometry("400x300")

            scrollbar = Scrollbar(top)
            scrollbar.pack(side=RIGHT, fill=Y)

            text = Text(top, wrap=NONE, yscrollcommand=scrollbar.set)
            text.pack(expand=True, fill=BOTH)

            text.insert(END, "🐶 Razas Almacenadas 🐶\n\n")
            for linea in razasAlmacenadas:
                text.insert(END, f"{linea[0]}, {linea[1]}\n")
            
            text.configure(state='disabled')
            scrollbar.config(command=text.yview)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo razas.csv no se encontró.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

def crearRaza():
    """
    Permitir al usuario añadir una raza al csv
    """
    def guardarRaza():
        nombre_raza = raza_entry.get().lower()
        if nombre_raza:
            raza = Raza(nombre_raza)
            try:
                with open("csv/razas.csv", mode='a', newline='') as archivo:
                    razaNueva = csv.writer(archivo)
                    razaNueva.writerow([raza.get_raza(), "1"])
                messagebox.showinfo("Éxito", f"Raza '{raza.get_raza()}' guardada en razas.csv")
                raza_entry.delete(0, END)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar la raza: {e}")
        else:
            messagebox.showerror("Error", "Por favor ingrese un nombre de raza.")

    top = Toplevel()
    top.title("Agregar Raza")
    top.geometry("300x150")

    Label(top, text="Ingrese el nombre de la raza:").pack(pady=10)
    raza_entry = Entry(top)
    raza_entry.pack(pady=5)
    Button(top, text="Guardar", command=guardarRaza).pack(pady=20)

def modificarEstadoRaza():
    """
    Permitir al usuario modificar el estado de una raza en el csv
    """
    def cambiarEstado():
        nombre_raza = raza_entry.get().lower()
        nuevoEstado = estado_entry.get()
        if nuevoEstado not in ["0", "1"]:
            messagebox.showerror("Error", "Estado inválido. Ingrese (0) Deshabilitado o (1) Habilitado.")
            return

        encontrado = False
        filas = []

        try:
            with open("csv/razas.csv", "r", encoding="UTF-8", newline="") as lectura:
                razasAlmacenadas = csv.reader(lectura)
                for linea in razasAlmacenadas:
                    if linea[0] == nombre_raza:
                        linea[1] = nuevoEstado
                        encontrado = True
                    filas.append(linea)

            if encontrado:
                with open("csv/razas.csv", "w", encoding="UTF-8", newline="") as escritura:
                    escritor = csv.writer(escritura)
                    escritor.writerows(filas)
                messagebox.showinfo("Éxito", f"Estado de la raza '{nombre_raza}' actualizado a {nuevoEstado}")
                raza_entry.delete(0, END)
                estado_entry.delete(0, END)
            else:
                messagebox.showerror("Error", f"La raza '{nombre_raza}' no se encontró en el archivo.")
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo razas.csv no se encontró.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar la raza: {e}")

    top = Toplevel()
    top.title("Modificar Estado de Raza")
    top.geometry("300x200")

    Label(top, text="Ingrese el nombre de la raza:").pack(pady=10)
    raza_entry = Entry(top)
    raza_entry.pack(pady=5)
    Label(top, text="Ingrese el nuevo estado (0 o 1):").pack(pady=10)
    estado_entry = Entry(top)
    estado_entry.pack(pady=5)
    Button(top, text="Guardar", command=cambiarEstado).pack(pady=20)

def menuRaza():
    ventana = Tk()
    ventana.title("Menu Razas")
    ventana.iconbitmap("img/404022.ico")
    ventana.geometry("300x250")

    Button(ventana, text="Mostrar Razas", command=mostrarRaza).pack(pady=10)
    Button(ventana, text="Agregar Raza", command=crearRaza).pack(pady=10)
    Button(ventana, text="Modificar Estado de Raza", command=modificarEstadoRaza).pack(pady=10)

    ventana.mainloop()