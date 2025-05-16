#!/usr/bin/python3


def studentinfo(name, gender ='Male'):
    '''This function prints info passed in the
    function parameters.'''
    print('Name: ', name)
    print('Gender: ', gender)
    return;

studentinfo(name = 'John')

studentinfo(name = 'Mary', gender = 'Female')


