'''

Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

'''
shoppingCar = str(input('Elementos de la cesta: ')).split()
arrObj = []
for i in shoppingCar:
    word = i.capitalize()
    arrObj.append(word)
    print(word)
print(', '.join(arrObj))