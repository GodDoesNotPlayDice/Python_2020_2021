"""
Ejercicio 4.
    Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima un mensaje
    segun el tipo de dato de cada variable

"""

def cheker():
    arr = []
    strr = ""
    num = 1
    boo = True
    return f'Tipo de datos: \n 1) Lista: {type(arr)} \n  2) String: {type(strr)} \n  3) Numero: {type(num)} \n 4) Booleano: {type(boo)} '

print(cheker())


def checktyper(dato,tipo):
    if isinstance(dato, list):
        print(f'El dato dado en la Lista es: {dato}')
        if tipo == 'lista':
            return f'Afirmativamente es de tipo {tipo}'
        else:
            return f'el tipo: {tipo} no es el mismo que el dato ingresado el tipo de dato correcto es una Lista!'
    elif isinstance(dato, bool):
        print(f'El dato dado es un booleano y lo que contiene es: {dato}')
        if tipo == 'bool' and isinstance(dato, bool):
            return f'Afirmativamente es de tipo {tipo}'
        else:
            return f'el tipo: {tipo} no es el mismo que el dato ingresado el tipo de dato correcto es un Booleano!'
    elif isinstance(dato, str):
        print(f'El dato dado es un string y lo que contiene es: {dato}')
        if tipo == 'string':
            return f'Afirmativamente es de tipo {tipo}'
        else:
            return f'el tipo: {tipo} no es el mismo que el dato ingresado el tipo de dato correcto es un String!'
    elif isinstance(dato, int) or isinstance(dato, float):
        print(f'El dato dado es un numero y lo que contiene es: {dato}')
        if tipo == 'entero' and isinstance(dato, int):
            return f'Afirmativamente es de tipo {tipo}'
        elif tipo == 'decimal' and isinstance(dato, float):
            return f'Afirmativamente es de tipo {tipo}'
        elif tipo != 'entero' and isinstance(dato, int):
            return f'el tipo: {tipo} no es el mismo que el dato ingresado el tipo de dato correcto es un Entero'
        elif tipo != 'decimal' and isinstance(dato, float):
            return f'el tipo: {tipo} no es el mismo que el dato ingresado el tipo de dato correcto es un Decimal'
    else:
       return 'Los datos ingresados no son validos!'

print(checktyper([1,23,5,6,7,234],'lia'))