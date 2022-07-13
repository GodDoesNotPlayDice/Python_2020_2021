"""
    Ejercio 5.
        Hacer un programa que mueste todos los numeros entre dos numeros que diga el usuario.

"""

n1 = int(input('Dame un numero: '))
n2 = int(input('Dame el segundo numero: '))
if n1 > n2:
    for cont in range(n2,n1 + 1):
        print(cont)
elif n1 < n2:
    for cont in range(n1,n2 + 1):
        print(cont)
elif n1 == n2 or n2 == n1:
    print(f'tu rango de numeros son iguales {n1}')
    
