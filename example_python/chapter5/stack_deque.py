#!/usr/bin/python3

from collections import deque
from queue import Queue

queue = deque()

# Enqueue (add elements)

queue.append(10)
queue.append(20)
queue.append(30)


# Dequeue (remove elements)
print('first item:', queue.popleft())
print(queue)
print('second item: ', queue.popleft())
print('Third item: ', queue.popleft())
print(queue)





##### Using queue.Queue (thread-safe)

q = Queue()

# Enqueue
q.put(10)
q.put(20)
q.put(30)


# Dequeue

print(q.get())
print(q.get())



