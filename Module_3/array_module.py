# import and use the array module
import array

# create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])

# accessing elements / iterating over the array
print("Array elements: ")
for num in int_array:
    print(num)

# output --> 
# Array elements:
# 1
# 2
# 3
# 4
# 5

grades = array.array('f', [85.5, 90.0, 92.5, 88.75])
for grade in grades:
    print(grade)
print(grades)

# output --> 
# 85.5
# 90.0
# 92.5
# 88.75

# output --> array('f', [85.5, 90.0, 92.5, 88.75])

# access values at specific index
numbers = array.array('i', [12, 13, 14, 15, 16])
print(numbers[0])
print(numbers[3])

# output --> 
# 12
# 15

# modify an element
numbers[1] = 10
print(numbers)
# output --> array('i', [12, 10, 14, 15, 16])

# length of an array
print(len(numbers))
# output --> 5

# append elements to the array
numbers.append(26)
print(numbers)
# output --> array('i', [12, 10, 14, 15, 16, 26])

# remove elements from the array
numbers.remove(12)
print(numbers)
# output --> array('i', [10, 14, 15, 16, 26])

# convert array to a list
numbers_list = numbers.tolist()
print(numbers_list)
# output --> [10, 14, 15, 16, 26]