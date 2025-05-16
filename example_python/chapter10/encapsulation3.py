#!/usr/bin/python3


class Student:
    def __init__(self, name, age):
        self.__name = name      # private attribute
        self.__age = age        # private attribute
        self.me = 5

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if name:
            self.__name = name
        else:
            print('Name cannot be empty.')

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Age must be positive.')

# Usage
s = Student('Alice', 20)

# Accessing value using getters
print(s.get_name()) # Output: Alice
print(s.get_age()) # Output: 20

# Changing values using setters
s.set_name('Bob')
s.set_age(25)

print(s.get_name()) # Output: Bob
print(s.get_age()) # Output: 25

#Trying to set invalid age
s.set_age(-5) # Output: Age must be positive

print(s.me)
print(s.__name)
