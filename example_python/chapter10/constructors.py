#!/usr/bin/python3

class ComplexNumbers:
    def __init__(self, x=0, y=0):
        self.real = x   # instance variable of a class
        self.imagined = y

    def getNumbers(self):
        print('Complex numbers are: {0} + {1}'.format(self.real, \
                self.imagined))

object1 = ComplexNumbers(2, 3) # creates a new ComplexNumbers object
object1.getNumbers() # calls getNumbers() function

object2 = ComplexNumbers(10) # creates another ComplexNumbers object
object2.attr = 20 # creates a new attributes 'attr'

print((object2.real, object2.imagined, object2.attr))

object1.abc = 12

print((object1.real, object1.imagined, object1.abc))

#object1.attr # Generates an error because c1 object doesn't have 
             # attribute 'attr'

