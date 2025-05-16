#!/usr/bin/python3

f = open('fileno.txt', 'w')
fd = f.fileno()
print('File description: ', fd)

f.close()
