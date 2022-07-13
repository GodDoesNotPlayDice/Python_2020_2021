"""
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver
"""
def su(b):
    s=0
    for i in b:
        s+=i
    return s

def mu(b):
    s=1
    for i in b:
        s*=i
    return s

print(su([1,2,3,4]))
print(mu([1,2,3,4]))

