#!/usr/bin/python3


x, y, z = 5.7, 10, '3.5j'

print(x, 'is of type', type(x), y, 'is of type', type(y), 'and', z, 'is a', type(z))


x = int(x); y = float(y); z = complex(z)

print("After coercion, x new value is ", x, ", y's new value is", y, "and z is of type", type(z))


