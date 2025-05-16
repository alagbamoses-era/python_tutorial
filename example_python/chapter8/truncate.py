#!/usr/bin/python3

list_ = [1, 2, 3, 4, 5]

with open('truncate.txt', 'w+') as f:
    f.write('Hello Moses')
    f.truncate(5)

truncated = list_[0:3]
print(truncated)

string = 'Hello Moses'
trunc = string[3:6]
print(trunc)

