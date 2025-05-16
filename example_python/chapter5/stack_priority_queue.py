#!/usr/bin/python3


#### priority Queue
import queue 
# from queue import PriorityQueue

pq = queue.PriorityQueue()

# Enqueue (priority, value)
pq.put((2, "Task A"))
pq.put((1, "Task B"))
pq.put((3, "Task C"))

# dequeue (sorted by priority)
print(pq.get())
print(pq.get())
