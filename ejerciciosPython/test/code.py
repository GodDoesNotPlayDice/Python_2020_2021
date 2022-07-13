import random as rnd
largo= int(input("Elige el largo del numero: "))
adivinar = ""
reinicio=1
win=0
lose=0
if largo ==4:
    for i in range(4):
        posible = rnd.randint(0, 9)
        while str(posible) in adivinar:
            posible = rnd.randint(0, 9)
        adivinar += str(posible)
    intentos = 1
    adivinado = 0
    while intentos <= 4 and adivinado != adivinar:
        adivinado = input(f"Intento {intentos}:")
        intentos += 1
        fama = 0
        toque = 0
        for i in range(4):
            if adivinar[i] == adivinado[i]:
                fama += 1
            elif adivinar[i] in adivinado:
                toque += 1
        print(f"Famas:{fama} y Toques:{toque}")
    if fama == 4:
        print("Fin del juego.")
        win+=1
    if fama != 4:
        print(f"Fin del juego. La secuencia era: {adivinar}")
        lose+=1
if largo ==5:
    for i in range(5):
        posible = rnd.randint(0, 9)
        while str(posible) in adivinar:
            posible = rnd.randint(0, 9)
        adivinar += str(posible)
    intentos = 1
    adivinado = 0
    while intentos <= 5 and adivinado != adivinar:
        adivinado = input(f"Intento {intentos}:")
        intentos += 1
        fama = 0
        toque = 0
        for i in range(5):
            if adivinar[i] == adivinado[i]:
                fama += 1
            elif adivinar[i] in adivinado:
                toque += 1
        print(f"Famas:{fama} y Toques:{toque}")
    if fama == 5:
        print("Fin del juego.")
        win+=1
    if fama != 5:
        print(f"Fin del juego. La secuencia era: {adivinar}")
        lose+=1
if largo ==6:
    for i in range(6):
        posible = rnd.randint(0,9)
        while str(posible) in adivinar:
            posible = rnd.randint(0,9)
        adivinar+= str(posible)
    intentos=1
    while intentos <=6:
        adivinado= input(f"Intento {intentos}:")
        intentos+=1
        fama= 0
        toque= 0
        for i in range (6):
            if adivinar[i] == adivinado[i]:
                fama +=1
            elif adivinar[i] in adivinado:
                toque+=1
        print(f"Famas:{fama} y Toques:{toque}")
        if fama<=6:
            print("Fin del juego.")
            win+=1
        if fama!=6:
            print(f"Fin del juego. La secuencia era: {adivinar}")
            lose+=1
if largo == 7:
    for i in range(7):
        posible = rnd.randint(0, 9)
        while str(posible) in adivinar:
            posible = rnd.randint(0, 9)
        adivinar += str(posible)
    intentos = 1
    adivinado = 0
    while intentos <= 7 and adivinado!=adivinar :
        adivinado = input(f"Intento {intentos}:")
        intentos += 1
        fama = 0
        toque = 0
        for i in range(7):
            if adivinar[i] == adivinado[i]:
                fama += 1
            elif adivinar[i] in adivinado:
                toque += 1
        print(f"Famas:{fama} y Toques:{toque}")
    if fama==7:
        print("Fin del juego.")
        win+=1
    if fama!= 7:
        print(f"Fin del juego. La secuencia era: {adivinar}")
        lose+=1
if largo == 8:
    for i in range(8):
        posible = rnd.randint(0, 9)
        while str(posible) in adivinar:
            posible = rnd.randint(0, 9)
        adivinar += str(posible)
    intentos = 1
    adivinado = 0
    while intentos <= 8 and adivinado!=adivinar :
        adivinado = input(f"Intento {intentos}:")
        intentos += 1
        fama = 0
        toque = 0
        for i in range(8):
            if adivinar[i] == adivinado[i]:
                fama += 1
            elif adivinar[i] in adivinado:
                toque += 1
        print(f"Famas:{fama} y Toques:{toque}")
    if fama==8:
        print("Fin del juego.")
        win+=1
    if fama!= 8:
        print(f"Fin del juego. La secuencia era: {adivinar}")
        lose+=1
if largo ==9:
    for i in range(9):
        posible = rnd.randint(0, 9)
        while str(posible) in adivinar:
            posible = rnd.randint(0, 9)
        adivinar += str(posible)
    intentos = 1
    adivinado = 0
    while intentos <= 9 and adivinado!=adivinar :
        adivinado = input(f"Intento {intentos}:")
        intentos += 1
        fama = 0
        toque = 0
        for i in range(9):
            if adivinar[i] == adivinado[i]:
                fama += 1
            elif adivinar[i] in adivinado:
                toque += 1
        print(f"Famas:{fama} y Toques:{toque}")
    if fama==9:
        print("Fin del juego.")
        win+=1
    if fama!= 9:
        print(f"Fin del juego. La secuencia era: {adivinar}")
        lose+=1
reinicio=int(input("¿Deseas jugar nuevamente? 1.Si/0.No:"))
if reinicio==0:
    jugados=win + lose
    print(f"Jugados:{jugados}-Ganados:{win}-Perdidos:{lose}.")