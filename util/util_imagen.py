from PIL import Image, ImageTk

class Util_Imagen:
    

    def leer_imagen(img, size):
        return ImageTk.PhotoImage(Image.open(img).resize(size, Image.ADAPTIVE))