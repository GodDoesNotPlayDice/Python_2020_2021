import os, datetime, hashlib, usuarios.conexion as conexion
def inicio():
    # os.system('cls')
    return '''
Acciones Disponibles:
    - Registro
    - Login
    - Salir
'''
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = datetime.datetime.now()
        # Cifrar password
        cifrado = hashlib.sha256()  # Libreria de cifrado 256 recomendable
        cifrado.update(self.password.encode('utf8')) # cifrado update pasar a cifrado con metodo encode para transformar string utf8 a bytes.
        sql = 'INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)'
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha) # hexdigest devuelve el cifrado
        try:
            cursor.execute(sql, usuario)
            database.commit()
            return [cursor.rowcount, self]
        except:
            result = [0, self]
        return result
    def identificar(self):
        #Consulta para comprobar si existe el usuario.
        sql = 'SELECT * FROM usuarios WHERE email = %s AND password = %s'
        # Cifrar password
        cifrado = hashlib.sha256()  # Libreria de cifrado 256 recomendable
        cifrado.update(self.password.encode('utf8')) # cifrado update pasar a cifrado con metodo encode para transformar string utf8 a bytes.
        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        
        return result
