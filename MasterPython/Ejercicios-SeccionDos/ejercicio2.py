"""
Ejercicio 2. Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar la lista
"""
def programWhile():
    arr = []
    cont = 0
    while not len(arr) > 120-1:
        cont+=1
        arr.append(cont)
    else:
        print(f'Ya no puedes agregar mas items')
        return f'Items: {arr}'

print(programWhile())

def programFor():
    collect = []
    for cont in range(0, 120):
        collect.append(f'elemento: {cont}')
        print(f'La lista de numeros son {collect}')
    return f'Mostrando el: {collect[cont]}'

print(programFor())