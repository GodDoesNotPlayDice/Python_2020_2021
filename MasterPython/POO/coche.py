from constructor import Coche

carro = Coche('azul', 'Renautl', 'Clio', 150, 200, 4)
carro2 = Coche('verde', 'Seat', 'Panda', 240, 200, 4)
carro3 = Coche('rojo', 'Citroen', 'Xara', 100, 180, 4)
carro4 = Coche('amarillo', 'Mercedes', 'Clase A', 350, 400, 4)
print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

# Extra, detectar tipado

if type(carro3) == Coche:
    print('Es un obejto')
else:
    print('No es un obejto')


# Visibilidad
print(carro.soy_publico)
print(carro.getPrivado())