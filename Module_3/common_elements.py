# Given two lists of numbers, write a
# program to create a new list that
# contains the elements common to
# both lists.

# Note: Must use list
# comprehension


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = list1 + list2

# create a list with repeated values
print(list3)
# output --> [1, 2, 3, 4, 5, 4, 5, 6, 7, 8]

new_list = []

# create a list with non-repeated values
unique_elements = [new_list.append(num) for num in list3 if num not in new_list]
print(f"The unique elements in lists 1 and 2 are: {new_list}")
# output --> The unique elements in lists 1 and 2 are: [1, 2, 3, 4, 5, 6, 7, 8]

# this answers the prompt, singling out repeated values in list1 and list2
common_elements = [num for num in list1 if num in list2]
print(f"The common elements in lists 1 and 2 are: {common_elements}")
# output --> The common elements in lists 1 and 2 are: [4, 5]