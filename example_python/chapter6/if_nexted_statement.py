#!/usr/bin/python3


number = float(input('Enter a number to evaluate: '))

if number >= 0:
    if number == 0:
        print(number, 'is a zero')
    else:
        print(number, 'is a positive number')
else:
    print(number, 'is a negative number')


