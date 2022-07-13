"""
Proyecto python Y Mysql
- Abrir asistente
- Login o registro
- Si elegimos resgistro, creara un usuario en la bd
- Si elegimos login, identifica al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas.
"""
from usuarios import usuario, acciones
get = acciones.Acciones() 
while True:
    print(usuario.inicio())
    accion = input('Que quieres hacer?: ').lower()
    if accion == 'registro':
        get.registro()
    elif accion == 'login':
        get.login()
    elif accion == 'salir':
        break
    else:
        print('Opcion Invalida!')