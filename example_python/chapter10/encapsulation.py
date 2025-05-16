#!/usr/bin/python3

class Demo:
    def __init__(self):
        self.public = 'I am public'
        self._protected = 'I am protected'
        self.__private = 'I am private'

    def get_private(self):
        return self.__private

obj = Demo()
print(obj.public)
print(obj._protected)
print(obj.get_private())
