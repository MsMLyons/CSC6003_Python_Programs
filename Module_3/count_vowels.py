# Write a program that prompts
# the user to enter a string and
# then counts the number of
# vowels (a, e, i, o, u) in that
# string.

string = input("Please enter a string of characters: ")
count = 0
for character in string:
    if character.lower() in "aeiou":
        count += 1
print(count)
# output --> 11