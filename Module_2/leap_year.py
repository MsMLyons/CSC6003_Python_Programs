def leap_year():
    print("Let's check if a given year is a leap year.")
    year = int(input("Please enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else: print (f"{year} is not a leap year")

leap_year()