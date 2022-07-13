def generar_palabra():
    # Retorna una palabra al azar desde una lista de palabras
    # No se preocupe por comprender cómo esta función hace su trabajo
    from random import choice
    lista = ["pandemia","programación","paralelepipedo","equilatero","panaderia","automatizacion"] # lista de palabras en minúsculas, sin tildes ni otros símbolos
    pala = choice(lista)
    return pala

def palabra_encriptada(palabra):
    encri = ""
    for x in palabra:
        encri+="_ "  # se cambia la letra de la palabra por un guión bajo y un espacio
    return encri




# test="holo"
# print(test.index("o"))

# Escriba aquí su implementación de la función verificar_letra
def verificar_letra(palabra, letra):
    return True if letra in palabra else False

# Escriba aquí su implementación de la función mostrar_letra
def mostrar_letra(palabra, encriptada, letra):
    palabraAux=list(encriptada)
    posicion=[]
    if(verificar_letra(palabra,letra)):
        for x in range(len(palabra)):
            if(letra==palabra[x]):
                posicion.append(x)
        for y in posicion:
            palabraAux[y]=str(letra)
    
    return "".join(palabraAux)

# Programa principal:
cont = 1
games = []
while cont < 6:
    letra = str(input("letra: "))
    palabra = generar_palabra()
    encript = palabra_encriptada(palabra)
    verif = verificar_letra(palabra,letra)
    games.append([mostrar_letra(palabra,encript,letra)])
    print(games)
    cont+=1

# print("Bienvenidos al juego del adivinador de palabras!!!")

# Complete aquí el programa que implementa el juego

# print("Fin del juego")