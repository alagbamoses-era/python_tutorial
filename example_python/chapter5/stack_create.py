#!/usr/bin/python3

from collections import deque
from queue import LifoQueue
import stack_custom 


stack = []


# push elements

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# pop element

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)


#### using collections.deque (Recommended)

stack = deque()

# push elements

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# pop element
print(stack.pop())
print(stack)


##### using queue.LifoQueue (Thread-safe)


stack = LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)

print(stack)

## pop element

print(stack.get())




### Using custom stack 

s = stack_custom.Stack()
s.push(100)
s.push(200)
s.push(300)


print(s.is_empty())
print(s.last_value())
print(s.pop())


