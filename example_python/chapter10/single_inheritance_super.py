#!/usr/bin/python3

class Parent:
    def __init__(self):
        print('Parent init')
    
    def greetings(self):
        print('Hello')

class Child(Parent):
    def __init__(self):
        super().greetings()
        print('Child init')

child = Child()
child.greetings()
