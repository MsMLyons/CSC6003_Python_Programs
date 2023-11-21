# customer database
customers = {
    "customer1": {"name": "Saron Thomas", "age": 25, "email": "saron@example.com"},
    "customer2": {"name": "Bill Young", "age": 32, "email": "bill@example.com"},
    "customer3": {"name": "Khloe Winton", "age": 18, "email": "kw@example.com"}
}

# iterating over customer information
for customer_id, customer_info in customers.items():
    print("Customer ID:", customer_id)
    print("Name:", customer_info["name"])
    print("Name:", customer_info["age"])
    print("Name:", customer_info["email"])
    print()

# output --> 
    # Customer ID: customer1
    # Name: Saron Thomas
    # Name: 25
    # Name: saron@example.com

    # Customer ID: customer2
    # Name: Bill Young
    # Name: 32
    # Name: bill@example.com

    # Customer ID: customer3
    # Name: Khloe Winton
    # Name: 18
    # Name: kw@example.com