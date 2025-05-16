#!/usr/bin/python3


class Coffee:
    def cost1(self):
        return 5

class MilkDecorator(Coffee):
    def __init__(self, base):
        self.base = base

    def cost2(self):
        return self.base.cost1() + 2

coffee = MilkDecorator(Coffee())
print(coffee.cost2()) # output: 7
