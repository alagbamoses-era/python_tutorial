#!/usr/bin/python3

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self): pass
        

class Eater(ABC):
    @abstractmethod
    def eat(self): pass


class Fun(Workable):
    def work(self): print('Working')

    def eat(self): print('Eating')

fun = Fun()
fun.work()
fun.eat()

