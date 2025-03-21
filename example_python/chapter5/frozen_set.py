#!/usr/bin/python3

fs_1 = frozenset([1, 2, 3, 4])
fs_2 = frozenset([1, 2, 5, 6])

## adding elements (Union)
# fs_1.add(fs_2)  this will thros error

print(fs_1.union(fs_2))  # to print all elements in set fs_1 and fs-2

### intersection 

print(fs_1.intersection(fs_2))


## Difference
print(fs_1.difference(fs_2))

## Symmentric difference

print(fs_1.symmetric_difference(fs_2))

