"""
Estructura en la cual se cumple una condicion hasta que llege al limite ejecuta hasta que el contador
llege a 0
"""

count = 1
muestrame = 0
while count <= 100:
    muestrame = (f'{muestrame}, {count}')
    count+=1
    print(f'Estoy en el numbero: {count - 1}')

print(muestrame)

# Tabla de multiplicar
result = 0
count = 0
userN = int(input('Introduce un numero: '))
while count <=9:
    count+=1
    result = userN * count
    print(f'\n Tu tabla es: {userN} X {count} = {result}')


