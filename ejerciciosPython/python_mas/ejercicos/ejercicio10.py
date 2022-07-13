"""
Definir una función que calcule la longitud de una lista o una cadena dada.

"""
a = ['a','b','c']
e = 'si'
def lenght(b):
    c=0
    if isinstance(b, list):
        for x in b:
            x.count(str())
            c+=1
        return c
    else:
        return b.count(str())-1
        
"""
Orther solution

def largo_cadena (lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

print(largo_cadena(e))

"""