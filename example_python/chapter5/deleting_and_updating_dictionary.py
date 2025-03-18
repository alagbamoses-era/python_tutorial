#!/usr/bin/python3

student = {'name':'John', 'age':25, 'grade':'B+'}
print('Before update: ', student)
print('\nchange age to 30:\nAdd:value pair')

student['age'] = 30
student['sex'] = 'Male'

print('\nAfter update: ', student)
print('\nDelete grade entry: ')

del student['grade']

print('After deleting grade: ', student)
