# use NumPy 
import numpy as np

# create a new NumPy array
numpy_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

# accessing elements and performing operations
print("\nNumPy Array elements: ")
for num in numpy_array:
    print(num)

# output -->
# NumPy Array elements:
# 1.0
# 2.0
# 3.0
# 4.0
# 5.0

# element-wise operations with NumPy
result_array = numpy_array * 2
print("\nNumPy Array * 2: ")
print(result_array)

# output --> 
# NumPy Array * 2:
# [ 2.  4.  6.  8. 10.]