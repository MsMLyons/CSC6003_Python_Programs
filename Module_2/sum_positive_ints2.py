def sum_positives():
    total = 0
    while True:
        num = int(input("Please enter a positive number (negative to quit): "))
        if num < 0:
            break
        total += num
    print(f"The sum of the positive numbers is: {total}")
sum_positives()