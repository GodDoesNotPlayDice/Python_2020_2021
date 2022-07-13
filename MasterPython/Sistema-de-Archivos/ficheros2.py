from io import open
import pathlib
import shutil
import os
# Copiar
# ruta = str(pathlib.Path().absolute()) + "/archivo-informatica.txt"
# ruta_nueva = str(pathlib.Path().absolute()) + "/archivo-informatica-copia.txt"
# shutil.copyfile(ruta, ruta_nueva)

# Mover
"""
ruta = str(pathlib.Path().absolute()) + "/MasterPython/Sistema-de-Archivos/texto.txt"
shutil.move(ruta, ruta_nueva)
"""
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/MasterPython/Sistema-de-Archivos/texto-movido.txt"

# Eliminar

os.remove(ruta_nueva)
"""
"""
# Comprobar si existe
rutaAbs = os.path.abspath("./")
# print(rutaAbs)
rutaComprabar = os.path.abspath("MasterPython/Sistema-de-Archivos/") + "/texto.txt"
print(rutaComprabar)f os.path.isfile(rutaComprabar):
    print('Si existe')
else:
    print('No existe')
"""

