#!/usr/bin/python3


text = input('Enter number in words: ')
with open('text.txt', 'w+') as f:
    f.write(text)
    print('Current file position', f.tell()) 

