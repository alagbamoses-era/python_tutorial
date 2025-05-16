#!/usr/bin/python3

from simplecrypt import encrypt

message = 'Hello World'
password = 'greetings'

ciphertext = encrypt(password, message)

print('encrypted: ', ciphertext)
