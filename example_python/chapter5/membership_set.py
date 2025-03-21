#!/usr/bin/python3

#### Checking membership

s = set([1, 2, 3, 4])

print(3 in s)
print(5 in s)


set_t = set([1, 2, 3])
set_p = set([3, 4, 5])

### Union of set

print(set_t | set_p)
print(set_t.union(set_p))


### Intersection of set

print(set_t & set_p)

print(set_t.intersection(set_p))


## Difference : elements in A but not in B

print(set_t - set_p)
print(set_t.difference(set_p))

### Symmetric Difference (^ or symmetric_difference())

# elements that are in one set but not both

print(set_t ^ set_p)
print(set_t.symmetric_difference(set_p))




