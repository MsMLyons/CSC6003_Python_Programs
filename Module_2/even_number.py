def even_number():
    num = int(input("Enter the maximum number in the range: "))
    for number in range(num):
        if number % 2== 0:
            print(number)
even_number()