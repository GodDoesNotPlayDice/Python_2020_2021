import os
import shutil
#crear carpeta
ruta = os.path.isdir('./MasterPython/Sistema-de-Archivos/mi_carpeta')
if not ruta:
    os.mkdir('./MasterPython/Sistema-de-Archivos/mi_carpeta')
    print('Carpeta creada')
else:
    print('Ya existe')

# Borrar
#os.rmdir('./MasterPython/Sistema-de-Archivos/mi_carpeta')
"""
#Copiar
current_ruta = './MasterPython/Sistema-de-Archivos/mi_carpeta'
ruta_nueva = './MasterPython/Sistema-de-Archivos/mi_carpeta-copiada'
shutil.copytree(current_ruta, ruta_nueva)

"""

# listar contenido

c = os.listdir('./') + '\n'
print(c)