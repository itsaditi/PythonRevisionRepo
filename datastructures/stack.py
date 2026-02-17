"""
python3 queue.py
"""

from collections import deque

## Using Double ended queue
stack = deque()

# Enqueue elements into the queue
stack.append('Task 1')
stack.append('Task 2')
stack.append('Task 3')
stack.append('Task 4')

print(stack)

while len(stack) != 0:
    print("Dequeued element", stack.pop())


## Using List
list_queue = []

list_queue.append('Task 1')
list_queue.append('Task 2')
list_queue.append('Task 3')
list_queue.append('Task 4')

print(list_queue)

while len(list_queue) != 0:
    print("Dequeued element", list_queue.pop())