# Gregory-Leibniz Series (needs a lot of terms to be accurate)

def Gregory_Leibniz():
    pi = 0
    for i in range(1, 1000000000000): #It might be too long to run
        oddnumber = 2 * i - 1
        if oddnumber % 4 == 1:
            pi = pi + 1 / oddnumber
        else:
            pi = pi - 1 / oddnumber

    pi = pi * 4
    print(str(pi))

Gregory_Leibniz()

def Nilakantha_Somayaji():
    pi = 3
    for i in range(1, 10000000000000): #It might be too long to run
        evennumber = 2 * i
        if evennumber % 4 == 2:
            pi = pi + 4 / (i*(i + 1)*(i + 2))
        else:
            pi = pi - 4 / (i*(i + 1)*(i + 2))

    print(str(pi))

Nilakantha_Somayaji()



