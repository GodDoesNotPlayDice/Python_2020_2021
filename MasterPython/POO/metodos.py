# Metodos Estaticos y de Instancia
'''
Cuando el metodo contiene la palabra self se le denomina como metodo de instancia
y cuando no tiene la palabra self se le denomina como metodo estatico

'''





class Perro:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def getColor(self):
        return self.color
    def getSize(self):
        return self.size

    @staticmethod
    def perrosCatergory():
        return 'Perros altos, perros bajos'

perro1 = Perro('blanco','30cm')
print(perro1.getColor())
print(perro1.perrosCatergory())