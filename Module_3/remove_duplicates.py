# Write a program that prompts the
# user to enter a list of strings and
# then removes any duplicate
# strings from that list. 

# Hints:
# 1. Once again prompt for input
# with spaces
# 2. Use .split()
# 3. Create a blank list variable for
# the result

# test
string_list = []

my_string = input("Please enter a list of strings, separated by spaces: ").split(', ')

string_list.append(my_string)

print(f"This is the list of strings you entered: {my_string}")
# output --> This is the list of strings you entered: ['a cork pickle popcorn cheezit my alphabet soup pumpkin']

print(f"This is new list of strings: {string_list}")
# output --> This is new list of strings: [['a cork pickle popcorn cheezit my alphabet soup pumpkin']]

# responds to prompt
strings = input("Enter a list of strings, separated by spaces: ").split()
print(f"This is the list of strings you entered: {strings}")
# output --> This is the list of strings you entered: 
# ['a', 'cork', 'pickle', 'popcorn', 'cheezit', 'my', 'alphabet', 'soup', 'pumpkin', 'soup', 'pickle', 'cork', 'a']
result = []
for string in strings:
    if string not in result:
        result.append(string)
print(f"List with duplicates removed: {result}")
# output --> List with duplicates removed: ['a', 'cork', 'pickle', 'popcorn', 'cheezit', 'my', 'alphabet', 'soup', 'pumpkin']
