#!/usr/bin/python3

class Engine:
    def _start(self):
        print("Engine started")
    
    def belt_size(self):
        self.__size = 800
        return self.__size 

class Car:
    def __init__(self):
        self.engine = Engine()

    def move(self):
        self.engine._start() # this does not work for private method
    
    def print_size(self):
        self.engine = Engine()
        print(self.engine.belt_size())



car = Car()
car.move()
car.print_size()




