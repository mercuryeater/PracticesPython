a = 5
b = 10
c = 12


# IF - ELIF - ELSE
if a < 10:
    print("A is less than B")


if b == c:
    print("B is equal to C")


if a < b and c > b:
    print("A is less than B and C is more than B")

if a > b or b == 10:
    print("Some condition was asserted")

if a == b:
    print("A is equal to B")
elif a != b:
    print("A is different from B")

if a == b:
    print("A is equal to B")
elif a == 12:
    print("A is equal to 12")
else:
    print("Nothing meets the condition")


# ----------------------------------------------------------------
# CONDICIONAL WHILE
while b < c:
    print("B is " , b) 
    b += 1
    

if b == c:
    print("B is the same as C")


count = 0

while count <= 10:
    if count % 2 == 0:
        print(count, "is an even number")
    else:
        print(count, "is and odd number")
    
    count += 1


# -------------------------------------------------------------------
# LOOP FOR

list = [1,2,3,4,5]
longitude = len(list)
print("list has " , longitude , "items")

for number in range(longitude):
    print("Value in list is " , number, " : " , list[number])

for  currentValue in list:
    if currentValue == 3:
        print("list contains a 3")
        continue
    print(currentValue)

tuple = (1,2,3,4,5)
for  currentValue in tuple:
    if currentValue == 3:
        print("tuple contains a 3")
        continue
    print(currentValue)

for number in range(5,11):
    print("The numbers in this range are", number)

# Hay un "else para los for loop pero rara vez se utiliza"


# ------------------------------------------------------------
# in y not in 

secondList = ["hola","mundo","como","vamos"]

if "mundo" in secondList:
    print("The word mundo is in secondList")

if "comer" not in secondList:
    print("The word comer is not in secondList")


# ------------------------------------------------------------
# sort 

numbersList = [6,3,1,7,2,4,5]
lettersList = ["Z","c","z","C","a","P","A","p"]

# Esto se basa en el codigo ASCI
orderedLetterList = sorted(lettersList)
print(orderedLetterList)

orderedNumbersList = sorted(numbersList)
print(orderedNumbersList)



# ------------------------------------------------------------
#  SWITCH 

value = 5

match value:
    case 1:
        print("value is 1")
    case 5:
        print("value is 5")