#!/usr/bin/python3


class School:

    def library(self):
        print('School Library')

    def sport_complex(self):
        print('School sport complex')

class Agric(School):
    def farm(self):
        print('This is level 1')

class Science(School):
    def lab(self):
        print('This is laboratory')

class Student(Agric, Science):
    def level_1(self):
        print('This is level 1')

    def level_2(self):
        print('This is level 2')

student_agric = Student()
student_agric.library()
student_agric.sport_complex()
student_agric.farm()
student_agric.level_1()

student_science = Student()
student_science.library()
student_science.lab()
student_science.level_2()
