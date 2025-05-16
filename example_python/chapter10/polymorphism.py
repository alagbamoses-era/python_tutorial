#!/usr/bin/python3


class Cat:
    def speak(self):
        return 'Meow'

class Dog:
    def speak(self):
        return 'Bark'

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak()) # Each calls its own speak()
