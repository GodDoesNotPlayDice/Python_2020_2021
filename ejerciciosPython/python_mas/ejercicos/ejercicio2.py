"""
Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:
"""
import math
pi = math.pi

radio = int(input('Dame un numero de radio: '))
def area_circulo(radio):
    op = radio**2*pi
    return f'El area del circulo es: {op}'

print(area_circulo(radio))