# Write a Python program that takes two arrays of integers as input 
# and calculates their element-wise sum. The two arrays should have the same length.
# https://www.geeksforgeeks.org/python-adding-two-list-elements/

import array

def get_two_arrays():
    ''' Function to receive user input and store it in two equal-sized arrays '''
    # create empty arrays to store user input
    array1 = array.array('i', [])
    array2 = array.array('i', [])

    # prompt for user input of the number of elements in the arrays    
    user_input = int(input("Please enter the number of elements in each array: "))
    
    # prompt for first set of elements to be appended to array1
    for i in range(0, user_input):
        element = int(input("Please enter an element for array 1: "))
        array1.append(element)
        # convert the array to a list for better visual representation when printing
        my_array1 = array1.tolist()
    
    # prompt for second set of elements to be appended to array2
    for j in range(0, user_input):
        element2 = int(input("Please enter an element for array 2: "))
        array2.append(element2)
        # convert the array to a list for better visual representation when printing
        my_array2 = array2.tolist()

    # print the lists with the elements from each array for user confirmation (optional)
    print(f"Array 1 is: {my_array1}")
    print(f"Array 2 is: {my_array2}")

    # return the elements in the arrays for use in other functions
    return array1, array2


def sum_elements(array1, array2):
    ''' Function to sum the elements of two arrays '''

    # create a list to store the values of the summed elements
    # use list comprehension to carry out the calculation
    array3 = [array1[i] + array2[i] for i in range(len(array1))]
    print(f"The sum of each element in array 1 and array 2 is: {array3}")


array1, array2 = get_two_arrays()
sum_elements(array1, array2)
