#!/usr/bin/python3

def studentinfo(x, *args, **kwargs):
    print(f'X : {x} \nPositional: {args} \nKeyword: {kwargs}')


studentinfo(1, 2, 3, name='Moses', age=21)



