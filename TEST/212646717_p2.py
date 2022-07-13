stock = [
    ['Leche',2,500],
    ['Nescafe 200gr',4,2360],
    ['Leche',4,700],
    ['Leche',10,600],
    ['Nescafe 200gr',10,2760]
    
    ] # Lista de stock

while True: # Bucle para mantener la "interfaz del programa"
    print('Bienvenido!') 
    print('''
    (1) Revisar producto
    (2) Salir      
    ''')
    opcion = int(input('Porfavor ingrese una opcion: ')) # Opcion input
    if opcion == 1: # Condicional para el input
        producto = str(input('Ingrese el producto: ')).capitalize() # producto input
        nStock = 0 # numero de stock
        maxProducto = 0 # numero maximo del precio del prodcuto
        for i in stock: # Bucle para recorrer la lista
            if i[0] == producto: # condicional para el input del producto
                nStock += i[1] # incremento del stock
                if maxProducto < i[2]: # condicional para buscar el mas grande
                    maxProducto = i[2] # variable que guardar el maximo
        margen = maxProducto * 0.25 # calculo del margen
        precioSugerido = margen + maxProducto # precio sugerido 
        print(f'El stock de {producto} es de {nStock}')
        print(f'El precio de venta sugerido es {precioSugerido}')
    elif opcion == 2: # condicional para cerrar con break
       print('Saliendo del programa.') 
       break