from random import *
participantes = ['Martina','Verónica','Luisa','María','Josefa','Paulina','Amanda','Rocío','Paula','Eloísa']
competiciones = ['Barra','Suelo', 'Salto','Viga']
arr = []

compPointsAll = [[],[],[],[]]

for i in participantes:
    dicting = {
        i:{
            competiciones[0]: randint(0,10),
            competiciones[1]: randint(0,10),
            competiciones[2]: randint(0,10),
            competiciones[3]: randint(0,10),
        },
    }
    arr.append([dicting[i]['Barra'],dicting[i]['Viga'],dicting[i]['Suelo'],dicting[i]['Salto']])
print(arr)
for i in arr:
    compPointsAll[0].append(i[0])
    compPointsAll[1].append(i[1])
    compPointsAll[2].append(i[2])
    compPointsAll[3].append(i[3])
    
    
print(compPointsAll)
# print([max(i)])
# compPointsAll[1].append(arr[cont].index(max(arr[cont])))
# print(max(arr[0]))
# print(arr[0].index(max(arr[0]))) 