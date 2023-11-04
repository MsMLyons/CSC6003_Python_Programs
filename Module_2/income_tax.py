def income_tax():
    print("Let's calculate your income tax. \n")
    income = float(input("Please enter your anual income without using a comma to separate values: "))
    print()
    if income < 10000:
        print("Your income is below the value to charge income tax, so no tax for you.")
    elif income >= 10001 and income <= 50000:
        tax_10 = income * 0.10
        print(f"Your income tax is 10% of your income, which is {tax_10}.")
    elif income > 50001 and income <= 100000:
        tax_20 = income * 0.20
        print(f"Your income tax is 20% of your income, which is {tax_20}.")
    else:
        tax_30 = income * 0.30
        print(f"Your income is over $100,000, therefore your income tax is 30% of your income, which is {tax_30}.")
income_tax()