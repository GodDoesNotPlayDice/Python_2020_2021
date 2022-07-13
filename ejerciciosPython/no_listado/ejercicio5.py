numero = input('numero: ')
suma = 0
for i in numero:
    suma += int(i)**len(numero)
print('Es de Armstrong' if int(numero)==suma else 'No es Armstrong')