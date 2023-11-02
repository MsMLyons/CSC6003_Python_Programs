'''
Write a program that
receives three numbers (a, b,
c) and discovers (prints out)
which one among them is 
the largest one
'''

print("Hi, there! Let's compare some numbers to see which is the biggest one.")

A = int(input("Please enter a number: "))
B = int(input("Please enter another number: "))
C = int(input("Please enter a third number: "))

def compare_numbers():
    if A == B == C:
        print("These numbers are all equal.")
    elif A < B and A < C:
        if B < C:
            print(f"{C} is the largest number out of {A}, {B}, and {C}.")
    elif A < B and B > C:
        print(f"{B} is the largest number out of {A}, {B}, and {C}.") 
    else:
        if A > B and A > C:
            print(f"{A} is the largest number out of {A}, {B}, and {C}.")

compare_numbers()