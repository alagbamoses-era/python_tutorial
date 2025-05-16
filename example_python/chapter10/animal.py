#!/usr/bin/python3

import sys

### Monogamy single inheritance

class Animal: # parent
    def __init__(self, name):
        self.name = name
       

class Cat(Animal): # child

    def meow(self):
        print(f'{self.name} sounds meow')

class Dog(Animal):

    def bark(self):
        print(f'{self.name} barks')

class Duck(Animal):

    def quack(self):
        print(f'{self.name} sounds quack')


def cat_sound(obj: Animal):
    obj.meow()

def dog_sound(obj: Animal):
    obj.bark()

def duck_sound(obj: Animal):
    obj.quack()
    
if __name__ == '__main__':
    var = str(input('Enter cat, dog or duck: '))
    
    cat = Cat(var)
    dog = Dog(var)
    duck = Duck(var)

    if var == 'cat':
        cat_sound(cat)
    elif var == 'dog':
        dog_sound(dog)
    elif var == 'duck':
        duck_sound(duck)
    else:
        print('Invalid input')
        sys.exit()



