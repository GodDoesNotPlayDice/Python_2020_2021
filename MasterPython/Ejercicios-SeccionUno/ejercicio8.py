"""
    Ejercicio8. ¿Cuanto es el X porcentaje de X numero?
"""

n1 = int(input('Dame el numero: '))
porcentaje = int(input(f'Dime el porcentaje que quieres sacar de {n1} sin el %: '))

op = n1*porcentaje/100
print(f'Tu porcentaje de {n1} es {op}%')