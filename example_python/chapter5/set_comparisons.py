#!/usr/bin/python3


x = set([1, 2])
y = set([1, 2, 3, 4])

print(x < y)
print(x.issubset(y))
print(y > x)
print(y.issuperset(x))


print(x != y)
print(x == y)




### set comprehension

squared = {x ** 2 for x in range(5)}
print(squared)


