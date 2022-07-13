class Persona:
    def __init__(self, nombre, edad): #init inicializa el objeto al momento de crearlo osea un constructor
        self.nombre = nombre
        self.edad = edad
    def __str__(self): # __str__ devuelve el objeto en una cadena de texto
        return f'Nombre: {self.nombre} \nEdad: {str(self.edad)}'

juan = Persona('Juan', 20)
print(juan)

print(dir(Persona)) # La dir() función devuelve todas las propiedades y métodos del objeto especificado, sin los valores.