# Queue: First-in, first-out (FIFO) data structure
# the first element added is the first element retrieved (first in, first out)
# collections.deque --> designed to append and pop quickly from both ends of a list

from collections import deque

queue = deque(["Erin", "Jalaya", "Michelle"])
queue.append("Tippee")
queue.append("Anastasia")
print(len(queue))
print(queue)

# output --> 
    # 5
    # deque(['Erin', 'Jalaya', 'Michelle', 'Tippee', 'Anastasia'])

queue.popleft()
print(len(queue))
print(queue)

# output -->
    # 4
    # deque(['Jalaya', 'Michelle', 'Tippee', 'Anastasia'])