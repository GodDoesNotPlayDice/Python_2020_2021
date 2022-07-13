"""
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

"""
t = 'Mi Diario Python'


def inv(a):
    arr = list(a)
    arr.reverse()
    t = str().join(arr)
    return t


print(inv(t))


"""
Ida hacer que la palabra ingrese por mediante un array de tal forma de usar reverse(), para dar vuelta la palabra luego en un for in tomar cada una de esas letras e ir colocandolas en un string

"""

"""
Orther solution

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1

"""