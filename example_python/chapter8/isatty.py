#!/usr/bin/python3

#### anything related to tty is for terminal

import sys

if sys.stdout.isatty():
    print('Output is going to the terminal')
else:
    print('Output is redirected')


with open('isatty.txt', 'w') as f:
    if f.isatty():
        print('This will not be true since it is a file')
    else:
        print('Output is redirected to a file')

