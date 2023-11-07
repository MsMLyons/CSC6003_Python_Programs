"""
File: lyonsm_module_2.py
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 2
Date Created: 2023-11-05
Date Updated: 2023-11-06

Description: This program asks the user for two 
positive integers and returns True if either 
evenly divides the other. If neither value
evenly divides the other, or the user enters
a negative number, the program continues to
prompt the user for new values. 

"""
def is_evenly_divided():
    ''' Function to prompt the user for positive integers and evaluate if they divide evenly '''
    
    while True:
        num1 = int(input("\nPlease enter a positive integer: "))
        num2 = int(input("\nPlease enter another positive integer: "))

        if num1 > 0 and num2 > 0:
            if num1 % num2 != 0 and num2 % num1 != 0:
                print("\nThose integers do not divide evenly. Please try again.")                
                continue
            else:
                print("\nAt least one of those integers divides the other evenly.\n")
                return num1 % num2 == 0 or num2 % num1 == 0                
                break
        else: 
            print("\nInvalid entry. Please enter only positive integers.")            
            continue

def main():
    ''' Function to find and print the result of the is_evenly_divided function '''
    
    result = is_evenly_divided()
    print(result)
main()


