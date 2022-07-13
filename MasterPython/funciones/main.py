"""
Una función es un conjunto de instrucciones agrupadas bajo un numbre concreto que pueden reutilizarse invocando a la función tantas veces como sea necesario

ej:

def NombreDeFuncion(parametros):
    # Bloque de codigo o conjunto de instrucciones

NombreDeFuncion(parametros)

"""

def showNames():
    print('Vicente')
    print('Daniela')
    print('Kaffito')

# showNames() 

"""
Parametros, es un dato que se pasa desde afuera para adentro de la función

"""
def ShowYourName(name, edad):
    print(f'Tu nombre es: {name}')
    if edad >=18:
        print(f'Hola {name} tienes {edad} eres mayor de edad')

# yourName = str(input('Introduce tu nombre: '))
# yourAge = int(input('Introduce tu edad: '))

# ShowYourName(yourName,yourAge)


"""
    Siguiente ejemplo:
        tablas de multiplicar

"""

def tabla(numero):
    print(f'\n tabla de multiplicar del numero: {numero} \n')
    for count in range(11):
        op = numero * count
        print(f'{numero} X {count} = {op}')

# tabla(3)
# tabla(12)
# tabla(7)

"""
Siguiente ejemplo:
    todas las tablas de multiplicar
"""
# for n_tabla in range(11):
    # tabla(n_tabla)

"""
Siguiente ejemplo:
    Parametros opcionales
"""

def getEmepleado(nombre,dni = None):
    print('Empleado')
    print(f'Nombre: {nombre}')
    if dni != None:
        print(f'DNI: {dni}')

# getEmepleado('Vicente')


"""
Siguiente ejemplo: 
    Parametros opcionales con return
"""
#Ejemplo con return
def saludame(nombre):
    saludo = f'Hola, saludos {nombre}'
    return saludo

# print(saludame('vicente'))

#Calculadora
def calculadora(n1, n2, basicas = False):
    suma = n1 + n2
    res = n1 - n2
    mult = n1 * n2
    div = n1 / n2

    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(res)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(mult)
        cadena += "\n"
        cadena += "División: " + str(div)

    return cadena

# print(calculadora(5,5,True))

    

"""
Siguiente ejemplo:
    Funciones dentro de funciones
"""

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto
def getApellido(apellidos):
    texto = f"El apellido es: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellido(apellidos)
    return texto

# print(devuelveTodo('Vicente','Vasquez'))

"""
Siguiente ejemplo:
    Función lambda o anonima:
        Estas funciones sirven para tareas simples y sencillas pero que pueden volverse repetitivas y que todo su contenido se traduce en una linea en el codigo
"""

getYear = lambda year: f'El año es {year * 50}'
print(getYear(2034))



