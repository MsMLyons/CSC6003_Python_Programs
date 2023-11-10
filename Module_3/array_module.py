# import and use the array module
import array

# create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])

# accessing elements
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