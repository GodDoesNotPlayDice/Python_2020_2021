def lines():
     while True:
        try:
            lines = int(input('junk lines: '))
            print('pls wait... junkCode is being generated...')
            if lines <= 0:
                print('the lines have to be greater than zero')
                continue
            else:
                return lines
        except ValueError:
            print('pls use int')

def junk():
    import random, string
    cont = 0
    arrLetters = []
    arrFunc = []
    arrNum = []
    boolArr = []
    while cont < 10000:
        letter = random.choice(string.ascii_letters)
        cont+=1
        arrLetters.append(str(letter))
    while cont < 10010:
        nameFunc = random.choice(string.ascii_letters)
        arrFunc.append(nameFunc)
        cont+=1
    while cont < 20000:
        num = str(random.randint(0,999))
        arrNum.append(num)
        cont+=1
    while cont < 30000:
        tfNum = random.randint(0,10)
        if tfNum % 2 == 0:
            boolArr.append(True)
        else:
            boolArr.append(False)
        cont+=1
    nums = ''.join(arrNum)
    funcNames = ''.join(arrFunc)
    lines = ''.join(arrLetters)
    text = f'''
def {funcNames}():
    '{str(lines)}'
    {eval(nums)}
    {boolArr}

'''
    return text

def JunkLinesGen(lines):
    cont = 0
    file = open('junkPythonCode.py', 'a+')
    while cont < lines:
        file.write(junk() + '\n')
        cont+=1
    print('junked successfully...')