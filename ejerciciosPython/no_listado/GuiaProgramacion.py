n1 = 900
n2 = 100
n3 = 600

def maxi(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
def mini(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3

def middle(n1,n2,n3):
    op = (n1 + n2 + n3) - mini(n1,n2,n3) - maxi(n1,n2,n3)
    return op

minimo = mini(n1,n2,n3)
medio = middle(n1,n2,n3)
maximo = maxi(n1,n2,n3)
print(f'Numeros ordenados: {minimo}, {medio}, {maximo}')