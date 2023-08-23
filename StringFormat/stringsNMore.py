# -----------------------------------------------------------------
# The bad way, old one, b4 python 2.6

num = 123
text = "Hello world"
floatNum = 1.2356789
state = True

print("The number is %d, the text is %s, the float is %f and the state is %s" % (num, text, floatNum, state))
print("The float value is %f" % floatNum)
print("The float value with 2 decimals is %.2f" % floatNum)

# The .format() one, until python 3.6

print("With .format: The number is {}, the text is {}, the float is {} and the state is {}"
      .format(num, text, floatNum, state))

print("With vars: The number is {num}, the text is {txt}, the float is {flt} and the state is {stt}"
      .format(num=num, txt=text, flt=floatNum, stt=state))


# LA MODERNA - con f string
print(f"With f string: The number is {num}, the text is {text}, the float is {floatNum} and the state is {state}")

#Con f string podemos manipular las variables ya como texto:
print(f"With f string: The text is {text.replace('o','a')}")

class Toy:
    name = ""
    year = 0

    def __init__(self,name,year):
        self.name = name
        self.year = year
    
    def __str__(self):
        return f"Mi name is {self.name}, I'm from {self.year}"
    
bionicle = Toy("Bionicle", 2010)
print(str(bionicle))


import pprint as p

p.pprint(dir(""))

