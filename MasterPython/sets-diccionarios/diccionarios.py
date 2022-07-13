"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

personas = {
    "nombre": "Vicente",
    "apellidos": "Vasquez",
    "web": "vicentevasquez.com"
}
print(personas["web"])

#Lista con diccionarios

contactos = [
    {
        "nombre": "Antonio",
        "email": "antonio@antonio.com"
    },
    {
        "nombre": "Luis",
        "email": "luis@luis.com"
    },
    {
        "nombre": "Salvador",
        "email": "salvador@salvador.com"
    }
]
contactos[0]['nombre'] = 'Antoñito'
print(contactos[0]['nombre'])


print('\n Listado de contactos: ')

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']} \nEmail del contacto: {contacto['email']} \n --------------- \n")