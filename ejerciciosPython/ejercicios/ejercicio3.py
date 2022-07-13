'''

El juego consiste en tratar de adivinar una palabra secreta, dando algunas letras como pista. La persona tiene hasta 7 intentos para adivinar la palabra.

Tu programa debe:

    Crear una lista con palabras secretas, y escoge aleatoriamente cuál palabra usarás para el juego.
    Escoger aleatoriamente cuántas letras mostrar de la palabra secreta, de acuerdo a la longitud de la palabra. Para ocultar las letras crea la función ocultarletras(palabra, cantidad) que debe recibir como parámetro la palabra secreta y ocultar la cantidad de letras indicada, en posiciones aleatoriamente escogidas, reemplazándolas por “”. Ej. ocultar_letras(“lepidoptero”,1) podría retornar “_epidoptero”, “lepdoptero”, “lepidopter”, etc.
    El jugador debe poder ingresar una letra o arriesgarse a decir la palabra completa. Para revisar si una letra ingresada por el jugador existe en la palabra, crea la función revisar_letra(palabra_secreta, palabra, letra) que verifica si letra existe en la palabra secreta y la reemplaza en todas las posiciones que aparece en la palabra con las letras ocultadas, retornando la nueva palabra que debe mostrarse al jugador. Ej. revisarletra(“lepidoptero”, ”lepidopter”, ”o”) debería retornar lepidoptero.

'''

import random
# Escojer palabra aleatoria
arr = ['lepidoptero','perro','gato','elefante']
secretIndex = random.randint(0,len(arr)-1)
secretWord = arr[secretIndex]

# Ocultar letras
def hidenWords(secretWord,cantidad):
    arr = []
    for i in secretWord:
        arr.append(i)
    cont=0
    while cont<cantidad:
        while True:
            hideWordIndex = 0
            if hideWordIndex == hideWordIndex:
                hideWordIndex = random.randint(0,len(secretWord)-1)
        if arr[hideWordIndex]:
            arr.pop(hideWordIndex)
            arr.insert(hideWordIndex,'_')
        elif not arr.count(arr[hideWordIndex]):
            pass
        cont+=1
    return arr

print(hidenWords(secretWord, 3))