print("Let's compare some numbers and see how they compare with Booleans!")

a = float(input("Enter a number for a: "))
b = float(input("Enter a number for b: "))

print("a == b", a == b)
print("a < b", a < b)
print("a > b", a > b)
print("a <= b", a <= b)
print("a >= b", a >= b)
print("a != b", a != b)

c = float(input("Enter a number for c: "))
d = float(input("Enter a number for d: "))

print("(", a, "< c) and (", b, "> d):", (a < c) and (b < d))
print("(", a, "< c) and (", b, "> d):", (a < c) or (b < d))

print("I hope you had fun learning about Booleans!")