''''
El constructor:
    es un metodo especial dentro de una clase, y se suele utilizar para darle un valor a los atributos del objeto al crearlo, es el primer metodo que se ejecuta al crear un objeto, y se llama automaticamete al crearlo, este metodo puede recibir parametros, y para pasarselos simplemente tenemos que pasarselo cuando se invoca la clase

'''





class Coche:
    # Atributos(ex variables)
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

        self.soy_publico = 'Hola, soy un atributo publico'
        self.__soy_privado = 'Hola, soy un atributo privado'

    # Metodos, son acciones que hace el objeto
    def  getPrivado(self):
        return self.__soy_privado
    #Sacar atributto privado
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setModelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo
    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca

    def getInfo(self):
        info = '---- Informacion del coche ----'
        info += '\n Color: ' + self.getColor()
        info += '\n Marca: ' + self.getMarca()
        info += '\n Modelo: ' + self.getModelo()
        info += '\n Velocidad: ' + str(self.getVelocidad())
        return info



coche = Coche()
print(coche)