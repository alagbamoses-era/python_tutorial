#!/usr/bin/python3 


def multiply(*args):
    result = 1
    for num in args:
        result = result * num # result *= num
    return result


product = multiply(2, 3, 4, 5)
print(product)

