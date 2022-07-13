cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Inglesias']
numeros = [1,2,5,8,3,4]

#Ordenar
# print(numeros)
numeros.sort()
# print(numeros)

#Añadir elementos
cantantes.append('Natos y Waor')
cantantes.insert(1,'David Bisbal')
cantantes.pop(1)
cantantes.remove('Bad Bunny')
# print(cantantes)

#Dar la vuelta
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print('Drake' in cantantes) #devuelve un booleano
print(len(cantantes))

#Cuantas veces aparece un elemento

print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))

#Conseguir indice
print(cantantes.index("Drake"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)