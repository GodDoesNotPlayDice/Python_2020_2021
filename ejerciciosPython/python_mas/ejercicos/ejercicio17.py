"""
 Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

"""

def max_in_list(a=[]):
    z=0
    for i in a:
        if i > z:
            z=i
    return z
print(max_in_list([1,10,60,5,100,2,502220,123,564,3421,45]))