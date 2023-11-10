# nested list contains 3 sublists, each representing a row of numbers
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nested list comprehension with 2 parts
# num ** 2 to square each element in the nested list
# for sublist in nested_list for num in sublist - outer and inner loops
squared_list = [num ** 2 for sublist in nested_list for num in sublist]
print(squared_list)
# output --> [1, 4, 9, 16, 25, 36, 49, 64, 81]