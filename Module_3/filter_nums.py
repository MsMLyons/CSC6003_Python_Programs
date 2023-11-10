# filter list of numbers for specific values
numbers = [1, 4, 7, 9, 10, 12, 15, 18]
new_list = [num for num in numbers if num > 5 and num % 2 == 0]
print(f"This is the new list of numbers based on the filters greater than 5 and evenly divisible: {new_list}")
# output --> This is the new list of numbers based on the filters greater than 5 and evenly divisible: [10, 12, 18]