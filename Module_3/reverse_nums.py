# Write a program that prompts the
# user to enter a list of numbers and
# then prints the reverse of that list.

numbers = input("Please enter a list of numbers, separated by commas: ").split(', ')

print(f"This is the list of numbers you entered: {numbers}")
# output --> This is the list of numbers you entered: ['2', '5', '8', '9', '3', '0', '6']

reverse_numbers = numbers[::-1]

print(f"And this is that list of numbers in reverse: {reverse_numbers}")
# output --> And this is that list of numbers in reverse: ['6', '0', '3', '9', '8', '5', '2']