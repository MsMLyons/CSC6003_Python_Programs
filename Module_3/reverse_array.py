# printsthe reverse of an array using the array module

import array

numbers = array.array('i', [10, 5, 8, 12, 3])

reversed_numbers = array.array('i', [])

for i in range(len(numbers) -1, -1, -1):
    reversed_numbers.append(numbers[i])

print(f"Reversed list: {reversed_numbers}")
