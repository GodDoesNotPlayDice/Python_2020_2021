from scripts.moves import get_move
from math import *
from random import uniform
import src.db as db

iv,lvl,ev= 31,50,250
pokemons = db.getPokemons()
table = db.getEffectTable()
def pokeBox():
    arr = []
    pokeList = []
    nameList = []
    for i in pokemons:
        arr.append(i.replace(';',','))
    for i in arr:
        pokeList.append(i.split(','))
    for i in range(0,len(pokeList)):
        nameList.append(pokeList[i][0])
    return nameList,pokeList

class PKM:
    def __init__(self,name,tipo,hp,attack,defe,atks,defs,speed):
        self.name = name
        self.tipo = tipo
        self.hp = hp
        self.atk = attack
        self.defe = defe
        self.atks = atks
        self.defs = defs
        self.speed = speed

    def setHp(self):
        return ((((self.hp+iv)*2+(sqrt(ev)/4))*lvl)/100)+lvl+10
    def setAtack(self):
        return ((((self.atk+iv)*2+(sqrt(ev)/4))*lvl)/100)+5
    def setDef(self):
        return ((((self.defe+iv)*2+(sqrt(ev)/4))*lvl)/100)+5
    def setAtkSpecial(self):
        return ((((self.atks+iv)*2+(sqrt(ev)/4))*lvl)/100)+5
    def setDefSpecial(self):
        return ((((self.defs+iv)*2+(sqrt(ev)/4))*lvl)/100)+5
    def setSpeed(self):
        return ((((self.speed+iv)*2+(sqrt(ev)/4))*lvl)/100)+5
    def getName(self):
        return self.name.capitalize()
    def getType(self):
        return self.tipo
    def getHp(self):
        return self.setHp()
    def getDamageSpecial(self):
        return self.setAtkSpecial()
    def getDefSpecial(self):
        return self.setDefSpecial()
    def getPysDef(self):
        return self.setDef()
    def getDamagePys(self):
        return self.setAtack()
        
    def getInfo(self):
        return f'''
        Nombre: {self.name.capitalize()}
        Nivel: {lvl}
        Tipo: {self.tipo.capitalize()}
        Vida: {str(int(self.setHp()))}
        Ataque: {str(int(self.setAtack()))}
        defesa: {str(int(self.setDef()))}
        Ataque Especial: {str(int(self.setAtkSpecial()))}
        defesa Especial: {str(int(self.setDefSpecial()))}
        Velocidad: {str(int(self.setSpeed()))}
        '''

def pokemon(poke):
    pokemon = PKM(poke[0],poke[1],int(poke[2]),int(poke[3]),int(poke[4]),int(poke[5]),int(poke[6]),int(poke[7]))
    return pokemon
def getPokemonBase(poke):
    return f'''
    Nombre: {poke[0].capitalize()}
    Nivel: {1}
    Tipo: {poke[1].capitalize()}
    Vida: {str(poke[2])}
    Ataque: {str(poke[3])}
    Defesa: {str(poke[4])}
    Ataque Especial: {str(poke[5])}
    Defensa Especial: {str(poke[6])}
    Velocidad: {str(poke[7])} 
        '''
def vs(atk,defen):
    atkTable = []
    atkIndex = int()
    defenIndex = int()
    for i in table:
        atkTable.append(i.split(','))
    atkTable[0].pop(0)
    tableTypeDef = atkTable[0][0:18]
    atkTable.pop(0)
    if tableTypeDef.count(defen):
        defenIndex = tableTypeDef.index(defen)
    for i in range(0,len(atkTable)):
        if atkTable[i].count(atk):
            atkIndex = i
            atkTable[i].pop(0)
    return float(atkTable[atkIndex][defenIndex])


def modifier(type,poke1,poke2):
    stab = 1.2
    if poke1 == poke2:
        stab = 1.0
    return type * stab *uniform(.85,1.0)* 1
def damage(power,modify,a,d):
    return ((((((2*50)/5)+2)*power*a/d)/50)+2)*modify

def pokeSkills(pokeStats):
    cont = 1
    for i in pokeStats:
            print(f'{cont} - {i}')
            cont+=1

def pokeAtk(pokeStats,pokeIndex):
    return get_move(pokeStats[pokeIndex])

def validPower(Stats):
    while True:
        try:
            pokeStatsIndex = int(input('Selecciona un ataque: '))
            if pokeStatsIndex <= 0:
                    print(f"El ataque {pokeStatsIndex} no existe porfavor escoja uno de la lista!")
            else:
                power = pokeAtk(Stats,pokeStatsIndex-1)
                if power[1] != 0:
                    return power
                else:
                    print("el poder del ataque es 0, por favor selecciona otra ataque")
        except:
            print("seleccione un numero de la lista")

def msg(damage,rndHp):
    return f''' 
        Daño Causado: {damage}
        Vida Restante: {rndHp - damage}
        '''

def selectPokemon():
    while True:
        try:
            pokemon = input('Selecciona pokemon: ').lower()
            arr,pokeList = pokeBox()
            if arr.count(pokemon):
                pokeIndex = arr.index(pokemon)
                return pokeList[pokeIndex][0:8],pokeList[pokeIndex][8:-1]
        except ValueError:
            print("Selecciona un pokemon valido")

def selectRival():
    while True:
        try:
            pokemon = input('Selecciona pokemon rival: ').lower()
            arr,pokeList = pokeBox()
            if arr.count(pokemon):
                pokeIndex = arr.index(pokemon)
                return pokeList[pokeIndex][0:8]
        except ValueError:
            print("Selecciona un pokemon valido")

def result(power,pokemonRival,pokeRivalObj,pokeObj):
    modify = modifier(vs(power[2],pokemonRival[1].lower()),pokeObj.getType(),pokeRivalObj.getType())
    physicalAtkMY,specialAtkMY = pokeObj.getDamagePys(),pokeObj.getDamageSpecial()
    physicalDefRDM,spesDefRDM = pokeRivalObj.getDamagePys(),pokeRivalObj.getDefSpecial()
    if power[3] == "physical":
        Damage = damage(power[1],modify,physicalAtkMY,physicalDefRDM)
        return msg(Damage,pokeRivalObj.getHp())
    else:
        Damage = damage(power[1],modify,specialAtkMY,spesDefRDM)
        return msg(Damage,pokeRivalObj.getHp()) 
