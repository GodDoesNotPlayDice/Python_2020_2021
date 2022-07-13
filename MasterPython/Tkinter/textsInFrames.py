from tkinter import *

ventana = Tk()
ventana.geometry('700x500')
blockFather = Frame(ventana, width='700', height='500')
blockFather.pack(expand=YES, fill=BOTH)
block = Frame(blockFather, width='100', height='100')
block.config(
    bg='red',
    bd=2,
    relief='solid'
)
block.pack(side=LEFT, anchor=NW)
block = Frame(blockFather, width='100', height='100')
block.config(
    bg='blue',
    bd=2,
    relief='solid'
)
block.pack(side=RIGHT, anchor=NE)
block = Frame(blockFather, width='100', height='100')
block.config(
    bg='yellow',
    bd=2,
    relief='solid'
)
block.pack(side=LEFT, anchor=SW)
block = Frame(blockFather, width='100', height='100')
block.config(
    bg='green',
    bd=2,
    relief='solid'
)
block.pack(side=RIGHT, anchor=SE)
ventana.mainloop()