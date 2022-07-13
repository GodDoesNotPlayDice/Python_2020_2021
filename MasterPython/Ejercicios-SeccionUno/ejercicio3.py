"""
Ejercicio 3, Escribir un programa que mueste los cuadrados
(Numero multiplicado por si mismo) de los primeros 60 numeros naturales
con For y Con while
"""

# While
"""
count = 0
while count <= 60:
    count+=1
    cuadrado=count*count
    print(f'El cuadrado de {count} es {cuadrado}')
"""
# for

for cont in range(61):
    square = cont * cont 
    print(f'el cuadrado de {cont} es {square}')