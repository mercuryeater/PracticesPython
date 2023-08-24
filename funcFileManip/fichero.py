import pickle
f = open('miFichero.txt', 'a')

f.write("datos\n")
f.write("datosDOS\n")
f.close()

a = open('anotherFile.txt', 'a')
list = [
    'fisrt line',
    'second line',
    'third line',
]
jumpList = []

for item in list:
    item += '\n'
    jumpList.append(item)

a.writelines(jumpList)
a.close()


def escribe(file, data):
    f = open(file, 'w')

    for line in data:
        if not line.endswith('\n'):
            line += '\n'
        f.write(line)
        # line.append('\n')


escribe('aanotherFile', list)


# MODULO PICKLE
# Serializar y des-serializar


class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def tellData(self):
        print(f'My name is {self.name} and my price is {self.price}')


# bear = Toy('Bear', 10)
# c = open('datos.bin', 'wb')  # write - binary data
# pickle.dump(bear, c)
# c.close()
# Creé el objeto Juguete y como comenté la instancia,
# está eliminado, pero quedó en el .bin que se lee así:

d = open('datos.bin', 'rb')
loadedBear = pickle.load(d)
d.close()

# Y entonces puede leerse nuevamente
print(type(loadedBear))
print(loadedBear.tellData())
