# Write a Python program that takes two arrays of integers as input 
# and calculates their element-wise sum. The two arrays should have the same length.
# https://www.geeksforgeeks.org/python-adding-two-list-elements/

#import array

def get_values():
    # array1 = array.array('i', [])
    # array2 = array.array('i', [])
    array1 = []
    array2 = []
    user_input = int(input("Please enter the number of elements in each array: "))
    for i in range(0, user_input):
        element = int(input("Please enter an element for array 1: "))
        array1.append(element)
    for j in range(0, user_input):
        element2 = int(input("Please enter an element for array 2: "))
        array2.append(element2)
    print(f"Array 1 is: {array1}")
    print(f"Array 2 is: {array2}")
    return array1, array2


def sum_elements(array1, array2):
    array3 = [array1[i] + array2[i] for i in range(len(array1))]
    print(f"The sum of each element in array 1 and array 2 is: {array3}")


array1, array2 = get_values()
sum_elements(array1, array2)
