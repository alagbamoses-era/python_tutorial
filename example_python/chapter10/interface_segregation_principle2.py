#!/usr/bin/python3

from abc import ABC, abstractmethod
import random

class Animal(ABC):

    @abstractmethod # it enforces segregation logic
    def segregation(self):
        pass

class Goat(Animal):

    def __init__(self, food):
        self.food = food

    def segregation(self):
        return Goat(self.food)

    def __repr__(self):
        return self.food

class Dog(Animal):
    def __init__(self, food):
        self.food = food

    def segregation(self):
        return Dog(self.food)

    def __repr__(self):
        return self.food

class Owner:
    def __init__(self, animal1: Animal, animal2: Animal):
        self.animals = [animal1, animal2]

    def care(self):

        segregate_animal = random.choice(self.animals).segregation()
        return segregate_animal


if __name__ == '__main__':
    goat = Goat('grass')
    dog = Dog('bone')
    owner = Owner(goat, dog)

    num_generate = 1000
    generate = [owner.care() for _ in range(num_generate)]

    count_goat = sum(1 for g in generate if g.food == 'grass' )
    count_dog = sum(1 for d in generate if d.food == 'bone')

    print(f"goat {goat} : {count_goat}")
    print(f"dog {dog} : {count_dog}")
    

    



