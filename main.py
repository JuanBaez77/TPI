from Raza import Razas
from Persona import Persona


def menu():
    print("          MENU\n")
    n = int(input("Personas // presione(1)\nMascotas // presione(2)\nTratamientos // presione(3)\n--> "))

    if n == 1:
        # Submenú para Personas
        m = int(input(
            "Lista de Clientes // presione(1)\n"
            "Personas Activas // presione(2)\n"
            "Empleados // presione(3)\n--> "
        ))
        
        if m == 1:
            print("Mostrando lista de clientes...")
        elif m == 2:
            print("Mostrando personas activas...")
            Persona.mostrarPersona()
        elif m == 3:
            print("Mostrando empleados...")

    elif n == 2:
        m = int(input(
            "Mascotas Activas // presione(1)\n"
            "Nueva Mascota // presione(2)\n"
            "Razas de Mascotas // presione(3)\n"
            "Historial de Vacunas // presione(4)\n--> "
        ))
        
        if m == 1:
            print("Mostrando mascotas activas...")
        elif m == 2:
            print("Agregar nueva mascota...")
        elif m == 3:
            j = int(input("Agregar raza // presione(1)\nEliminar raza // presione(2)\n--> "))
            if j == 1:
                raza = Razas(input("Que raza desea agregar --> "))
                raza.add_raza()
            elif j == 2:
                eliminar_raza = Razas(input("Que raza desea eliminar --> "))
                eliminar_raza.delete_raza()
        elif m == 4:
            print("Mostrando historial de vacunas...")

    elif n == 3:
        m = int(input(
            "Tratamientos Disponibles // presione(1)\n"
            "Agenda de Tratamientos // presione(2)\n--> "
        ))

        if m == 1:
            print("Mostrando tratamientos disponibles...")
        elif m == 2:
            print("Mostrando agenda de tratamientos...")

if __name__ == "__main__":
    menu()