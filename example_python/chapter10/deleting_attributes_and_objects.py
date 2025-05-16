#!/usr/bin/python3


class ComplexNumbers:
    def __init__(self, x=0, y=0):
        self.real = x
        self.imagined = y

    def getNumbers(self):
        print('Complex numbers are: {0} + {1}'.format(self.real, \
                self.imagined))

object1 = ComplexNumbers(2, 3)# creates a new ComplexNumbers object
object1.getNumbers() # calls getNumbers() function

object2 = ComplexNumbers(10) # creates another ComplexNumbers object
object2.attr = 20 # creates a new attribute 'attr'

print(object2.real, object2.imagined, object2.attr)

del ComplexNumbers.getNumbers

object1.getNumbers()



