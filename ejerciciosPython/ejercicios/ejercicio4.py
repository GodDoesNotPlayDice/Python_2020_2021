'''
Traducir normal a jerigonzio

'''
def jer(text):
    vocals = ['a','e','i','o','u']
    arr = []
    for i in text:
        if vocals.count(i):
            i = i+'p'+i
        arr.append(i)
    return ''.join(arr)

print(jer('hola como estamos'))