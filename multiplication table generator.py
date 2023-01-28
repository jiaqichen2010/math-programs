# Generates multiplication tables for given number up to highest multiple (as inputted).

number = input("What number do you want to generate multiplication tables for? ")

upperlimit = input("What multiple do you want to generate up to? ")

othernumber = 1

for othernumber in range(1, int(upperlimit) + 1):
  print(number + ' × ' + str(othernumber) + ' = ' + str(int(number) * othernumber))
