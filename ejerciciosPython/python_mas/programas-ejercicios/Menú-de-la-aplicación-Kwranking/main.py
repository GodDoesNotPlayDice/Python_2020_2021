def run():
    import functions, os
    os.system('cls')
    select = -1
    try:
        while not select == 0:
            print('''
                [1] – Importar palabras clave
                [2] – Mostrar palabras clave
                [0] – Salir   
                ''')
            select = int(input('Eliga una Opcion: '))
            if select == 1:
                os.system('cls')
                functions.cargarKeyword()
            elif select == 2:
                os.system('cls')
                functions.readKeyword()
            if select == 0:
                print('Programa Finalizado con Exito!')
    except ValueError:
        os.system('cls')
        print('Introduce una opcion valida!')
    except KeyboardInterrupt:
        os.system('cls')
        print('Finalización correcta del programa!')
    except FileNotFoundError:
        print('Error Al cargar!')

run()