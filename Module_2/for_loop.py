# Using a for loop, write a code fragment that counts backward from 50 to 25 by 5’s 
# and only prints out the values 50, 45, 40…etc. until 25

# Example 1
def count_back():
    num = 55
    for i in range(num):
        if num >= 30:
            num = num - 5
            print(num)
count_back()

# Example 2
def count_back1():    
    for num in range(50, 20, -5):
        print(num)
count_back1()