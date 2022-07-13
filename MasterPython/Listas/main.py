"""
Listas(Arrays)
Son colecciones do conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numerico

"""
# Definir Lista
peliculas = ['Batman', 'Spiderman', 'El señor de los anillos']
cantantes = list(('2pac','Drake','Jennifer Lopez')) # Transformar a lista
years = list(range(2020, 2050))
# print(years)
variada = ['Vicente',30,3.3,True,'text']
"""
#Indices
print(peliculas[1])
print(peliculas[-2]) #Acepta valores negativos
print(cantantes[0:2]) #Rango de elementos
print(peliculas[0:]) #cuando se coloca solo un numero antes de los 2 puntos se toman todos los elementos a apartir de del numero colocado

# Remplazar items de una lista
peliculas[0] = "Gran torino"
peliculas[1] = "El Hobbit"
print(peliculas)
cantantes.append('Kase O')
print(cantantes)

# Recorrer una lista
nueva_pelicula = "" 
while nueva_pelicula != "parar":
    nueva_pelicula = input('intrduce la nueva pelicula: ')
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    # print(f'{peliculas.index(pelicula)+1}. {pelicula}')
"""


#listas Multidimensionales

contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

# print(contactos[1][1])
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f'Nombre: {elemento}')
        else:
            print(f'Email: {elemento}')
    print('\n')