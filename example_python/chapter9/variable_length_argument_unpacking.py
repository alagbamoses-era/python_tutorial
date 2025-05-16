#!/usr/bin/python3


def studentinfo(name, age, height):
    print(f'Name: {name} \nAge: {age}')

args = ('Moses', '21', '30')
studentinfo(*args)

kwargs = {'name':'Moses', 'age':'21', 'height':'30'}
studentinfo(**kwargs)



