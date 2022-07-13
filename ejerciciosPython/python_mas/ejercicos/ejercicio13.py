"""
Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

"""
t = 'radar'
def pal(a):
    arr=list(a)
    arr.reverse()
    x=str().join(arr)
    if x == a:
        return f'Tu palabra {a} es palindroma!', True
    else:
        return f'la palabra {a} no es palíndroma con {x}', False

print(pal(t))