n1 = 10
n2 = 20
n3 = 4
arr = [n1,n2,n3]
def minMax(num):
    a = num[0] #Menor
    b = num[0] #Mayor
    for i in num:
        if i < a:
            a = i
        if i > b:
            b = i
    return a, b

maximo = minMax(arr)
menor = minMax(arr)
c = (n1 + n2 + n3) - menor[0] - maximo[1]
print(f'Numeros ordenados: {menor[0], c, maximo[1]}')
