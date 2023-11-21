class Stack:
    # initialize class
    def __init__(self):
        self.items = []

    # add an element to the top of the stack
    def push(self, item):
        self.items.append(item)

    # remove and return the topmost element
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    # return the topmost element without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError