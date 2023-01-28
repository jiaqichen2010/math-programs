import random

listtobesorted = []
length = int(input("Length of list to be sorted: "))

for carrot in range(1, length+1):
    listtobesorted.append(carrot)
    carrot += 1

random.shuffle(listtobesorted)

print(listtobesorted)
