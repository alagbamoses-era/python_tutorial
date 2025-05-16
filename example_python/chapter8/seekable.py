#!/usr/bin/python3 

import sys
from io import BytesIO, StringIO

with open('seekable.txt', 'w') as f:
    print(f.seekable())


print(sys.stdin.seekable())

## Seekable works with 
# io.StringIO
# io.BytesIO


data = BytesIO(b'Hello Moses')
print(data.seekable())


data2 = StringIO('Hello Moses')
print(data2.seekable())


string_ = 'Hello John'
#print(string_.seekable()) ### it does not support seekable()

