"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******

"""

def his(a=list()):
    for x in a:
        op=x*'*'    
        print(f'{op}')

his([2,3,6,10])