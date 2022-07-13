"""
Ejercicio3.
    Programa que compruebe si una variable está vacia y si está vacia, rellenarla con texto en minusculas y mostrarlo en mayusculas
"""


def varcheker(text = ''):
    if not len(text.strip()) <= 0:
        return '\nEsta variable contiene texto!'
    else:
        print('\nVariable Vacia se ha auto rellando con texto! \n')
        text = "variable rellenada con texto!"
        return text.upper()
    
print(varcheker(''))