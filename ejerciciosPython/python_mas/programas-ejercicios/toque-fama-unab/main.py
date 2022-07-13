import os, random
chanceList = list()
toquePointsList = []
famaPointsList = []
def numbersGen(number):
       cont = 0
       arr = list()
       while cont <= number-1:
           genNum = random.randrange(1,10)
           arr.append(genNum)
           cont += 1
       return arr
def chanceLister(number):
    chanceList.append(number)
    return chanceList
def chanceValidator(numberList = list(), chanceList = list(), chanceNum = int(), indice = int()):
    toque = 0
    fama = 0
    if numberList[indice] == chanceList[indice] and numberList.count(chanceNum):
        fama+=1
        famaPointsList.append(fama)
        numberList[indice] = ''       
    elif numberList.count(chanceNum):
        toque+=1
        toquePointsList.append(toque)
        
def toquesPoints():
    toquePoints = 0
    for t in toquePointsList:
        toquePoints+=t
    return f'Toques: {toquePoints}'        
def famasPoints():
    famaPoints = 0
    for t in famaPointsList:
        famaPoints+=t
    return f'Famas: {famaPoints}'
def winValue(number):
    for i in numberList:
        if i != '':
            return False
    return True
def attepmsOut(a,b):
    if a > b:
        return True

def attempsUsed(attemps):
    return f'numero de intentos utilizados: {attemps}'

os.system('cls')
print('''
     Menu de toque y fama!

        [1] - Start
        [0] - Exit
''')
select = -1
gamesCont = 0
winGame = 0
lossGame = 0
try:
    while not select == 0 or KeyboardInterrupt == True:
        try:
            select = int(input('Selecciona una opcion: '))
            if select == 1:
                n = 0
                while not (4 <= n <= 9):                  
                    try:
                        n = int(input('Que tan largo quieres que sea tu numero secreto, 4 y 9?: '))
                    except ValueError:
                        print('Dato no valido!')
                while True:
                    attemps = int(input('Ingresa tu numero de intentos: '))
                    if attemps > 0:
                        break  
                cont = 1
                indice = 0
                toquePointsList = []
                famaPointsList = []
                fama = famaPointsList
                toques = toquePointsList
                number = n
                numberList = numbersGen(n)
                contAttemps = 0
                gamesCont+=1
                intento = 1
                os.system('cls')
                print(f' - - - Bienvenido a Toque y Fama! - - - \nTu numero secreto es de {numberList} digitos, tienes {attemps} intentos')
                while cont <= attemps+1:
                    if winValue(n) == True:
                        print('Felicitaciones Has Ganado, Selecciona [1] para volver a jugar! o [0] para salir y ver tus estadisticas.')
                        print('Has acertado a todos los numeros!')
                        print(attempsUsed(cont-1))
                        winGame+=1
                        break
                    if attepmsOut(intento,attemps) == True:
                        print('Intentos Exedidos, Partida perdida. / Selecciona [1] para volver a jugar! o [0] para salir y ver tus estadisticas.')
                        lossGame+=1
                        break
                    indice = 0
                    chanceList = []
                    numcont = 1
                    print(f'------ Intento numero {intento} -------')  
                    try:
                        while numcont < n+1:
                            try:
                                if winValue(n) == True:
                                    break
                                else:     
                                    chance = int(input(f'digito numero {numcont}: '))
                                    numcont+=1
                                    chanceList = chanceLister(chance)
                                    chanceValidator(numberList, chanceList, chance, indice)
                                    indice += 1
                                    print(numberList)
                                    print(f'{famasPoints()}\n{toquesPoints()}')
                            except ValueError:
                                print('Ingresa un numero valido')
                        intento+=1
                    except ValueError:
                        print('Ingresa una opcion valida!')
                    cont += 1
            elif select == 0:
                if gamesCont == 0:
                    print('Has salido del Juego!')
                    break
                else:
                    print('Has salido del Juego!')
                    print(f'Estadisticas:\nPartidas Jugadas: {gamesCont}\nPartidas Ganadas: {winGame}\nPartidas Perdidas: {lossGame}')
                    break
            else:
                print('Esa Opcion no esta disponible')
        except ValueError:
            print('Ingresa una opcion valida!')
        except NameError:
            print('Ingresa una opcion valida!')
except KeyboardInterrupt:
    os.system('cls')
    print('Has salido del programa con exito!')
