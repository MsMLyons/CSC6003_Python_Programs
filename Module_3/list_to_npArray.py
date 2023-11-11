import numpy as np

# prompt for the number of elements in the array
num_elements = int(input("Please enter the number of elements: "))

# create an empty list to store the input values
elements = []

# prompt for the inputs in a loop
for i in range(num_elements):
    value = float(input(f"Enter element {i+1}: "))
    elements.append(value)

# convert the list to a numpy array
my_array = np.array(elements)

# print the numpy array
print(f"NumPy array: {my_array}")

# output -->
# Please enter the number of elements: 5
# Enter element 1: 2
# Enter element 2: 4
# Enter element 3: 6
# Enter element 4: 8
# Enter element 5: 10
# NumPy array: [ 2.  4.  6.  8. 10.]