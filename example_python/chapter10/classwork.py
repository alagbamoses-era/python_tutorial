#!/usr/bin/python3

class School:
    def school_name(self):
        self.name = str(input('Enter the name of your school: '))
        print('Name of the school is: ', self.name)

class Student(School):
    def level(self):
        print("I'm in 400L")

student1 = Student()
student1.school_name()



