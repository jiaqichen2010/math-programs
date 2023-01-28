print("This is temperature converter. You may convert a temperature from celsius to fahrenheit or from fahrenheit to celsius.")

def c_to_f():
  c = input("Enter temperature in celsius: ")
  f = 1.8 * float(c) + 32
  if f % 1 == 0:
    print("The temperature in fahrenheit is " + str(int(f)) + "°F")
  else:
    print("The temperature in fahrenheit is " + str(float(f)) + "°F")

def f_to_c():
  f = input("Enter temperature in fahrenheit: ")
  c = (float(f) - 32) * 5 / 9
  if c % 1 == 0:
    print("The temperature in celsius is " + str(int(c)) + "°C.")
  else:
    print("The temperature in celsius is " + str(float(c)) + "°C.")

def convert():
  mode = input("Enter mode (fahrenheit or celsius) to convert: ")
  if mode.upper() == "FAHRENHEIT" or mode.upper() == "F":
    f_to_c()
  elif mode.upper() == "CELSIUS" or mode.upper() == "C":
    c_to_f()
  elif mode.upper() == "FARENHEIT":
    didyoumean = input("Did you mean fahrenheit? (Yes/No) ")
    if didyoumean.upper() == "YES":
      f_to_c()
    else:
      print("Sorry, then.")
  elif mode.upper() == "CELCIUS" or mode.upper() == "CELSIOUS" or mode.upper() == "CELCIOUS":
    didyoumean = input("Did you mean celsius? (Yes/No) ")
    if didyoumean.upper() == "YES":
      c_to_f()
    else:
      print("Sorry, then.")
  else:
    print("Invalid input.")
  print("\n")

while True:
  convert()
