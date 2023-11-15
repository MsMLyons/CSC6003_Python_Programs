# Write a Python program that takes an array of integers as input 
# and sorts the elements in ascending order.

def get_values():
    values = []
    user_input = int(input("Please enter the number of elements in the array: "))
    for i in range(0, user_input):
        element = int(input("Please enter an element: "))
        values.append(element)
    print(f"The values entered are: {values}")
    return values

def sort_values(values):
    values.sort()
    print(f"The values sorted in ascending order are: {values}")

values = get_values()
sort_values(values)