#!/usr/bin/python3


f = open('flush.txt', 'w+')
f.write('This is flush\n')
f.flush() ### flush write to disk

f.close()
