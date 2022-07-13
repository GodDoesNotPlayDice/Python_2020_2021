import random
# Funciones nativas
cadena = 'hola soy una cadena de texto'
numero = 10
lista = ['hola','soy','una','lista']
listaNumeros = []
a = 0
while a < 20:
    numero = str(random.randint(1,20))
    listaNumeros.append(numero)
    a+=1
cadena = ''.join(listaNumeros)
# print(cadena)

# Len() devuelve la cantidad de elementos de una lista,tupla o cadena:
# print(len(cadena))

# Max() devuelve el mayor elemento.
# print(max(listaNumeros))

# Min() devuelve el menor elemento.
# print(max(listaNumeros))

# Metodo !!!, Index() devuelve el índice de la primera ocurrencia de ‘x’ en la secuencia.
# print(listaNumeros.index(2))

# Eval() Evalúa una cadena como una expresión:
# num = '10 + 20'
# res = (eval(num))
# print(type(res))

# La función pow() si recibe dos (02) argumentos, eleva el primero argumento a la potencia del segundo argumento.
# print(pow(2,10))

# La función round() redondea un número flotante a una precisión dada en dígitos decimal (por defecto 0 dígitos). Esto siempre devuelve un número flotante. La precisión tal vez sea negativa.
# print(round(10.6))

# La función sum() devuelve una lista ordenada de los elementos de la secuencia que recibe como argumento (lista o cadena). La secuencia original no es modificada.
lista = [1,1]
print(sum(lista))