"""
Ejercicio 9. Hacer un programa que pida numeros al Usuario indefinidamento hasta meter el 111
"""
n1 = 1
while n1 < 111:
    n1 = int(input('Dame un numero: '))
    if n1 == 111:
        break
    else:
        print(f'Hola llevas {n1} y debes completar hasta el numero 111')
        