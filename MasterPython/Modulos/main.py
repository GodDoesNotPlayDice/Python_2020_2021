"""
Modulo: Un modulo son funcionalidades ya hechas para reutilizar
https://docs.python.org/es/3/py-modindex.html modulos nativos

Podemos conseguir modulos en internet
https://pypi.org

Crear modulos que a lo que se enfoca esto!
"""
"""
Formas de llamar a un modulo

import modulo
print(modulo.holaMundo('Vicente'))
"""

from modulo import holaMundo
print(holaMundo('Vicente'))


#Modulo de fechas

import datetime

print(datetime.date.today())
fecha__completa = datetime.datetime.now()
print(fecha__completa)
print(fecha__completa.year)
print(fecha__completa.day)
print(fecha__completa.month)

#Formatear fecha

fecha_personalizada = fecha__completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)
# Sacar el tiempo en unix
print(datetime.datetime.now().timestamp())
