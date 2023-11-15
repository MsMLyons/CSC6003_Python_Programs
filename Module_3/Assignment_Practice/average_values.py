# Write a Python program that takes an array of integers as input 
# and calculates the average (mean) of all the elements in the array.

def get_values():
    values = []
    user_input = int(input("Please enter the number of elements in the array: "))
    for i in range(0, user_input):
        element = int(input("Please enter an element: "))
        values.append(element)
    print(f"The values entered are: {values}")
    return values

def calculate_average(values):
    average = sum(values) / len(values)
    print(average)

values = get_values()
calculate_average(values)