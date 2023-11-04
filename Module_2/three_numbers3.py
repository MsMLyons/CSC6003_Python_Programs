a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = int(input("Please enter a third number: "))

if a > b and a > c:
    print("The largest is", a)
elif a == c and a == b:
    print("The values", a, ",", b, "and", c, "are equal")
elif a < c and b < c:
    print("The largest is", c)
else:
    print("The largest is", b)