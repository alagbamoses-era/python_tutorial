#!/usr/bin/python3


def studentinfo(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

studentinfo(name='Moses', age=21)

