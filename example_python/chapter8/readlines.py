#!/usr/bin/python3


f = open('song.txt', 'r')

read = ' '.join(f.readlines())

print(read)

f.close()
