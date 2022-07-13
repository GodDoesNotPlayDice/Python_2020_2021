import functions, os
print('''
     Menu de toque y fama!

        [1] - Start
        [0] - Exit
''')
select = -1
try:
    while not select == 0 or KeyboardInterrupt == True:
        try:
            select = int(input('Selecciona una opcion: '))
            if select == 0:
                print('Has salido del Juego!')
            elif select == 1:
                cont = 1
                index = 0
                functions.toquePointsList = []
                functions.famaPointsList = []
                fama = functions.famaPointsList
                toques = functions.toquePointsList
                number = functions.randomNumber()
                numberList = functions.numbersGen(number())
                os.system('cls')
                print(f' - - - Bienvenido a Toque y Fama! - - - \nTu numero secreto es de {number()} digitos, tienes {number()} intentos')
                while cont < int(number())+1:
                    try:
                        chance = int(input(f'intento numero: {cont}: '))
                        chanceList = functions.chanceLister(chance)
                        cont += 1
                        functions.chanceValidator(numberList, chanceList, chance, index)
                        index += 1
                        print(f'{functions.famasPoints()}\n{functions.toquesPoints()}')
                    except ValueError:
                        print('Ingresa una opcion valida!')
                print()
            else:
                print('Esa Opcion no esta disponible')
        except ValueError:
            print('Ingresa una opcion valida!')
except KeyboardInterrupt:
    os.system('cls')
    print('Has salido del programa con exito!')
