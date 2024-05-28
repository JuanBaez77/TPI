# IMPORTAR MENU
from modulos.menu import MenuDesign
def nombreVeter():
        with open("assets/nombre.txt") as file:
                reader = file.read()
        return reader

def menu():
        raiz = MenuDesign(nombreVeter())
        raiz.mainloop()

if __name__ == "__main__":
        menu()