# String Functions
# Identify 3 string functions available in Python
# source: https://www.w3schools.com/python/python_ref_string.asp

# count() --> Returns the number of times a specified value occurs in a string
my_string = "Hi there, Friends! How are you?"
frequency = my_string.count("e")
print(frequency)
# output --> 4

# endswith() --> Returns true if the string ends with the specified value
new_string = "What are you looking forward to?"
string_end = new_string.endswith("?")
print(string_end)
# output --> True

# replace() --> Returns a string where a specified value is replaced with a specified value
another_string = "I'm looking forward to time off work!"
replacement = another_string.replace("time off work", "vacation")
print(replacement)
# output --> I'm looking forward to vacation!