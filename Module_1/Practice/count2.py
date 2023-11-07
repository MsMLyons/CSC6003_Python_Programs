def count():
    print("Let's count the coins in your piggy bank")
    pennies = int(input("How many pennies do you have? "))
    nickels = int(input("How many nickels do you have? "))
    dimes = int(input("How many dimes do you have? "))
    quarters = int(input("How many quarters do you have? "))

    p = 1 * pennies
    n = 5 * nickels
    d = 10 * dimes
    q = 25 * quarters

    sum = (p + n + d + q) / 100
    print(f"The total value of the piggy bank is {sum}")

count()