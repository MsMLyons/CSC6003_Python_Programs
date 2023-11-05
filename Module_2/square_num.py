def square_num():
    while True:
        user_input = input("Enter a number (0 to exit): ")
        if user_input == '0':
            break
        else:
            num = int(user_input)
            square = num * num
            print(f"The square of {num} is {square}")
square_num()

def square_num2():
    while True:
        num = int(input("Enter a number (0 to exit): "))
        if num == 0:
            break
        else:
            square = num * num
            print(f"The square of {num} is {square}")
square_num2()