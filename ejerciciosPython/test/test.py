import random
partidas = 0
partidasGanadas = 0
partidasPerdidas = 0
volverAJugar = ''
while True:
    if volverAJugar == 0:
        break
    #Verificacion del largo del numeros e intentos
    LargoNum= int(input(f"Elige el largo del número: "))
    while not (LargoNum>=4 and LargoNum<=9):
        LargoNum= int(input("Error, ingrese un numero valido: "))
        

    intentos = LargoNum
    cont = LargoNum
        
    #Generacion del numero secreto    
    numSecreto= ""
    largoNumeroSecreto= 0
    while largoNumeroSecreto!=LargoNum:
        digito= str(random.randint(0,9))
        while digito not in numSecreto:
            numSecreto= numSecreto+(digito)
            largoNumeroSecreto=len(numSecreto)
        if numSecreto[0] == '0':
            numSecreto = ''
    print(numSecreto)
    print("Numero de intentos:",intentos)
    numIntentos=1
    while True:
        if numIntentos>intentos:
            partidas+=1
            partidasPerdidas+=1
            print("El numero secreto era: ",numSecreto)
            volverAJugar = int(input('Desea volver a jugar "1" o "0": '))
            if volverAJugar == 1:
                break
            elif volverAJugar == 0:
                break
            else:
                print('ingresa si o no estupido de mierda!')
                continue

        numeroUsuario=int(input("Ingrese su numero: "))
        numeroUsuario=str(numeroUsuario)
        if numeroUsuario == numSecreto:
            partidas+=1
            partidasGanadas+=1
            print(f"¡Felicitaciones! Has acertado en {numIntentos} intentos")
            volverAJugar = int(input('Desea volver a jugar "Sí/1" o "No/0": '))
            if volverAJugar == 1:
                break
            elif volverAJugar == 0:
                break
            else:
                print('¿Deseas jugar nuevamente? 1. Sí / 0. No: 0 ')
                continue
        elif (len(numeroUsuario)!=largoNumeroSecreto):
            if numIntentos<intentos:
                cont-=1
                print(f'Numero invalido, se te resta un intento, te quedan {cont}')
                numIntentos+=1    
                continue
            else:
                print('Numero de intentos exedidos')            
        else:
            toque=0
            fama=0            
            for i in range(largoNumeroSecreto):
                if numSecreto[i] == numeroUsuario[i]:
                    fama+=1
                    toque=0 
                elif numSecreto[i] in numeroUsuario:
                    toque+=+1       
            print(f"intento numero {numIntentos}: {numeroUsuario} Toques:{toque} - Famas:{fama} ")
        numIntentos+=1
                    
print(f'''
- - - - Estadisticas - - - -
Partidas Jugadas: {partidas}
Partidas Ganadas: {partidasGanadas}
Partidas Perdidas: {partidasPerdidas}

''')


print("Ganaste")