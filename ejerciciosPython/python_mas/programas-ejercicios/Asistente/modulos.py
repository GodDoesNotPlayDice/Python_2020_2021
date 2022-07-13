class Usuario:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
    def __str__(self):
        return f'Usuario: {self.usuario}\nPassword: {self.password}'

    def getUsuario(self):
        return str(self.usuario)
    def getPassword(self):
        return str(self.password)