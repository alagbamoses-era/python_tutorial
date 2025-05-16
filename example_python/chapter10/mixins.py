#!/usr/bin/python3


class LoggerMixin:
    def log(self, msg):
        print(f"[LOG]: {msg}")

class Number:
    def add(self, x, y):
        print(f'{x} + {y}= ', x + y)

class Students:
    def course(self, a, b):
        print(f'What grade do you have in {a} and {b}?')


class Worker(LoggerMixin, Number, Students):
    def work(self):
        self.log('Working hard ...') 
        self.add(2, 5)
        self.course('Maths', 'English')



w = Worker()
w.work()




