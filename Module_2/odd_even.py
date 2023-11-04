def odd_even():
    print("Let's check to see if a number is odd or even")
    num = float(input("Enter a number: "))
    if num % 2 == 0:
        print(f"The number {num} is even", num % 2 == 0, sep = ", ")
    else:
        print(f"The number {num} is odd", num % 2 == 0, sep = ", ")
odd_even()