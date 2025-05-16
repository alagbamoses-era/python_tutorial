#!/usr/bin/python3


class Stack:
    def __init__(self):
        self.stack = [ ]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise Indexerror("Pop from empty stack")

    def last_value(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

## Usage
s = Stack()
s.push(10)
s.push(20)
s.push(20)

print(s.pop())
print(s.is_empty())
print('Last value', s.last_value())

print(s.size())

print(s.pop())
print('Last value 2: ', s.last_value())
print(s.pop())
print(s.is_empty())
print(s.size())




