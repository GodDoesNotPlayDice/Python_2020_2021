from tkinter import *

ventana = Tk()
ventana.geometry('700x400')
ventana.title('Formulario')

# Texto encabezado

encabezado = Label(ventana, text='Formulario con tkinter')
encabezado.config(
    fg='white',
    bg='darkgray',
    font=('Open Sans', 18),
    padx=10,
    pady=10
)

encabezado.grid(row=0,column=0,columnspan=2,sticky=W,)

#Label para el campo
label = Label(ventana, text='Nombre')
label.grid(row=1,column=0,padx=5,pady=5)
label = Label(ventana, text='Apellido')
label.grid(row=2,column=0,padx=5,pady=5)

# Campo texto 
nombre = Entry(ventana)
apellido = Entry(ventana) #Con .config(justify=left,right / state=disabled,normal) justify por donde sale el texto y state para habilitar y desabilitar el texto.
nombre.grid(row=1,column=1,padx=5,pady=5,sticky=W)
apellido.grid(row=2,column=1,padx=5,pady=5,sticky=W)

#Label descripcion
label = Label(ventana, text='Description')
label.grid(row=3,column=0,padx=5,pady=5)

#campo grande (description)
bigText = Text(ventana)
bigText.grid(row=3,column=0,padx=5,pady=5)
ventana.mainloop()
