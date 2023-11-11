# calculates the average of array numbers using the array module

import array

numbers = array.array('i', [10, 5, 8, 12, 3])

sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)

print(f"Average: {average}")