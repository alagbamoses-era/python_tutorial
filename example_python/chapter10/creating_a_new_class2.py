#!/usr/bin/python3


class NewClass:
    '''This is our first class. What is doea is display a string
    text and a value of variable name'''
    
    def __init__(self):
        self.name = str(input('Enter your name: '))

    def greeting(self): # self is a reference
        print('Hello ', self.name)

MyObject = NewClass()

print(MyObject.greeting())
print(NewClass.__doc__)



