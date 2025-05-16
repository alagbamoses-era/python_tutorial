#!/usr/bin/python3


import pwinput

def password():
    password = 'admin123'
    pw = pwinput.pwinput(prompt = 'Enter Password: ', mask='*')
    if (pw == password):
        save_file()

def save_file():
    file = open('save.txt', 'w+')
    file.write('Hello Moses')


