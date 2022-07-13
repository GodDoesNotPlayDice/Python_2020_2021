"""
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
"""

a = int(input('Dame el número A: '))
b = int(input('Dame el número B: '))
def n_max(a,b):

    if a > b:
        return f'El Numero maximo es {a} y el minimo {b}'
    elif a < b:
        return f'El Número maximo es {b} y el minimo {a}'
    else:
        return f'Los dos números son iguales'

print(n_max(a,b))
