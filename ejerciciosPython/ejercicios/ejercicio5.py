def btlShipTable():
    import string
    cont = 0
    arr = []
    while True:
        try:
            tablero = int(input('Tamaño del tablero: '))
            if tablero<=3:
                print('El tamaño del tablero tiene que ser sobre 3!')
                continue
            else:
                break
        except:
            print('Ingresa un dato valido!')
    while cont<tablero:
        arr.append(['-']*tablero)
        cont+=1
    cont = 0
    takesLetters = list(string.ascii_uppercase)
    while True:
        try:
            boats = int(input('Cantidad de barcos: '))
            if boats<=0:
                print('La cantidad de barcos no puede ser 0 ni menor que 0!')
            else:
                break
        except:
            print('Ingresa un dato valido!')
    contMarker = 1
    while cont<boats:
        print(arr)
        print(f'La columna del barco tiene de la letra {takesLetters[0]} al {takesLetters[tablero-1]}')
        while True:
            try:
                letter = str(input(f'Columna del barco numero {contMarker}: ')).upper().strip()
                if letter == ValueError() or letter == '':
                    print(f'La columna tiene que ser una letra del {takesLetters[0]} al {takesLetters[tablero-1]}')
                    continue
                else:
                    break
            except:
                print('Dato no valido!')
        while True:
            try:
                posX = int(input(f'Numero del 1 al {tablero}: '))-1
                if posX<=-1:
                    print('La poscision tiene que ser mayor a 0')
                else:
                    break
            except:
                print('Dato no valido!')
        posY = list(string.ascii_uppercase).index(letter)
        arr[posY].pop(posX)
        arr[posY].insert(posX,'X')
        contMarker+=1
        cont+=1
    return arr
print(btlShipTable())