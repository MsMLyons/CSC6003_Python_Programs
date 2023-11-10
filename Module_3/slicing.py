# to slice, know the index values
text = "Hello, World!"

# Indexing (begins at 0 for the first character)
# access the first character
print(text[0])
# output --> H

# access the 8th character
print(text[7])
# output --> W

# access the last character
print(text[-1])
# output --> !

# Slicing
# get the substring 'Hello'
print(text[0:5])
# output --> Hello

# get the substring starting from the 8th character
# and going to the end
print(text[7:])
# output --> World!

# get the substring starting up to the 5th character
print(text[:5])
# output --> Hello

