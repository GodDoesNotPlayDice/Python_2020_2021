import scripts.functions as func
def main():
    try:
        print("Bienvenido al simulador")
        poke,pokeStats = func.selectPokemon()
        pokemonBase = func.getPokemonBase(poke)
        print(f'Mi Pokemon: {pokemonBase}')
        print('Movimientos que puede aprender el pokémon: ')
        func.pokeSkills(pokeStats)
        power = func.validPower(pokeStats)
        print(f'El ataque seleccionado es: {power[0]}')
        print(f'Poder de ataque es: {power[1]}')
        MyPokemon = func.pokemon(poke)
        print(MyPokemon.getInfo())
        pokeRival = func.selectRival()
        pokeRivalObj = func.pokemon(pokeRival)
        print(f'El hp al nivel 50 de {pokeRivalObj.getName()} es de {pokeRivalObj.getHp()}')
        return func.result(power,pokeRival,pokeRivalObj,MyPokemon)
    except KeyboardInterrupt: 
        print('Saliendo del programa')
        quit(0)

print(main())