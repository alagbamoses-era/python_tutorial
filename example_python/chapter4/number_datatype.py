#!/usr/bin/python3


x = 7
print(x, 'is of type', type(x))

y = 7.0
print(y, 'is of type', type(y))

z = 1 + 2j
print('is', z, 'a complex number?', isinstance(1 + 2j, complex))

print(isinstance(x, int))
print(isinstance(y, float))


a = 5; b = 5.0; c = 2 + 3j
print(a); print(b); print(c)

del b, a, z


print(a); print(z); print(b)

