#!/usr/bin/python3

import sys

class NoSlots:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class WithSlots:
    __slots__ = ['a', 'b']
    def __init__(self, a, b):
        self.a = a
        self.b = b

print(sys.getsizeof(NoSlots(1, 2))) # e.g 56 bytes (plus __dict__)
print(sys.getsizeof(WithSlots(1, 2))) # e.g 40 bytes 
