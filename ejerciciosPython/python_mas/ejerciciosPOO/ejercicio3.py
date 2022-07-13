class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        '''
        a = left side
        b = right side
        c = bottom side

        '''

    def getInfo(self):
        if self.a == self.b != self.c or self.a == self.c != self.b or self.a != self.b == self.c:
            return 'Triangulo Isósceles tiene dos lados iguales'
        elif self.a == self.b == self.c or self.a == self.b == self.c:
            return 'Triangulo Equilátero tiene todos los lados iguales'
        else:
            return 'Triangulo Escaleno tiene todos los lados diferentes'
triangulo = Triangulo(30,30,10)
print(triangulo.getInfo())