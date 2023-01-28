import random

def generatebinary(length):
    binarystring = ''

    for i in range (1, length, 1):
        x = random.randrange(0,2)
        binarystring += str(x)

    print(binarystring)

for i in range (1, 20, 1):
    generatebinary(961)
