#!/usr/bin/python3

class NewClass:
    '''This is our first class. What it does is display a string
    text and a value of variable name'''
    
    def __init__(self):
        self.name = str(input('Enter your name: '))

    def greeting(self):
        print('Hello ', self.name)

MyObject = NewClass()

# Creating a new NewClass object
print(MyObject.greeting())
# MyObject.greeting() # calling function greeting()


