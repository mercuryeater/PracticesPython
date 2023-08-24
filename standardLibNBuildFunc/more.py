from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# FILTER


def isFive(x):
    if x == 5:
        return True

    return False


filtered = filter(isFive, numbers)
print(list(filtered))

#
# MAP
#


def square(x):
    return x * x


mapped = map(square, numbers)
print(list(mapped))

#
# REDUCE
#


def sum(a, b):
    return a + b


reduced = reduce(sum, numbers)
print(reduced)

#
# ZIP
#
courses = ['Javascript', 'Python', 'Git']
assistants = [15, 20, 18]

demo = zip(courses, assistants)
print(list(demo))

#
# INPUT
#

name = input('Name please:')
print(f'Thanks for the information, {name}')


secretValue = 38

value = 0

while value != secretValue:
    value = int(input('Guess the integer number:'))

    if value > secretValue:
        print('Too high')
    elif value < secretValue:
        print('Too low')
    else:
        print('You guessed!')
