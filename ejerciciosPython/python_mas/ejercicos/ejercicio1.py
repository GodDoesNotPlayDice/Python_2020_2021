"""
Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura:

"""
print('Area del rectángulo')
base = int(input('Dame un valor de la base: '))
altura = int(input('Dame un valor de la altura: '))
def area_rectangulo(base, altura):
        op = base*altura
        return f'el area del rectangulo es: {op}'

print(area_rectangulo(base,altura))