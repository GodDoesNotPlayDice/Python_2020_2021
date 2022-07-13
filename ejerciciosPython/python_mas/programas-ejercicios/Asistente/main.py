from modulos import *
import os, conexion
def main():
    nombre = input('Nombre: ')
    password = input('Contraseña: ')
    user = Usuario(nombre,password)
    conexion.getInfo(user.getUsuario(), user.getPassword())
if __name__ == '__main__':
    print(main())
    