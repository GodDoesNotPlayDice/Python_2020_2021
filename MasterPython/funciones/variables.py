"""
Variable local: es aquella que se define dentro de la función y no puede ser utilizada fuera de esta, solo estan disponibles dentro, A no ser que se haga un return

Variable global: Son aquellas que se definen fuera de la función y puede usarse tanto fuera como adentro de esta.

"""

#Variable global
frase = 'Siempre hay pan pal que necesite comer'
print(frase)
#Varialbe local
def holaMundo():
    frase = 'Hola Mundo!!' #Si yo comento esta variable se usara la variable global fuera de la función
    print(frase)
    year = 2021
    print(year)

    global website 
    website = "vicentevasquez.es"
    print(f'dentro: {website}')
    return "Dato devuelto" + str(year)

print(holaMundo())
print(f'Fuera: {website}')