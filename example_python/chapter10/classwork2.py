#!/usr/bin/python3 

####  SINGLE INHERITANCE: ONLY INHERIT FROM ONE PARENT

# Parent class
class Person:
    def __init__(self):
        self.full_name = str(input("Enter student's full name: "))

# Child class inheriting from parent
class Student(Person):

    def save_file(self):
        with open('student.txt', 'a+') as f:
            f.write(self.full_name + '\n')
        print(f"Student name: {self.full_name}")
        print('Save successfully')

student = Student()
student.save_file()


