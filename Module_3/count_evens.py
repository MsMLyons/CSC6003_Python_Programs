# Counting Even Numbers Write a
# program that prompts the user to
# enter a list of numbers and then
# counts the number of even
# numbers in that list.

numbers = input("Please enter a list of numbers separated by spaces: ").split()

count = 0
for num in numbers:
    if int(num) % 2 == 0:
        count += 1
print(f"The number of even numbers in the list is: {count}")
# output --> The number of even numbers in the list is: 9