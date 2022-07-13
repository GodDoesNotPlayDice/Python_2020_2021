def getPokemons():
    file = open('PokemonPython/src/pokemon_data.csv', 'r')
    return file.readlines()
def getEffectTable():
    file = open('PokemonPython/src/tabla_efectividad.csv', 'r')
    return file.readlines()