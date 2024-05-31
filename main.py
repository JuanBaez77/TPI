# IMPORTAR MENU
from Vista.VistaMenu import Vista

def nombreVeter():
        with open("assets/nombre.txt") as file:
                reader = file.read()
        return reader

def menu():
        raiz = Vista(nombreVeter())
        raiz.mainloop()

if __name__ == "__main__":
        menu()