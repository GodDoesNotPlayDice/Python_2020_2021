from tkinter import *
ventana = Tk()
ventana.geometry('500x500')
# ventana.config(bg='black')
textos = Label(ventana, text='Bienvenido a mi programa')
textos.config(
    fg='white',
    bg='black',
    padx=20,
    pady=20,
    font=('sans-serif', 30)

)
textos.pack()
textos = Label(ventana, text='Como estas?')
# parametros de palabras claves da igual el orden de los parametros
textos.config(
    width=400,
    height=200,
    bg='orange',
    justify=RIGHT,
    cursor='arrow'
)
textos.pack(anchor='sw')
ventana.mainloop()