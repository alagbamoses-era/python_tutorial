#!/usr/bin/python3


from cryptography.fernet import Fernet
import os


def encrypt_file():
    path = '/modules'
    os.chdir(path)

    password = input('Enter your password: ')
    password = password.encode()
    key = Fernet.generate_key()
    file_name = input('Enter full file name: ')

    with open(file_name, 'rb') as file:
        encrypted_content = Fernet(key).encrypt(file.read())

    with open('encrypted_' + file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content)

    print('File has been encrypted')

encrypt_file()
