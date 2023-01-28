#Binary generator
#Run in fullscreen for best effect

from random import randrange
import time

def printbinary():
    binarystring = ''
    for number in range(1, 154):
        binarynumber = randrange(2)
        binarystring += str(binarynumber)
        number += 1
    print(binarystring)
    time.sleep(0.03)

while True:
    printbinary()
