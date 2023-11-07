def check_divisibility(num1, num2):
    return bool(num1 % num2 == 0 or num2 % num1 ==0)

def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    num1 = get_positive_integer("Enter a positive integer: ")
    num2 = get_positive_integer("Enter a another positive integer: ")

    result = check_divisibility(num1, num2)

    if result:
        print("At least one of these integers divides the other evenly.")
    else:
        print("Neither of these integers divides the other evenly.")

if __name__ == "__main__":
    main()