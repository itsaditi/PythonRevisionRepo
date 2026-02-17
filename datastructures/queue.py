"""
python3 queue.py
"""

from collections import deque

## Using Double ended queue
queue = deque()

# Enqueue elements into the queue
queue.append('Task 1')
queue.append('Task 2')
queue.append('Task 3')
queue.append('Task 4')

print(queue)

while len(queue) != 0:
    print("Dequeued element", queue.popleft())


## Using List
list_queue = []

list_queue.append('Task 1')
list_queue.append('Task 2')
list_queue.append('Task 3')
list_queue.append('Task 4')

print(list_queue)

while len(list_queue) != 0:
    print("Dequeued element", list_queue.pop(0))