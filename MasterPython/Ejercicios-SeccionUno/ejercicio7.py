"""
Ejercicio 7. Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

"""

n1 = int(input('Dame un numero: '))
n2 = int(input('Dame el siguiente numero: '))

if n1 < n2:
    for arr in range(n1,n2+1):
        if arr%2 == 0:
            print(f'{arr} Es PAR')
        else:
            print(f'{arr} Es Impar')
else:
        print('El numero 1 debe ser mayor al 2')
        