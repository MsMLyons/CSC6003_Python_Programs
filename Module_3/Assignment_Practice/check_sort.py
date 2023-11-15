# Write a Python program that takes an array of integers as input 
# and checks if the array is sorted in non-decreasing order.

def get_values():
    values = []
    user_input = int(input("Please enter the number of elements in the array: "))
    for i in range(0, user_input):
        element = int(input("Please enter an element: "))
        values.append(element)
    print(f"The values entered are: {values}")
    return values

def is_increasing_order(values):
    if values == sorted(values):
        print("The values entered are sorted in increasing order.")
    else:
        print("The values entered are not sorted in increasing order.")

values = get_values()
is_increasing_order(values)