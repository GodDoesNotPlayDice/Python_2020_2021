"""
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

texto = 'HOLAsSs'
def searchMayus(a=str()):
    arr=list()
    b=list()
    for x in a:
        arr.append(x)
        for z in arr:
            pass
        if arr.count(z.upper()):
            if arr.count(z.lower()):
                pass
            else:
                b.append(z)
    return f'Este texto tiene {len(b)} palabras en mayusculas'

print(searchMayus(texto))