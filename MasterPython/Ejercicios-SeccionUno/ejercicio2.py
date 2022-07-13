"""
    Ejercicio 2:
        Escribir un Script que nos muestre por pantalla todos los numeros pares del 1 al 120
"""
count = 1
for count in range(1,120 + 1):
    if count%2 == 0:
        print(count)