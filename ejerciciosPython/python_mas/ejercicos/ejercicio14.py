"""
 Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

"""


"""
Solution whitout nested loop

k = [1,2,3,4,5]
l = [8,0,1]
def sup(a=list(),b=list()):
    a=set(a)
    b=set(b)
    if a.isdisjoint(b):
        return False
    else:
        return True
print(sup(k,l))

"""

# solution whit nested loop
k = [1,2,3,4,5]
l = [8,0]
def supp(a=list(),b=list()):
    wr1=set()
    wr2=set()
    for x in a:
        wr1.add(x)
        for z in b:
            wr2.add(z)
    if wr1.isdisjoint(wr2):
        return False
    else:
        return True

print(supp(k,l))

"""
orther solution

def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False
    
"""