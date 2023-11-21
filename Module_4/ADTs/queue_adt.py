class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        # adds an item to the rear of the queue
        self.items.append(item)

    def dequeue(self, item):
        # removes and returns the item from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def peek(self):
        # returns the item from the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
        
    def is_empty(self):
        # examine the length of the list to determine whether it is empty or not
        return len(self.items) == 0
    
    def size(self):
        # returns the number of items currently in the queue by returning the length of the list
        return len(self.items)
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.size())
print(q.dequeue(1))
print(q.peek())

# output -->
    # 3
    # 10
    # 20
