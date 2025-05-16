#!/usr/bin/python3

import stack_simple_queue

### Example

q = stack_simple_queue.Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)


print(q.dequeue())
print(q)

