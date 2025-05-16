#!/usr/bin/python3


class Dog:
    def speak(self):
        return 'woof'

class Cat:
    def speak(self):
        return 'meow'

class AnimalFactory:
    def get_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            return None

#animal = AnimalFactory.get_animal('dog')

ani = input('Which of these pets do you liks? cat or dog: ')


animal = AnimalFactory.get_animal(ani)
print(animal.speak())


