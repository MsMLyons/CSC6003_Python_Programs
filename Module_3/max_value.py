# Find the maximum element in 
# that list using the array module

import array

# declare array of numbers
numbers = array.array('i', [10, 5, 8, 12, 3])

# declare max number equal to first number in array
max_number = numbers[0]

# compare other numbers in array to the first number
# reassign the maximum element to num variable if larger than
# the first value
for num in numbers:
    if num > max_number:
        max_number = num

print(f"Maximum element: {max_number}")
