# IMPORTAR MENU
from Vista.VistaMenu import Vista

def nombreVeter():
        with open("TPI/assets/nombre.txt") as file:
                reader = file.read()
        return reader

def menu():
        raiz = Vista(nombreVeter())
        raiz.iconbitmap("TPI/assets/logo_nuevo.ico")
        raiz.mainloop()

if __name__ == "__main__":
        menu()