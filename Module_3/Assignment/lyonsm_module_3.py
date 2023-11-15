""" 
File: lyonsm_module_3.py
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 3
Date Created: 2023-11-12
Date Updated: 2023-11-14

Description: This program prompts the user to enter
two arrays. The arrays are converted to lists and
used as both arrays and lists to manipulate the
elements/values in each. The objectives include:
calculating sums and averages, sorting, removing
duplicates, and finding minimum and maximum values.
"""

import array

def get_arrays():
    ''' Function to receive user input and store it in two equal-sized arrays '''

    # create empty arrays to store user input
    array1 = array.array('i', [])
    array2 = array.array('i', [])

    # prompt for user input of the number of elements in the arrays    
    user_input = int(input("\nPlease enter the number of elements in each array: "))
    
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
    print(f"\nThe elements you entered for array 1 are: {my_array1}")
    print(f"The elements you entered for array 2 are: {my_array2}")

    # return the elements in the arrays for use in other functions
    return array1, array2, my_array1, my_array2


def calculate_sum(array1):
    ''' Calculate the sum of the elements of an array '''

    print("\nLet's calculate the sum of the elements of array 1.")    
    # use the sum function to find the sum of the elements of the array
    Sum = sum(array1)    
    print(f"The sum of the elements of array 1 is: {Sum}.")


def find_max(array1):
    ''' Function to find the maximum value in array 1 '''
    
    print("\nLet's find the maximum value in array 1.")
    # find the maximum value
    max_value = array1[0]
    for element in array1:
        if element > max_value:
            max_value = element           
    return max_value
    

def find_min(array1):
    ''' Function to find the minimum value in array 1 '''
    
    print("And let's find the minimum value in array 1.")
    # find the minimum value
    min_value = array1[0]
    for element in array1:
        if element < min_value:
            min_value = element
    return min_value


def sum_elements(array1, array2):
    ''' Function to sum the elements of two arrays '''

    print("\nLet's calculate the sum of the corresponding elements in each array.")
    # create a list to store the values of the summed elements
    # use list comprehension to carry out the calculation
    array3 = [array1[i] + array2[i] for i in range(len(array1))]
    print(f"The sums of the elements are: {array3}")


def remove_duplicates(array1):
    ''' Function to remove duplicates from array 1 '''

    # create a new array to store non-duplicate elements
    array4 = array.array('i', [])
    print("\nLet's make sure there are no duplicate elements in array 1.")
    # find non-duplicate elements and append them to the new array
    for element in array1:
        if element not in array4:
            array4.append(element)
            # create a list for better visualization when printing
            my_array4 = array4.tolist()
    print(f"This is the new array with any duplicate integers removed: {my_array4}")


def sort_values(my_array1):
    ''' Function to sort values of array 1 in ascending order'''

    print("\nLet's sort the values in array 1 in ascending order.")
    # use array converted to a list to sort the values
    my_array1.sort()
    print(f"The ascending order of the values is: {my_array1}")
    print("Now let's sort the values in array 1 in descending order.")
    my_array1.sort(reverse=True)
    print(f"The descending order of the values is: {my_array1}")


def is_increasing_order(my_array2):
    ''' Function to check if values in array 2 are sorted in non-decreasing order'''

    print("\nLet's check if the elements entered for array 2 are sorted in non-decreasing order.")
    # compare the list to its sorted self
    if my_array2 == sorted(my_array2):
        print("The values entered are sorted in increasing order.")
    else:
        print("The values entered are not sorted in non-decreasing order.")


def calculate_average(array1):
    ''' Function to average the values of the elements of array 1'''

    print("\nLet's calculate the average (mean) of the values entered for array 1.")
    # calculate the average
    average = sum(array1) / len(array1)
    print(f"The average value of the elements in array 1 is: {average}")


def main():
    ''' Function to call the functions for each program '''

    array1, array2, my_array1, my_array2 = get_arrays()
    calculate_sum(array1)
    max_value = find_max(array1)
    min_value = find_min(array1)
    print(f"The maximum value is: {max_value}")
    print(f"The minimum value is: {min_value}")
    sum_elements(array1, array2)
    remove_duplicates(array1)
    sort_values(my_array1)
    is_increasing_order(my_array2)
    calculate_average(array1)

main()