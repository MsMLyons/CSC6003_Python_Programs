# Examples of ternary operators

x = 10
y = "Even" if x % 2 == 0 else "Odd"
print(y)

x = 12
y = "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
print(y)

age = 25
can_rent_appt = True if age >= 18 and age <= 120 else False
print(can_rent_appt)

def is_even(n):
    return True if n % 2 == 0 else False

result = is_even(13)
print(result)