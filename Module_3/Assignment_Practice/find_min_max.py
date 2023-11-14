# Write a Python program that takes an array of integers as input 
# and finds the maximum and minimum values in the array.

import array

def get_values():
    values = array.array('i', [])
    user_input = int(input("Please enter the number of elements in the array: "))
    for i in range(0, user_input):
        element = int(input("Please enter an element: "))
        values.append(element)
    return values
    
def find_max(values):
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value        
    return max_value

def find_min(values):
    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
    return min_value

user_values = get_values()

max_value = find_max(user_values)
min_value = find_min(user_values)

print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")