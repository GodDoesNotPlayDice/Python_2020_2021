from tkinter import *
from PIL import Image, ImageTk
ventana = Tk()
ventana.geometry('700x500')
Label(ventana, text='hola, soy vicente').pack(anchor='ne')
imagen = Image.open('k:/DesarrolloWeb/MasterPython/Tkinter/img/minita.png')
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack()
ventana.mainloop()