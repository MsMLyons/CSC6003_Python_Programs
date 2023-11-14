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

calculate_sum()