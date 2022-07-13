from io import open
import pathlib

# Abrir archivos
ruta = str(pathlib.Path().absolute()) + "/MasterPython/Sistema-de-Archivos/texto.txt"
print(ruta)
archivo = open(ruta, "a+")

# Escribir
# archivo.write('Soy un texto metido desde python \n')

# Cerrar
# archivo.close()


# Abrir archivos PERMISO DE LECTURA
# ruta = str(pathlib.Path().absolute()) + "/archivo-informatica.txt"
# print(ruta)
# archivo_lectura = open(ruta, "r")

# Leer
# contenido = archivo_lectura.read()
# print(contenido)

# Leer Contenido y guardar en la lista
# lista = archivo_lectura.readlines()
# archivo_lectura.close()

# print(lista)
# for i in lista:
#     if not i.isnumeric():
#         print(f'- {i}')
#     else:
#         print(False)