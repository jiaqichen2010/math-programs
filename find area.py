# This program asks you what shape you want to find the area for and finds the area of it.

import math

def findarea():
    mode = input("What do you want to find the area for?\nYou may choose circle, triangle, ellipse (or oval), square or rectangle. ")
    if mode.upper() == "CIRCLE":
        radius = input("What's the radius? ")
        areacircle = float(radius) * float(radius) * math.pi
        # Checking if it is an integer
        if float(areacircle) % 1 == 0:
          print('The area of the circle is ' + str(int(areacircle)) + '!')
        else:
          print('The area of the circle is ' + str(float(areacircle)) + '!')
    elif mode.upper() == "TRIANGLE":
        base = input("What's the base? ")
        height = input("What's the height? ")
        areatriangle = float(base) * float(height) * 0.5
        if float(areatriangle) % 1 == 0:
          print('The area of the triangle is ' + str(int(areatriangle)) + '!')
        else:
          print('The area of the triangle is ' + str(float(areatriangle)) + '!')
    elif mode.upper() == "ELLIPSE" or mode.upper() == "OVAL":
        longradius = input("What's the longest radius? ")
        shortradius = input("What's the shortest radius? ")
        if float(longradius) >= float(shortradius):
            areaellipse = float(longradius) * float(shortradius) * math.pi
            if float(areaellipse) % 1 == 0:
              print('The area of the ellipse (or oval) is ' + str(int(areaellipse)) + '!')
            else:
              print('The area of the ellipse (or oval) is ' + str(float(areaellipse)) + '!')
        else:
            print("Error: longest radius is shorter than shortest radius.")
    elif mode.upper() == "SQUARE":
        length = input("What's the length? ")
        areasquare = float(length) * float (length)
        if float(areasquare) % 1 == 0:
          print('The area of the square is ' + str(int(areasquare)) + '!')
        else:
          print('The area of the square is ' + str(float(areasquare)) + '!')
    elif mode.upper() == "RECTANGLE":
        length2 = input("What's the length? ")
        breadth = input("What's the breadth? ")
        arearectangle = float(length2) * float(breadth)
        if float(arearectangle) % 1 == 0:
          print('The area of the rectangle is ' + str(int(arearectangle)) + '!')
        else:
          print('The area of the rectangle is ' + str(float(arearectangle)) + '!')
    else:
        print("Invalid input.")
    print("\n")
    

while True:
    findarea()
