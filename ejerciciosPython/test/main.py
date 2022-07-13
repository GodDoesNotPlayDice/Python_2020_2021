class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def setNombre(self, nombre):
        self.nombre = nombre
    def setEdad(self, edad):
        self.edad = edad
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad

    def esMayorDeEdad(self):
        if self.edad < 18:
            return False
        else:
            return True
    @staticmethod
    def getMayor(persona1, persona2):
        if persona1.getEdad() > persona2.getEdad():
            return persona1.getEdad()
        else:
            return persona2.getEdad()


yo = Persona('vicente',9)
el = Persona('haiko', 10)
print(yo.getMayor(yo,el))
