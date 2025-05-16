#!/usr/bin/python3


class Shape: # Base inheritance
    def area(self):
        raise NotImplementedError('Subclasses must implement')


class Circle(Shape): 
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(7)
print(circle.area())

shape = Shape()
print(shape.area())
