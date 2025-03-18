#!/usr/bin/python3

def msb_value_bitwise(n):
    if n == 0:
        return 0
    msb = 1
    while n > 1:
        n >>= 1
        msb <<= 1
    return msb

x = 5
y = 3

# Bitwise AND
result = x & y
print(result)
print(10 & 9)

# Bitwise OR
print(6 | 7)


# Bitwise NOT
a = 5
b = ~a
print(b)

a = 8
b = ~a
print(b) # the result is always negative


n = 5 
print(msb_value_bitwise(n))


# Bitwise XOR (Exclusive OR)
print(10 ^ 11)


# Bitwise right shift
a = 20
b = 2
c = a >> b
print(c)


a = 100
b = 7
c = a >> b
print(c)

## Bitwise left shift
a = 10
b = 7
c = a << b
print(c)



