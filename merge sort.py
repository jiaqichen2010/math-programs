import time
import random

def mergesort(listtobesorted):
    if len(listtobesorted) > 1:
        middle = len(listtobesorted) // 2
        A = listtobesorted[:middle]
        B = listtobesorted[middle:]
        
        mergesort(A)
        mergesort(B)
        
        i, j, k = 0, 0, 0
        
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                listtobesorted[k] = A[i]
                i += 1
            else:
                listtobesorted[k] = B[j]
                j += 1
            k += 1
        
        while i < len(A):
            listtobesorted[k] = A[i]
            i += 1
            k += 1
        
        while j < len(B):
            listtobesorted[k] = B[j]
            j += 1
            k += 1

listtobesorted = []
length = int(input("Length of numbers to be sorted: "))

for carrot in range(1, length+1):
    listtobesorted.append(carrot)
    carrot += 1

random.shuffle(listtobesorted)

print("Here are your randomized numbers:\n" + str(listtobesorted))
input("Hit enter to start merge sort\n")

start_time = time.time()
mergesort(listtobesorted)
print(listtobesorted)
print("--- %s seconds ---" % (time.time() - start_time))
