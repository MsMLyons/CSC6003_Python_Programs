# List methods

# concatenation
first_list = [23, 51]
second_list = [34, 16]
final_list = first_list + second_list
print(final_list)
# output --> [23, 51, 34, 16]

# replication
print(final_list * 3)
# output --> [23, 51, 34, 16, 23, 51, 34, 16, 23, 51, 34, 16]

# sort list
my_list = [23, 51, 34, 16, 84, 72]
my_list.sort()
print(my_list)
# output --> [16, 23, 34, 51, 72, 84]

# reverse list
my_list.reverse()
print(my_list)
# output --> [84, 72, 51, 34, 23, 16]

# append list
my_list.append(65)
print(my_list)
# output --> [84, 72, 51, 34, 23, 16, 65]

# remove a value from the list
my_list.remove(34)
print(my_list)
# output --> [84, 72, 51, 23, 16, 65]

# pop a value from the list at indicated index value
my_list.pop(4)
print(my_list)
# output --> [84, 72, 51, 23, 65]

# insert a value at specified index location
my_list.insert(3, 77)
print(my_list)
# output --> [84, 72, 51, 77, 23, 65]

# clear list
my_list.clear()
print(my_list)
# output --> [] (empty list)

# split list
a = "There is a blaze of light in every word"
a_list = a.split()
print(a_list)
# output --> ['There', 'is', 'a', 'blaze', 'of', 'light', 'in', 'every', 'word']