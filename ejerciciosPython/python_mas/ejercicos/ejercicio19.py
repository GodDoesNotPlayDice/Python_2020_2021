"""
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

"""

def fil(a=list(),b=int()):
    i=int()
    z=list()
    arr=list()
    v=list()
    res = list()
    for x in a:
        arr.append(len(x))
    for y in arr:
        if b in arr:
            i=b
            z.append(i)
            s=arr.index(i)
            v.append(s)
        elif i == 0:
            return f'No hay palabra que contenga estos numeros {b} de caracteres'
    for k in v:
        res.append(a[k])
    return z



print(fil(['hola','s','holaaaaa','holasdasdsa'],8))


"""
terminado || Bug en el recorredor del array si la longitud parte en un numero mayor que el siguiente menor no lo tomara

"""