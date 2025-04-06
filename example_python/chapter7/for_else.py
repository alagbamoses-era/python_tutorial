#!/usr/bin/python3

# For syntax 
# for variable in squence

# for: the for loop in python iterate over a sequence such: 
# list, tuple, string, range, dictionary and set

# variable: variable in a for loop is a placeholder that holds the current 
# elements of the sequence during each iteration.

# sequence: sequence are iterable object like list, tuple, string, or range, 
# dictionary, set

# The loop runs once for each element in the sequence

# Iteration over a list using for loop
numbers = [0, 1, 3, 5, 6, 9, 10]

for i in numbers:
    print(i)
else:
    print('No more numbers to print.')

# Iteration over a tuple using for loop

animals = ('goat', 'dog', 'cow', 'hen',)

for i in animals:
    print(i)
else:
    print('This is not an animal')

# Itiration over a string

greet = 'This', 'is', 'a', 'dog'

for i in greet:
    print(i)
else:
    print('This is a cat')

# Iteration over a range

for i in range(1, 20, 2):
    print(i)

else:
    print('Not included')


# Iteration over a dictionary

dict_ = {'name':'moses', 'occupation': 'programmer', 'gender':'male'}

for k, v in  dict_.items():
    print(k,':',v)
else:
    print('Not included')

# Iteration over a set

set_ = set(['goat', 'dog', 'cow'])

for i in set_:
    print(i)
else:
    print('none')


