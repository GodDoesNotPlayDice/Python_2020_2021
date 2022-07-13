class Calculadora:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def getSuma(self):
        return f'Tu suma es de: {self.a + self.b}'
    def getResta(self):
        return f'Tu resta es de: {self.a - self.b}'
    def getDivision(self):
        return f'Tu division es de: {self.a / self.b}'
    def getMultiplicacion(self):
        return f'Tu multiplicacion es de: {self.a * self.b}'
    def getInfo(self):
        return f'Tu suma es de: {self.a + self.b}\nTu resta es de: {self.a - self.b}\nTu division es de: {self.a / self.b}\nTu multiplicacion es de: {self.a * self.b}'

calculadora = Calculadora(10,20)

print(calculadora.getMultiplicacion())
print(calculadora.getInfo())