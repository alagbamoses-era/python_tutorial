#!/usr/bin/python3

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print('Salary must be positive.')

# Usage
e = Employee(5000)

print(e.salary) # No need to call get_salary()!

e.salary = 600 # No need to call set_salary()!

print(e.salary)

e.salary = -1000 # Invalid salary, prints error.
