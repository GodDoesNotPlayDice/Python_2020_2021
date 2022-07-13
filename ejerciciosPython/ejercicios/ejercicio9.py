'''
Crear un módulo para validación de contraseñas. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

La contraseña debe contener un mínimo de 8 caracteres.
Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
La contraseña no puede contener espacios en blanco.
Contraseña válida, retorna True.
Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".

'''
import string
password = 'Hola#123'.strip()
alphaNumeric = string.ascii_letters + string.digits + '!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~'
if len(password) < 8:
    print('u password is very short, pls write a password more long!')
else:
    alphList = list()
    passSplit = list()
    checkers = list()
    for i in alphaNumeric:
        alphList.append(i)