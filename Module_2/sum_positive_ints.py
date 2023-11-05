def sum_positives():
    num_list = []
    Sum = 0

    while True:
        num = int(input("Please enter a positive number: "))        

        if num > 0:                        
            num_list.append(num)
            Sum += num            
        else:
            print("Sorry, that is not positive number")
            print(f"The sum of all the positive numbers you entered is {Sum}")
            break
sum_positives()