# Examples of string methods

text = "   Hello, World!   "

# remove leading and trailing whitespace
stripped_text = text.strip()
print(stripped_text)
# output --> Hello, World! (without whitespace)

# remove whitespace from the beginning of the string
left_text = text.lstrip()
print(left_text)
# output --> Hello, World! (no whitespace on the left)

# remove whitespace from the end of the string
right_text = text.rstrip()
print(right_text)
# output -->     Hello, World! (contains whitespace on the left but no whitespace on the right)

# replace characters in text with another character
replace_text = text.replace('o', '0')
print(replace_text)
# output -->    Hell0, W0rld!   (also has preceding and final whitespace)

# check if string consists only of letter characters
is_alpha = text.isalpha()
print(is_alpha)
# output --> False (whitespace, comma, exclamation point)

new_text = 'Hi'
is_alpha = new_text.isalpha()
print(is_alpha)
# output --> True

# change text to all upper case
my_text = "It's a beautiful day in the neighborhood."
upper_case_text = my_text.upper()
print(upper_case_text)
# output --> IT'S A BEAUTIFUL DAY IN THE NEIGHBORHOOD.

# change text to all lower case
lower_case_text = my_text.lower()
print(lower_case_text)
# output --> it's a beautiful day in the neighborhood.

# capitalize the first letter in the string
capitalize_text = my_text.capitalize()
print(capitalize_text)
# output --> It's a beautiful day in the neighborhood.

# find specific characters
find_char = my_text.find('i')
print(find_char)
# output --> 12 (the lower case i in beautiful is at index position 12)

# count 
count_text = my_text.count('e')
print(count_text)
# output --> 3 (there are 3 e's in the text)

# does the string start with a specific character
text_start = my_text.startswith('T')
print(text_start)
# output --> False (the string does not start with 'T')

# does the string end with a specific character
text_end = my_text.endswith('.')
print(text_end)
# output --> True (the string ends with '.')

# does the string consist of digits
isdigit_text = my_text.isdigit()
print(isdigit_text)
# output --> False

my_digit = '123'
maybe_digit = my_digit.isdigit()
print(maybe_digit, 'hi')
# output --> True

# does the string consist of numbers
isnum_text = my_text.isalnum()
print(isnum_text)
# output --> False

maybe_num = my_digit.isalnum()
print(maybe_num, 'hello')
# output --> True