"""
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

"""
arr = []
def separar(arr):
    par = []
    impar = []
    n = 0
    while len(arr) <= 9:
        n = int(input('introduce los 10 números que estaran en las lista: '))
        arr.append(n)
    arr.sort()
    for i in arr:
        op = i%2
        if op == 0:
            par.append(i)
        else:
            impar.append(i)
    return f'Lista de numeros Pares: {par}\n Lista de numeros Impares: {impar}'

print(separar(arr))
