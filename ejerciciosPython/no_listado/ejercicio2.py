minuntosDia = int(input('')) 
minuntosNoche = int(input(''))
exedidoNoche = 0
exedidoDia = 0
if minuntosDia > 100:
     exedidoDia = (minuntosDia*15)+1000
     print('Dia: excede')
elif minuntosDia <= 100:
    exedidoDia = minuntosDia*10
    print('Dia: no excede')

if minuntosNoche > 80:
     exedidoNoche = (minuntosNoche*15)+1000
     print('Noche: excede')
elif minuntosNoche <= 80:
    exedidoNoche = minuntosNoche*7
    print('Noche: no excede')

print(f'Cliente paga: $ {exedidoNoche + exedidoDia}')
    