# IMPORT DE CLASES
from raza import Razas
from Persona import Persona


def menu():
    while True:
        print("          MENU\n")
        n = int(input("Personas // presione(1)\nMascotas // presione(2)\nTratamientos // presione(3)\nSalir del menu // presione(4)\n--> "))

        if n == 1:
            m = int(input(
                "Registrar persona // presione(1)\n"
                "Lista de Clientes // presione(2)\n"
                "Personas Activas // presione(3)\n"
                "Empleados // presione(4)\n"
            ))
            if m == 1:
                Persona.registrarPersona()
            elif m == 2:
                print("Mostrando lista de clientes...")
            elif m == 3:
                print("Mostrando personas activas...")
                Persona.mostrarPersona()
            elif m == 4:
                print("Mostrando empleados...")
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")

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
                j = int(input("Mostrar Razas // presione(1)\nAgregar raza // presione(2)\nEliminar raza // presione(3)\n--> "))
                if j == 1:
                    raza = Razas.mostrarRaza()
            elif j == 2:
                    raza = Razas(input("Que raza desea agregar --> "))
                    raza.añadirRaza()
            elif j == 3:
                    eliminar_raza = Razas(input("Que raza desea eliminar --> "))
                    eliminar_raza.eliminarRaza()
            elif m == 4:
                print("Mostrando historial de vacunas...")
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")

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
            j = int(input("Mostrar Razas // presione(1)\nAgregar raza // presione(2)\nEliminar raza // presione(3)\n--> "))
            if j == 1:
                raza = Razas.mostrarRaza()
            elif j == 2:
                raza = Razas(input("Que raza desea agregar --> "))
                raza.añadirRaza()
            elif j == 3:
                eliminar_raza = Razas(input("Que raza desea eliminar --> "))
                eliminar_raza.eliminarRaza()
        elif m == 4:
            print("Mostrando historial de vacunas...")

            if m == 1:
                print("Mostrando tratamientos disponibles...")
            elif m == 2:
                print("Mostrando agenda de tratamientos...")
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        elif n == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    menu()
