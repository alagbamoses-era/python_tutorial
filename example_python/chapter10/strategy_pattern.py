#!/usr/bin/python3

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy(data)

def strategy_add(data):
    return sum(data)

def strategy_max(data):
    return max(data)

ctx = Context(strategy_add)
print(ctx.execute([1, 2, 3]))

ctx_max = Context(strategy_max)
print(ctx_max.execute([1, 2, 3]))

