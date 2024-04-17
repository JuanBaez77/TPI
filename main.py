from raza import Razas

def menu():
    print("          MENU\n")
    n = int(input("Listado de mascotas activas // presione(1)\nListado de tratamientos // presione(2)\nListado de diagnosticos // presione(3)\nListado de Vacunas // presione(4)\nListado de razas // presione(5)\nListado de veterinarios // presione(6)\nListado de clientes // presione(6)\n-->"))

    if n == 5:
        j = int(input("Agregar raza // presione(1)\nEliminar raza // presione(2)\n-->"))
        if j == 1:
            raza = Razas(input("Que raza desea agregar -> "))
            raza.add_raza()
        if j == 2:
            pass

if __name__ == "__main__":
    menu()