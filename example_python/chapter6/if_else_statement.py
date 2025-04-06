#!/usr/bin/python3


x, y = 12, 12
if (x == y):
    print('x is equal to y')
else:
    print('x is not equal to y')

a, b = 4, 8
if (a == b):
    print('a is equal to b')
else:
    print('a is not equal to b')

### membership operator

s = 'Hello Moses'
if ('H' in s):
    print('H is a member')
    print('H' in s)
else:
    print('H is not a member')
    print('H' is not s)

if ('M' not in s):
    print('M is not a member')
else:
    print('M is  member')

## identity operator
p = s

if (p is s):
    print('Both are the same')
    print(p is s)
else:
    print('they are different')


l = [1, 'h', 1.0, 1+2j]

a, b, c, d = 1, 2, 3, 4
if ((a <= b or a >= b) and ((b == c and b != c) or (c < d and c > d))):
    print('if body')
else:
    print('else body')


