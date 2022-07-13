import usuarios.usuario as modelo
import notas.acciones
class Acciones:
    def registro(self):
        print('Registrate :)')
        nombre = input('Cual es tu nombre?: ')
        apellidos = input('Cual es tu apellido?: ')
        email = input('Cual es tu email?: ')
        password = input('Cual es tu contraseña?: ')

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f'Perfecto! {registro[1].nombre} te has registrado con el email {registro[1].email}')
        else:
            print('\nNo te has registrado correctamente')

    def login(self):
        print('Logeate :)')
        try:
            email = input('Cual es tu email?: ')
            password = input('Cual es tu contraseña?: ')
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f'Bienvenido {login[1]}, te has registrado en el sistema, el dia {login[5]}')
                self.proximasAcciones(login)
        except TypeError:
            print(f'Login incorrecto')

    def proximasAcciones(self, usuario):
        print("""
        Acciones Disponibles:
        - Crear notas (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        accion = input('Que quieres hacer?: ')
        get = notas.acciones.Acciones()

        if accion == 'crear':
            print('vamos a crear')
            get.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'mostrar':
            print('vamos a mostar')
            get.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'eliminar':
            print('vamos a eleminar')
            get.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'salir':
            print(f'Ok {usuario[1]}, hasta pronto!!!')
            exit()
    
 