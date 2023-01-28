import time
import webbrowser

greeting = input("Welcome to the 3x + 1 (or Collatz Conjecture) number generator.\nFor a start, do you know what is the Collatz Conjecture? (Yes/No) ")
if greeting.upper() == "YES":
    print("Great! Let's continue!")
elif greeting.upper() == "NO":
    webbrowser.open("https://en.wikipedia.org/wiki/Collatz_conjecture")
    time.sleep(3)
    print("Have you understood? Let's continue!")
else:
    print("Invalid input. Sorry!")
x = int(input("Enter the starting number: "))
delay = input("Enter the delay time between numbers (in seconds): ")
highestnumber = 0
runtime = 0
highestnumbertime = 0

print(str(x))
while x != 1:
    if x > highestnumber:
        highestnumber = x
        highestnumbertime = runtime
    if x % 2 == 0:
        x = x / 2
    else:
        x = 3 * x + 1
    print(str(int(x)))
    runtime += 1
    time.sleep(float(delay))

print("The highest number was " + str(int(highestnumber)) + ". It was reached at number " + str(int(highestnumbertime) + 1) + ".")
print(str(int(runtime) + 1) + " numbers were generated until the number reached 1, including 1.")
