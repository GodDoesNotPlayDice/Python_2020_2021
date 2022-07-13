# Herencia: Es la posibilidad de compartir atributos y metodos entre clases, y que diferentes clases hereden de otras.

class Persona:
    '''
    nombre
    apellidos
    altura
    edad
    '''

    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellidos
    def getAltura(self):
        return self.altura
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellidos):
        self.apellidos = apellidos
    def setAltura(self, altura):
        self.altura = altura
    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return 'Estoy hablando'
    def caminar(self):
        return 'Estoy caminando'
    def dormir(self):
        return 'Estoy durmiendo'

class Informatico(Persona):
    '''
    lenguajes
    experiencia
    '''

    def __init__(self):
        self.lenguajes = 'HTML, CSS, JavaScipt, PHP'
        self.experiencia = 5
    def getLenguajes(self):
        return self.lenguajes
    def setLenguajes(self, lenguajes):
        self.lenguajes = lenguajes
    
    def programar(self):
        return 'Estoy programando'

    def reperarPC(self):
        return 'He reparado tu PC'

class TecnicoRedes(Informatico):
    # Para acceder al constructor de la clase padre usamos
    def __init__(self):
        super().__init__()
        self.auditarRedes = 'Experto'
        self.experienciaRedes = 15

    def auditoria(self):
        return 'Estoy auditando una red'