# Capturar execepciones y manejar errores en codigo
# suceptible a fallos/errores


'''
try:
    nombre = input('Introduce tu nombre: ')
    if len(nombre) > 1:
        user = f'Tu nombre es {nombre}'
    print(user)
except:
    print('Ha Ocurrido un Error')
'''
# Multiples exepciones

try:
    numero = input('Numero para elevarlo al cuadrado: ')
    print(f'El cuadrado del numero es: {numero*numero}')
# except TypeError:
#     print('Debes convertir tus cadenas a enteros en el codigo!')
except ValueError:
    print('Introduce un numero correcto')
except Exception as error:
    print('Ha ocurrido un error: ', type(error).__name__)

# Excepciones personalizadas o lanzar exepciones
'''
try:
    nombre = input('Introduce el nombre: ')
    edad = int(input('Introduce la edad: '))
    if edad < 5 or edad > 110:
        raise ValueError('La edad introducida no es real')
    elif len(nombre) <= 1:
        raise ValueError('El nombre no esta completo')
    else:
        print('Bienvenido a la plataforma')
except ValueError:
    print('Introduce los datos correctamente')
except Exception as e:
    print('Existe un error', e)

'''