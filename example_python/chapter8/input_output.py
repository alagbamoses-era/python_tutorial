#!/usr/bin/python3


name = str(input('Enter your name: '))

age = int(input('How old are you?: '))

sex = str(input('Enter your gender M of F: ')).lower()

location = str(input('Which city do you live in: '))

if sex == 'm':
    gender = 'male'
elif sex == 'f':
    gender = 'female'
else:
    gender = 'invalid'


print('{}, you are a {} old {} from {}.'.format(name, age, gender, location))



