#!/usr/bin/python3

class Cat:
    def speak(self):
        #print('Meow')
        self.kitten = 'meow'
        return self.kitten

class Dog:
    def speak(self):
        return 'Bark'

def do_something(val):
    print(val.speak())

cat = Cat()
dog = Dog()

#print(cat.speak())
do_something(cat)
do_something(dog)



