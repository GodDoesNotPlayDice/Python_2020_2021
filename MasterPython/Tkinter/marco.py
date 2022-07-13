from tkinter import *
ventana = Tk()
ventana.title('marcos')
ventana.geometry('700x400')
marcoPadre = Frame(ventana, width=350, height=450)
marcoPadre.config(
    bg='blue'
)
marcoPadre.pack(fill=X, expand=YES, anchor=N)
marco = Frame(marcoPadre, width=250, height=250)
marco.config(
    bg='red',
    bd=5, # Borde
    relief='solid', # Raised
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)
Label(marco, text='Primer marco').pack()
marco = Frame(marcoPadre, width=250, height=250)
marco.config(
    bg='green',
    bd=5, # Borde
    relief='solid', # Raised
)
marco.pack(side=RIGHT, anchor=SE)

ventana.mainloop()