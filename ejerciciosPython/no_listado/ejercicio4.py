from random import randint as r
intentos = int(input('Ingrese cantidad de intentos: '))
cont = 1
ganadas = 0
perdidas = 0
while cont < intentos+1:
    while True:
        numero = input(f'Ingrese intento {cont}: ')
        if int(numero) < 999:
            print('Ingrese un numero mayor que 999')
        else:
            break
    suma = 0
    for i in numero:
        suma += int(i)
    umbral = r(1,100)
    if suma % 2 == 0:
        if suma > umbral:
            print(f'Intento ganado!! suma: {suma} umbral: {umbral}')
            ganadas +=1
        else:
            print(f'Intento perdido!! suma: {suma} umbral: {umbral}')
            perdidas +=1
    else:
        if suma < umbral:
            print(f'Intento ganado!! suma: {suma} umbral: {umbral}')
            ganadas +=1
        else:
            print(f'Intento pierde!! suma: {suma} umbral: {umbral}')
            perdidas +=1
    cont+=1
if ganadas > perdidas:
    print('Felicitaciones, ganaste la partida')
elif ganadas == perdidas:
    print('Empataste la partida')
else:
    print('Lo siento!! perdiste la partida')