name = 'Vicente Vasquez'
#función print()
# print(name)
#funcion type()
# type()
# Detectar el tipado
comprobar = isinstance(name, str)
if comprobar:
    print('Esa variable es un string')
else:
    print('No es un string')

if not isinstance(name, float):
    print('La variable no es un decimal')
else:
    print('La variable es un decimal')

#limpiar espacios
frase = '          Hola soy una frase       ' 
print(frase.strip())

#Eliminar variables
year = 2022
print(year)
del year

#Comprobar variable vacio
texto = " ff "
if len(texto) <= 0:
    print('la variable esta vacia')
else:
    print(f'la variable tiene contenido {len(texto)}')

# Encontrar caracteres

frase = "La vida es bella"
print(frase.find("vida"))

# Remplazar palabras en un string
nuevaFrase = frase.replace('vida', 'moto')
print(nuevaFrase)

#Mayusculas y minusculas
print(name)
print(name.lower())
print(name.upper())

