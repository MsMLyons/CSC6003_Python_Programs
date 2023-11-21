# Stack: Last-in, first-out (LIFO) data structure
# the last element added is the first element retrieved
# add an element with append()
# retrieve an element with pop()

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

# output --> [3, 4, 5, 6, 7]

stack.pop()
print(stack)

# output --> [3, 4, 5, 6]

stack.pop()
print(stack)

# output --> [3, 4, 5]

stack.pop()
print(stack)

# output --> [3, 4]