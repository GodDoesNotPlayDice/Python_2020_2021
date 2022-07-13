#Bucle For
"""
For Variable in elemento_iterable (lista,rango,etc)
    Bloque de instrucciones

"""

rango = range(1,11)
result = 0
for arrNumbers in rango:
    print(f'Voy por {arrNumbers}')
    result += arrNumbers

print(result)

# Ejemplo tablas de multiplicar

userN = int(input('¿De que número quieres la tabla?: '))
if userN < 1:
    userN = 1

print(f'Tabla de multiplicar del número {userN}')

for tableN in range(1,11):
    result = userN * tableN
    print(f'{userN} X {tableN} = {result}')


# cortar bucle con break