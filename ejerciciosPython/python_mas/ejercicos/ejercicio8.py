"""
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""
a = int(input('Dame el número A: '))
b = int(input('Dame el número B: '))
c = int(input('Dame el número C: '))
def max_de_tres(a,b,c):
    if a > b and a > c:
        return f'El número {a} es el mayor'
    elif b > a and b > c:
        return f'El número {b} es el mayor'
    elif c > a and c > b:
        return f'El número {c} es el mayor'
    else:
        return 'El conjunto de los tres números son iguales'

print(max_de_tres(a,b,c))