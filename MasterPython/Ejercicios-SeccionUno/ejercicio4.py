"""
Ejercicio 4.
    pedir 2 numeros al user y hacer todas las operaciónes basicas de una calculadora

"""

print('Bienvendio a la calculadora, selecciona tus 2 numeros y una operacion \n operaciones: \'+\'(suma),  \'-\'(resta),  \'x\'(multiplicación),  \'/\'(división)')

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
op = str(input('Operacion!: '))

if op == '+':
    result = n1 + n2
    print(f'Tu suma es de: {result}')
elif op == '-':
    result = n1 - n2
    print(f'Tu resta es de: {result}')
elif op == 'x':
    result = n1 * n2
    print(f'Tu multiplicación es de: {result}')
elif op == '/':
    result = n1 / n2
    print(f'Tu división es de: {result}')