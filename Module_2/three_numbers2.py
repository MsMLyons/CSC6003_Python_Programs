a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = int(input("Please enter a third number: "))

if a > b:
    if a > c:
        print("The largest is", a)
    else: print("The largest is", c)
else:
    if b > c:
        print("The largest is", b)
    else: print("The largest is", c)