#!/usr/bin/python3

# Multilevel inheritance is a type of inheritance where a class is derived 
# from another class, which is itself derived from another class, forming a 
# chain of classes.

# Example: The prototype structure:
# Grandparent --> Parent --> Child
# Each class inherits from the one above it

class Grandparent:
    def g_parent(self):
        print('This is grandparent')

class Parent(Grandparent):
    def p_parent(self):
        print('This is parent')

class Child(Parent):
    def c_child(self):
        print('This is Child')

child = Child()
child.g_parent()
child.p_parent()
child.c_child()


