def star_grid():
    rows = int(input("Please enter the number of rows 1 - 10: "))
    columns = int(input("Please enter the number of columns 1 - 10: "))

    for i in range(rows):
        for j in range(columns):
            print("*", end = " ")
        print()
star_grid()