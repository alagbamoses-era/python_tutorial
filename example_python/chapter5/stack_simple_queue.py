#!/usr/bin/python3


class Queue:
        def __init__(self):
            self.items = []  # Initialize an empty queue

        def enqueue(self, item):
            #"""Add an item to the end of the queue"""
            self.items.append(item)

        def dequeue(self):
            #"""Remove and return the front item from the queue"""
            if not self.is_empty():
                return self.items.pop(0)  # Removes the first element
            return None  # Return None if queue is empty

        def is_empty(self):
            #"""Check if the queue is empty"""
            return len(self.items) == 0

        def peek(self):
            #"""Get the front item without removing it"""
            return self.items[0] if not self.is_empty() else None

        def size(self):
            #"""Return the number of elements in the queue"""
            return len(self.items)

        def __str__(self):
            return f"Queue: {self.items}"
        


