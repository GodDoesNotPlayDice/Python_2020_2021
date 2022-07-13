from random import randint
import string as sttr
n = int(input('codes numbers: '))
file = open('Steam Gift.txt','a+')
cont = 0
letters = []
numbers = []
for i in sttr.ascii_uppercase:
    letters.append(i)
for i in sttr.digits:
    numbers.append(i)
def codeGen():
    rep = 0
    code = []
    while rep < 5:
        if randint(1,1000) % 2 == 0:
            code.append(letters[randint(0,25)])
            rep+=1
        elif randint(1,1000):
            code.append(numbers[randint(0,9)])
            rep+=1
        else:
            pass
    return code
while cont < n:
    file.write(f"{''.join(codeGen())}-{''.join(codeGen())}-{''.join(codeGen())}\n")
    cont+=1 


