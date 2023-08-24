# import pprint as p

# f = open("sampleText.txt", "r")
# f2 = open("sampleText.txt", "r")

# data = f.read()

# datos = f2.readlines()

# f.close()
# f2.close()

# p.pprint(data)

# p.pprint(datos)


def main():
    users = listUsers()
    print(users)

# No solo existe .read() sino tambien
# .readlines() y .readline()


def listUsers():
    f = open("sampleText.txt", "r")
    data = f.readlines()
    f.close()

    for line in data:
        print(line)


if __name__ == "__main__":
    main()
