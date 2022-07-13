"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

"""

x = input('letra: ')
def f(l = str()):
    v = ['a','e','i','o','u']
    if v.count(l.lower()):
        return True
    else:
        return False
print(f(x))
