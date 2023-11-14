# Write a Python program that takes an array of integers as input 
# and calculates the sum of all the elements in the array.
import array

def calculate_sum():
    numbers = array.array('i', [])
    user_input = int(input("Please enter the number of elements in the array: "))
    for i in range(0, user_input):
        element = int(input("Please enter an element: "))
        numbers.append(element)
    Sum = sum(numbers)
    print(numbers)
    print(Sum)

# Write a Python program that takes an array of integers as input 
# and finds the maximum and minimum values in the array.

def find_max_min():
    values = array.array('i', [])
    user_input = int(input("Please enter the number of elements in the array: "))
    for i in range(0, user_input):
        element = int(input("Please enter an element: "))
        values.append(element)
    
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value
        print(max_value)

    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
        print(min_value)

# Write a Python program that takes two arrays of integers as input 
# and calculates their element-wise sum. The two arrays should have the same length.


# Write a Python program that takes an array of integers as input 
# and removes all duplicate elements, keeping only the unique elements in the array.


# Write a Python program that takes an array of integers as input 
# and sorts the elements in ascending order.


# Write a Python program that takes an array of integers as input 
# and checks if the array is sorted in non-decreasing order.


# Write a Python program that takes an array of integers as input 
# and calculates the average (mean) of all the elements in the array.

def main():
    ''' Function to call the functions for each program '''
    
    #calculate_sum()
    find_max_min()
main()