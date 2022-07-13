print('Bienvenidos a Kiwi-Factory')
print('''
(A) RAM 8GB
(B) SSD 256GB
(C) RAM 8GB y SSD 256GB
''')
opcion = str(input('¿Cuáles productos comprará?: ')).upper()
if opcion == 'A':
    unidades = int(input('¿Cuántas unidades de RAM 8GB?: '))
    if unidades == 1:
        precio = 18500
    elif unidades == 2 or unidades == 3:
        precio = 18000
    else:
        precio = 15500
    total = precio * unidades
    print(f'Subtotal productos: ${total}')
elif opcion == 'B':
    unidades = int(input('¿Cuántas unidades de SSD 256GB?: '))
    if unidades == 1:
        precio = 42200
    elif unidades == 2 or unidades == 3:
        precio = 40000
    else:
        precio = 35000
    total = precio * unidades
    print(f'Subtotal productos: ${total}')
elif opcion == 'C':
    unidadesRam = int(input('¿Cuántas unidades de RAM 8GB?: '))
    if unidadesRam == 1:
        precioRam = 18500
    elif unidadesRam == 2 or unidadesRam == 3:
        precioRam = 18000
    else:
        precioRam = 15500
    unidadesSdd = int(input('¿Cuántas unidades de SSD 256GB?: '))
    if unidadesSdd == 1:
        precioSdd = 42200
    elif unidadesSdd == 2 or unidadesSdd == 3:
        precioSdd = 40000 
    else:
        precioSdd = 35000 
    total = (precioRam * unidadesRam) + (precioSdd * unidadesSdd)
    print(f'Subtotal productos: ${total}')
else:
    print('Error')
    quit()
contador = 0
descuento = 0
while contador < 3:
    codigo = str(input('Ingrese código de descuento: '))
    if codigo == 'uwu-131':
        descuento = total*0.1
        if descuento > 100000:
            descuento = 100000
            print(f'Descuento: $ {int(descuento)}')
            subTotal = total-descuento
            print(f'Subtotal: $ {int(subTotal)}')
            break
        else:
            print(f'Descuento: $ {int(descuento)}')
            subTotal = total-int(descuento)
            print(f'Subtotal: $ {int(subTotal)}')
            break
    else:
        print('Codigo invalido')
        contador += 1
if descuento == 0:
    subTotal = total
    print(f'Descuento: $ {int(descuento)}')
    print(f'Subtotal: $ {int(total)}')
envio = int(input(f'Envío a domicilio (1) / Retiro en tienda (2): '))
if envio == 1:
    costoEnvio = 4990
    if int(subTotal) > 75000:
        costoEnvio = 0
        print(f'Costo envío: $ {costoEnvio}')
        print(f'Total: ${subTotal}')
    else:
        print(f'Costo envío: $ {costoEnvio}')
        print(f'Total: ${subTotal + costoEnvio}')
elif envio == 2:
    costoEnvio = 0
    print(f'Costo envío: $ {costoEnvio}')
    print(f'Total: $ {subTotal}')
else:
    print('Error')
    
