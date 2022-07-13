"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
    - Recorrer la lista y mostrarla
    - Ordenarla y mostrarla
    - Mostrar su longitud
    - Buscar algun elemento (que el usuario pida por teclado)
"""

def showAndOrderList(numeros):
    list(numeros)
    numeros.sort()
    print('Numeros en la lista: ')
    for numero in numeros:
        print (f'Elementos: {numero}')
    print (f'Total de numeros que hay en la lista: {len(numeros)}')
    try:
        snumber = int(input('Dime que elemento quieres buscar: '))
        cheker = isinstance(snumber, int)
    except:
        return 'Introduce el numero bien!'
    while not cheker or snumber <= 0:
        snumber = int(input('Dime que elemento quieres buscar: '))
    else:
        print(f'Has introducido el numero {snumber}')
    try:
        search = numeros.index(snumber)
        return f'El numero buscado existe en la lista es el indice {search}'
    except:
        return 'El numero no se encuentra en la lista'


print(showAndOrderList([20,49,123,4423,234]))

