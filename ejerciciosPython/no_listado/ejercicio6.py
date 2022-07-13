palabra = str(input('Palabra: '))
arr = ['a','e','i','o','u']
nuevaPalabra = []
if len(palabra) < 6:
    print(palabra)
else:
    for i in palabra:
        if arr.count(i):
           i = ''
        else:
            nuevaPalabra.append(i)
print(''.join(nuevaPalabra))