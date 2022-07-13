from tkinter import *

ventana = Tk()
ventana.geometry('500x500')
texto = Label(ventana, text='Box 1')
texto.config(
    fg='white',
    bg='black',
    padx=20,
    pady=20,
    font=('sans-serif',20)
)
texto.pack(side=TOP, fill=X, expand=YES)
texto = Label(ventana, text='Box 2')
texto.config(
    bg='orange',
    padx=10,
    pady=10,
    font=('sans-serif',20)
)
texto.pack(fill=X, expand=YES)
texto = Label(ventana, text='Box 3')
texto.config(
    bg='red',
    padx=20,
    pady=20,
    font=('sans-serif',20)
)
texto.pack(side=LEFT)
texto = Label(ventana, text='Box 4')
texto.config(
    bg='green',
    padx=20,
    pady=20,
    font=('sans-serif',20)
)
texto.pack(side=LEFT)
texto = Label(ventana, text='Box 5')
texto.config(
    bg='pink',
    padx=20,
    pady=20,
    font=('sans-serif',20)
)
texto.pack(side=LEFT)
ventana.mainloop()
