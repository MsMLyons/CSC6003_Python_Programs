def count_up_down():
    target = int(input("Please enter a positive integer: "))

    for value in range(1, target + 1):
        print(value)
    
    while target >= 1:        
        print(target)
        target -= 1

count_up_down()