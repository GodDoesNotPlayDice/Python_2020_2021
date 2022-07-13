"""
Ejercicio 6.
    Moestrar todas la tablas de multiplicar del 1 al 10 moestrando el titulo de la tabla del 1 al 10

"""

#tabla del uno
for top in range(1, 11):
    print('##########')
    print(f'tabla del {top}')
    print('##########')
    for n in range(1, 11):
        print(f'{n} x {top} = {n*top}')
    print("\n")