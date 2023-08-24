# OBJETO
# Son instancias de una clase
# En los metodos se necesita una palabra
# para referirse a la instancia, por eso se usa
# "SELF"
from abc import ABC, abstractmethod


class Dino:
    feathers = True

    def talks(self):
        print("Hello world!")

    def changeFeathers(self):
        self.feathers = not self.feathers


d = Dino()
d2 = Dino()
d2.feathers = False

print(f"Esto es d: {d.feathers}")
print(f"Esto es d2: {d2.feathers}")

d.talks()

d.changeFeathers()
print(f"Esto es d: {d.feathers}")


class Person:
    # METODO CONSTRUCTOR
    # se llama automáticamente cuando se crea una nueva
    # instancia de la clase.
    # Su función principal es inicializar los atributos
    # de la instancia con los valores proporcionados al
    # momento de la creación.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printData(self):
        # se está utilizando una f-string (formatted string literal) abajo
        print(f"Person's name: {self.name} with an age of {self.age}")


p = Person("Pepito", 25)

p.printData()

# ----------------------------------------------------------------
# Herencia de clases


class Toy:
    on = False

    def onOff(self):
        self.on = not self.on

    def isOn(self):
        if self.on == True:
            print("This toy is on")
        else:
            print("This toy is off")


class Maxsteel(Toy):
    def jump(self):
        pass
# MaxSteel hereda las propiedades y metodos de Toy


max = Maxsteel()

# Podemos ahora usar los metodos de Toy, dentro de
# la instancia max de MaxSteel
max.onOff()
max.isOn()
max.onOff()
max.isOn()

# CLASES ABSTRACTAS

# En las primeras lineas se importa ABC (Abstract Base Class)
# from abc, que significa Abstract Base Classes
# junto al decorador abstractmethod que se aplica
# a otra funcion o metodo para modificar su comportamiento
# haciendo de un metodo, un metodo abstracto


class Animal(ABC):
    # Al volver un metodo abstracto
    # el metodo va a tener que ser implementado en
    # la clase que hereda la clase abstracta
    @abstractmethod
    def sound(self):
        pass

    def sayHi(self):
        print("Hi")


class Dog(Animal):
    def sound(self):
        print("guau")


d = Dog()

d.sayHi()
d.sound()


# ----------------------------------------------------------------
# CONECPTO COMPOSICION - Jerarquias de objetos
class Eyes:
    color = "green"


class Tail:
    size = "medium"


class Claws:
    state = "sharp"

    def cutNails(self):
        self.state = "short"


class Appearance:
    tail = Tail()
    eyes = Eyes()
    color = "orange"


class Cat:
    def __init__(self, name):
        self.name = name

    claws = Claws()
    appearance = Appearance()


bob = Cat("Bob")

print(
    f"{bob.name} is {bob.appearance.color}, his eyes are {bob.appearance.eyes.color}, his tail is {bob.appearance.tail.size} size and his claws are {bob.claws.state}")

bob.claws.cutNails()

print(
    f"{bob.name} is {bob.appearance.color}, his eyes are {bob.appearance.eyes.color}, his tail is {bob.appearance.tail.size} size and his claws are {bob.claws.state}")
