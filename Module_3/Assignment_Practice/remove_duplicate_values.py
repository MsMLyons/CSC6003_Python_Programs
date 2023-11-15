# Write a Python program that takes an array of integers as input 
# and removes all duplicate elements, keeping only the unique elements in the array.

def remove_duplicates():
    array1 = input("Enter a list of integers, separated by spaces: ").split()
    print(f"This is the array of integers you entered: {array1}")

    array2 = []
    for element in array1:
        if element not in array2:
            array2.append(element)
    print(f"This is the array with duplicate integers removed: {array2}")
remove_duplicates()