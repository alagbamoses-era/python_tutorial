#!/usr/bin/python3


print(1, 2, 3, 4, 5)
print(1,2,3,4, sep = '*')
print(1,2,3,4, sep = '#', end='&')


print('\n')
name = 'John'
print("1. My name is" + name, end='\n')

print('2. My name is', name)


### default str. format()
name = 'John'
age = 21

print('My name is {} and I am {} years old'.format(name,age))


###### Argument  string formatting 

print('My anme is {0} and I am {1} years old.'.format('John', 21))
print('I am a {1} year old programmer named {0}.'.format('John', 21))

#### keyword method

print('Hello. My name is {name}, and I am a {occupation}.'.format(occupation ='programmer', name = 'John'))





