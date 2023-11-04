print("Let's compare some numbers!")

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))

if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y is", x / y)
elif x < y:
    print("x is less than y")
else:
    print("y is less than x")
print("I hope you had fun comparing these numbers!")