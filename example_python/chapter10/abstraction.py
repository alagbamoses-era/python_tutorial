#!/usr/bin/python3


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return 'Bark'

d = Dog()
print(d.make_sound())


