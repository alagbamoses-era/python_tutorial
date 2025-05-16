#!/usr/bin/python3

f = open('writable.txt', 'w')
print(f.writable())
f.close()

f1 = open('writable1.txt', 'r+')
print(f1.writable())
f1.close()
