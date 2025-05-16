#!/usr/bin/python3


class Point:
    __slots__ = ['x', 'y', 'z'] # reserve space for special attributes


    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Point(1, 2, 5)
print(p.x, p.y, p.z)




