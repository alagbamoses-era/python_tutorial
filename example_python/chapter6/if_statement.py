#!/usr/bin/python3


x = 10
y = 20

if ((x == 10 or y == 30) and (y == 20 or x == 50)):
    print('x = 10')


## membership operator
x_1 = 'Hello Moses'
if ('Moses' in x_1):
    print(x_1)

### comparison operator
if (x < y):
    print(' 10 is less than 20')


if (y > x):
    print('20 is greater than 10')

numbers = [1, 2, 5, 7, 'Apple', 'corn']

if (1 in numbers):
    print('1 is a member')

if (1 in numbers) and ('Apple' in numbers):
    print('Both 1 and Apple are members')

n = [1, 5.0, 2+5j, 'Apple']

if (((1 in n) and (5.0 in n)) and (((2+5j) in n)) and ('Apple' in n)):
    print('All are members')

# identity operator

num_1 = [1, 2, 3, 4]
num_2 = num_1

if (num_1 is num_2):
    print('they are identical')
    print(num_1 is num_2)


if (num_1 is not num_2):
    print(num_1 is not num_2)

print('they are identical')


if (5 not in num_1):
    print('5 is not a member')
    print(5 not in num_1)

## using bitwise operator
### NOTE: DO NOT USE BITWISE OPERATORS FOR IF STATEMENT
             





