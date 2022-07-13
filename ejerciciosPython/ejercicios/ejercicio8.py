'''
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
El nombre de usuario debe ser alfanumérico.
Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
Nombre de usuario válido, retorna True.
'''
import string
user = 'xiSxS232'
if len(user) < 6:
    print('username very short!, pls write a with more digits!')
elif len(user) > 12:
     print('username very long!, pls write a with less digits!')
else:
    alphaNum = list()
    ans = str()
    alph = string.digits + string.digits
    for i in alph:
        alphaNum.append(i)
    for i in user:
        if alphaNum.count(i):
            ans = f'done u name is {user} ...'
        else:
            ans = f'u name only can have characters alphanumeric!'
    print(ans)