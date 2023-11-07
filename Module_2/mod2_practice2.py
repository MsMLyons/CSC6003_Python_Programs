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
        
    print(is_evenly_divided())
main()
