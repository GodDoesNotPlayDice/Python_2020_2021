from math import sqrt
cont = 1
volumenFinal = 0
precioFinal = 0
while cont < 4:
    peso = int(input(f'Ingrese peso del paquete {cont} [grs]: '))
    alto = int(input(f'alto paquete {cont} en [cm]: '))
    ancho = int(input(f'ancho paquete {cont} en [cm]: '))
    largo = int(input(f'largo paquete {cont} en [cm]: '))
    volumen = largo * ancho * alto
    volumenFinal += volumen
    print(f'Volumen paquete {cont}: {float(volumen)} [cm3]')
    peso = peso * 1200.15
    volumen = volumen * 155.87
    resEcu = peso + volumen
    res = round(resEcu**(1/3))
    print(f'Valor almacenaje paquete {cont}: ${res}')
    precioFinal += res
    cont+=1
    print('\n')
print(f'Volumen ocupado por los 3 paquetes: {volumenFinal} [cm3]')
x = float(input(f'Ingrese coord X del punto de destino: '))
y = float(input(f'Ingrese coord Y del punto de destino: '))
destino = sqrt(x**2 + y**2)
valorDestino = int(destino) * 1500
print(f'Distancia es: {round(destino,1)} [KM]')

print('_____________________________________________________________________________')
print('DETALLE DE COBRO POR SERVICIO')
print(f'Almacenaje: $ {precioFinal}')
print(f'Traslado: $ {valorDestino}')
total = precioFinal + valorDestino
print(f'Total a pagar: $ {total}')
print('_____________________________________________________________________________')
print('Hasta pronto !!')