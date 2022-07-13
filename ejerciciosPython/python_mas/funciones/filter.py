'''
Verifica si los elementos de una secuencia cumplen una condicion devolviendo un iterador
con los elementos que cumplen dicha condicion.

'''

# def numeroPar(num):
#     if num % 2==0:
#         return True

numeros = [17,24,7,39,8,51,92]

# print(list(filter(lambda numeroPar: numeroPar % 2==0, numeros)))

class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return f'{self.nombre} que trabaja como {self.cargo} tiene un salario de {self.salario} $'


listaEmpleados = [
    Empleado('Juan','Director', 75000),
    Empleado('Ana','Presidenta', 85000),
    Empleado('Antonio','Administrativo', 25000),
    Empleado('Sara','Secretaria', 27000),
    Empleado('Mario','Botones', 21000),
]

salariosAltos = filter(lambda empleado:empleado.nombre=='Sara', listaEmpleados)
for empleadoSalarios in salariosAltos:
    print(empleadoSalarios)