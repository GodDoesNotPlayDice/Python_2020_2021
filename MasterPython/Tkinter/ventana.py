# Tkinter
# Modulo para crear interfaces

from tkinter import *
import os
class Programa:
    def __init__(self):
        self.title = 'Master en python'
        self.icon = './img/logo.ico'
        self.icon_alt = 'k:/DesarrolloWeb/MasterPython/Tkinter/img/logo.ico'
        self.size = '770x470'
        self.resizable = False


    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #Bloquear tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)
        # Titulo de la ventana
        ventana.title(self.title)
        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)


    def addTexto(self, dato):
        # Mostrar texto en el programa
        texto = Label(self.ventana, text = dato)
        texto.pack()
    
    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()
        
#Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto('hola XD')
programa.mostrar()


