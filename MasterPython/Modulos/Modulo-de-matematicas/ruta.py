import os
ruta = os.path.dirname(__file__)
fileName = os.path.basename(__file__)
print(ruta)
print(fileName)

# Ruta relativa
# absoluta
ruta2 = os.path.abspath(__file__)
print(ruta2)