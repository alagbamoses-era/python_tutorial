#!/usr/bin/python3


class NewClass:
    '''This is our first class. What is doea is display a string
    text and a value of variable name'''

    name = str(input('Enter your name: '))

    def greeting(name):
        print('Hello ', name)

print(NewClass.name)
print(NewClass.greeting)
print(NewClass.__doc__)



