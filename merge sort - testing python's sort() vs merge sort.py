import time
import random

listtobesorted = []
length = int(input("Length of list to be sorted: "))

for carrot in range(1, length+1):
    listtobesorted.append(carrot)
    carrot += 1

random.shuffle(listtobesorted)

print("Here is your randomized list:\n" + str(listtobesorted))
input("Hit enter to start normal python sort\n")

start_time = time.time()
listtobesorted.sort()
print(listtobesorted)
print("--- %s seconds ---" % (time.time() - start_time))
