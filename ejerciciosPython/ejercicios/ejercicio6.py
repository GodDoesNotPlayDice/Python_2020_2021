from os import system
while True:
    try:
        cantidadadulto = int(input("¿Cuantos adultos son?: "))
        cantidadsocios = int(input("¿cuantos socios son?:  "))
        cantidadniño = int(input("¿Cuantos niños son?:   "))
        break
    except ValueError:
        print('dato valido!')
    except KeyboardInterrupt:
            system('cls')
            print('exit successfully')
            quit()

def estadio(valorKid,valorAdulto,valorSocios):
    while(True):
        try:
            print("Bienvenido al estadio este es el menu\n\tAdultos: $4500\n\tSocios: $3500\n\tNiños: $2000")
            adultos,socios,niños = 4500,3500,2000
            adultos,socios,niños = adultos*cantidadadulto, socios*cantidadsocios,niños*cantidadniño
            print("-----------------------------")
            print(f"{cantidadadulto} adultos: ${adultos}")
            print(f"{cantidadsocios} socios:  ${socios}")
            print(f"{cantidadniño} niños:     ${niños}")
            print("-----------------------------")
            break
        except:
            system('cls')
            print("ERROR, ingrese solo numeros")

estadio(cantidadniño,cantidadadulto,cantidadniño)