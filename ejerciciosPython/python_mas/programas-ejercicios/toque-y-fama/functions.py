import random
chanceList = list()
toquePointsList = []
famaPointsList = []
def randomNumber():
    allNumbers = random.randrange(0, 100)
    filteredNumber = allNumbers % 2
    def numberSecret():
        if filteredNumber == 0:
            secretNumberRange = 4
            return secretNumberRange
        else:
            secretNumberRange = 9
            return secretNumberRange
    return numberSecret

def numbersGen(number):
       cont = 0
       arr = list()
       while cont <= number-1:
           genNum = random.randrange(1,10)
           arr.append(genNum)
           cont += 1
       return arr
def chanceLister(number):
    chanceList.append(number)
    return chanceList
def chanceValidator(numberList = list(), chanceList = list(), chanceNum = int(), index = int()):
    toque = 0
    fama = 0
    if numberList[index] == chanceList[index] and numberList.count(chanceNum):
        fama+=1
        famaPointsList.append(fama)
    elif numberList.count(chanceNum):
        toque+=1
        toquePointsList.append(toque)
def toquesPoints():
    toquePoints = 0
    for t in toquePointsList:
        toquePoints+=t
    return f'Toques: {toquePoints}'        
def famasPoints():
    famaPoints = 0
    for t in famaPointsList:
        famaPoints+=t
    return f'Famas: {famaPoints}'      


