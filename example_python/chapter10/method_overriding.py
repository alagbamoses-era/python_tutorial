#!/usr/bin/python3

# Single inheriance means a child class inherit from one parent class only
class Parent:
    def speak(self):
        print('Animal speaks')


class Child(Animal):
    def talk(self):
        print('Dog barks')


dog = Child()
dog.speak()
dog.talk()




