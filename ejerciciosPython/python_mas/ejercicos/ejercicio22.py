try:
    numero = (input("Ingrese numero telefonico: "))
    hora = int(input("Ingrese hora de la llamada: "))
    numList = list()
    for i in numero:
        numList.append(i)
    exepcion = ['9','0','9']
    exepcionDos = ['8','7','7']
    print(numList[-3:])
    if len(numero) < 8 or len(numero) > 8:
        print("ingrese un numero telefonico de 8 cifras")

    rango = range(0,24)
    arr = list()
    for i in rango:
        arr.append(i)
    if arr.count(hora):
        horario_uno = arr[0:8]
        horario_dos = arr[8:15]
        horario_tres = arr[17:20]
        horario_cuatro = arr[20:24]
        if horario_uno.count(hora):
            print('Contestar')
        if horario_dos.count(hora):
            if horario_dos.count(hora) and numList[-3:] == exepcion[0:3]:
                print('Contestar')
            else:
                print('No contestar')
        if horario_tres.count(hora):
            if horario_tres.count(hora) and numList[0:3] == exepcionDos[0:3]:
                print('No contestar')
            else:
                print('Contestar')
        if horario_cuatro.count(hora):
            print('No contestar')
    else:
        print('Ingresa una Hora valida')
except ValueError:
    print('Ingresa algo valido')
