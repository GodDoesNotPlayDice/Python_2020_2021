from io import open
import os, pathlib, functions 
ruteFile = str(os.path.abspath('ejerciciosPython/python')) + '/programas-ejercicios/Menú-de-la-aplicación-Kwranking/keywords.txt'
def cargarKeyword():
    if not os.path.isfile(ruteFile):
        print('Archivo creado y editado correctamente!')
        rute = open(ruteFile, 'x+')
        rute.write('macarrones\nmacarrones con tomate y queso\nreceta de macarrones')
    else:
        print('Archivo editado correctamente!')
        rute = open(ruteFile, 'a+')
        rute.write('macarrones\nmacarrones con tomate y queso\nreceta de macarrones')
def readKeyword():
    letras = list()
    if not os.path.isfile(ruteFile):
        print('No se puede encontrar la ruta del archivo!!')
    else:
        readFile = open(ruteFile, 'r')
        arr = readFile.readlines()
        if len(arr) == 0:
            print('lista vacia!')
        else:
            for i in arr:
                i = i.replace('\n', '')
                letras.append(i)
            print(letras)
