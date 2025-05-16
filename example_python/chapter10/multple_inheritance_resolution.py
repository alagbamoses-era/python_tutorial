#!/usr/bin/python3

class A:
    def do_something(self):
        print('A')

class B(A):
    def do_something(self):
        print('B')

class C(A):
    def do_somethings(self):
        print('C')

class D(B, C):
    pass

d = D()
d.do_something()
d.do_somethings()
print(D.mro())


