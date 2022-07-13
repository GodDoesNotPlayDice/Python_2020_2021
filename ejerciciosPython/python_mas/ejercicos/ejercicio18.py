"""
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

"""

textos = ['hola', 'yo estoy', 'locuraaaaaaa', 'hola','dddddddddddddddddddddddddddddddddddd']


def mas_larga(a=list()):
    z=int()
    arr=list()
    for x in a:
        arr.append(len(x))
    for y in arr:
        if y > z:
            z=y
            s=arr.index(z)
            res = a[s]
    return res
    
print(mas_larga(textos))


"""
Devolver la palabra equivalente a Z
"""