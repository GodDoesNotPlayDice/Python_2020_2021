'''
Cambiar las vocales por mayusculas en una funcion

'''

def palabras(palabras): 
    vocales = ['a','e','i','o','u'] #Lista con vocales
    arr = [] #Lista donde pasaran las vocales cambiadas
    for i in palabras: # bucle para recorrer cada letra
        if vocales.count(i): # condicional para comparar cada letra
            arr.append(i.upper()) # metodo para agregar a la lista nueva en mayusculas
        else:
            arr.append(i.lower()) # agrega el resto de palabras no vocales en minuscula
    return ''.join(arr) # retorna la lista en forma de string


print(palabras('Hola como estas'))
