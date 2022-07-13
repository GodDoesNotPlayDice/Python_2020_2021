'''
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

'''
arr = list()
# e = str(input('cadena: '))
e = str(input('Cadena: '))
for i in e:
    if i.isupper() == True:
        arr.append(i)
res = ''.join(arr)
print(f'Hola tu plabra es {e} y contiene {len(res)} Mayusculas')