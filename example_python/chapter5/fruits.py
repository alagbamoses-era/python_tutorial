#!/usr/bin/python3

print('This information is about different types of fruit')


fruits = ('orange', 'pawpaw', 'apple', 'strawberry', 'gauva', \
        'banana',)

fruits = list(fruits)

print('These are diffrent types of fruits available in this store',\
        '\n '.join(fruits))


fruits2 = ['carrot', 'eggplant']

fruits.extend(fruits2)

print(fruits)
