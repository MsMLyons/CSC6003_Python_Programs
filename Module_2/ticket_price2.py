age = int(input("Enter visitor's age: "))

if age < 3:
    ticket_price = 0
elif 3 <= age <= 12:
    ticket_price = 10
else: 
    ticket_price = 15

print(f"The ticket price is ${ticket_price}")