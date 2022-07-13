"""
Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

"""

a = int(input('Dame el número A: '))
b = int(input('Dame el número B: '))
def intermedio(a,b):
    op = a+b
    res = op//2
    return f'El punto intermedio de {op} es: {res}'

print(intermedio(a,b))