"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla
ACCIÓN    AVENTURA          DEPORTES
GTA       ASSASIN            FIFA21
COD       CRASH               PRO21
PUGB      Prince of persia   MOTO GP21

Mostrar ordenada
"""

def videogames():
    VideoJuegos = [
        {
            'Categoria': 'ACCIÓN',
            'Juegos': ['GTA','COD','PUGB']
        },
        {
            'Categoria': 'Aventura',
            'Juegos': ['ASSASIN','CRASH','Prince of persia']
        },
        {
            'Categoria': 'Deportes',
            'Juegos': ['FIFA21','PRO21','MOTOGP21']
        }
    ]
    for categoria in VideoJuegos:
        print(f'----------{categoria["Categoria"]}-----------')
        for juegos in categoria["Juegos"]:
            print(juegos)


videogames()