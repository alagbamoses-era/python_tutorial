#!/usr/bin/python3

# Multiple inheritance refers to a scenario where a 
# class can inherit from more than one parent class.
# This allows the child class to inherit methods and
# attributes from multiple parent classes.

class School:
    def lib(self):
        print('Library')

class City:
    def police_station(self):
        print('Police Station')

class Hotel:
    def enjoy(self):
        print('It is time for fun!')

class Holiday:
    def away(self):
        print('Students are on holiday')

class Student(School, City, Holiday, Hotel):
    def student_crime(self):
        print('Student comes crime')

student = Student()
student.lib()
student.police_station()
student.student_crime()
student.away()
student.enjoy()

