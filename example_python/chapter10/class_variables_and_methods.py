#!/usr/bin/python3

class Employees:
    company = 'TechCorp'

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_company(cls):
        print(cls.company)

Employees.show_company()

employees = Employees('ERA')

employees.show_company()

