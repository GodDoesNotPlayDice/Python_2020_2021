'''
Clase es un molde para crear objetos con caracteristicas parecidas, y esta clase tendran metodos para hacer las funcionalidades del coche, tambien tendra atributos que seran el color, la marca etc.

Clase: Molde.
Atributo: Caracteristica.
Metodo: Funcionalidad.

'''

# Molde
class Coche:
    # Atributos(ex variables)
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos, son acciones que hace el objeto

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

# Fin de la definicion clase

# Crear objetos / Instaciar la clase

coche = Coche()


coche.setColor('amarillo')
coche.setModelo('Murcielago')
# print(coche.marca, coche.getModelo(),  coche.getColor())
# print('velocidad actual', coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()


# print('velocidad Nueva', coche.getVelocidad())  Cuando hacemos get osea la funcion retorna el valor junto self, se llama getther y es la mejor forma de retornar un valor, es hacer metodos que interactuen con propiedades y no interactuar con las propiedades directamente


# Crear mas obejtos 

coche2 = Coche()
coche2.setColor('verde')
coche2.setModelo('gallardo')
print(coche2.getColor(), coche2.getModelo())


