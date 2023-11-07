def count():
    print("Let's count the coins in your piggy bank")
    pennies = float(input("How many pennies do you have? "))
    nickels = float(input("How many nickels do you have? "))
    dimes = float(input("How many dimes do you have? "))
    quarters = float(input("How many quarters do you have? "))

    p = (0.01 * pennies)
    n = (0.05 * nickels)
    d = (0.10 * dimes)
    q = (0.25 * quarters)

    sum = p + n + d + q
    print(f"The total value of the piggy bank is {sum}")

count()