# List comprehension 

# make a new list of squared numbers based on a list of numbers
numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
# output --> [1, 4, 9, 16, 25, 36]

# filtering even numbers
numbers = [11, 12, 13, 14, 15, 16]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
# output --> [12, 14, 16]

