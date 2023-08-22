# FUNCIONES

def printName(name):
    print("Hi, ",name)

printName("Federico")

printName("Laura")

def sum(a,b):
    print(a + b)

sum(1,2) 


# Se pueden identar funciones pero no se usa mucho
def math(a,b):

    def sum(a,b):
        print(a+b)
    
    def sustract(a,b):
        print(a-b)
    
    sum(a,b)

    sustract(a,b)

math(5,3)

# Se puede cambiar el valor de una
# variable global con la palabra reservada "global"
# seguido del nombre de la variable a modificar
smthg = "Hello World!"
def testPrint():
    global smthg
    smthg = "Hello World Changed!"
    print(smthg)

testPrint()
print(smthg)


# Se le pueden dar argumentos por defecto
# a las funciones, haciendo el argumento opcional
def printWeather(weather="Cloudy"):
    print(weather)

printWeather()
printWeather("Sunny")

# Si son varios parametros puede pasarse 
# al invocar exacatamente a cual se refiere
# no tienen que seguir el mismo orden
def aSum(a=2,b=2,c=2):
    print(a+b+c)

aSum(b=5,c=1,a=1)

# PARAMETROS VARIABLES 

# En esta funcion se genera una tupla
def uncertainSum(*args):
    result = 0

    for arg in args:
        result += arg
    
    print(result) 

uncertainSum(1,2,3,4,5)

def kwargsFunction(**kwargs):
    print(kwargs)

kwargsFunction(house=1,dog=2, car="Volvo")


# Operador ternario de Python
# La comprobacion de la existencia de algo se pone en el medio
# Al comienzo el valor deseado si se tiene 
# Al final el valor por default, el else si es false la comprobacion
def rangeSum(**kwargs):
    initial = kwargs['initial'] if 'initial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else initial

    result = 0
    for x in range(initial, final + 1):
        result += x
    
    return result

print("Esto es rangeSum: " + str(rangeSum(initial=2,final=5)))

# FUNCION ANONIMA ----- LAMBDA

anon = lambda: print("Hello World!")
anon()

# Con argumentos/parametros
anon2 = lambda arg1, arg2: print("hello,", arg1, "adios,", arg2)
anon2("Pepe","Juana")

# No necesitan return si la funcion es simple
anon3 = lambda x: x+x
print(anon3(5))