class Persona:
    """
    Description of Persona

    Attributes:
        nombre (type):
        edad (type):

    Args:
        nombre (undefined):
        edad (undefined):

    """
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def getInfo(self):
        if self.edad < 18:
            return f'{self.nombre} es menor de edad su edad es: {self.edad}'
        else:
            return f'{self.nombre} es mayor de edad su edad es: {self.edad}'

persona1 = Persona('vicente',10)
print(persona1.getInfo())