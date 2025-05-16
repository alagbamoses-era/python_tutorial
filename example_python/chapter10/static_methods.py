#!/usr/bin/python3

class Math:
    
    @staticmethod # decorator (method that don't depend on instance or class)
    def add(a, b):
        return a + b

sum_ = Math.add(2, 5)
print(sum_)


