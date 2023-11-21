# Inventory Management
# Build an inventory management system that tracks
# products in stock. Each product is represented by a tuple
# containing its name, quantity available, and price.

# initialize inventory list
inventory = []

# add a product to inventory
def add_product(name, quantity, price):
    product = (name, quantity, price)
    inventory.append(product)

# update quantity of a product
def update_quantity(product_name, new_quantity):
    for i in range(len(inventory)):
        if inventory[i][0] == product_name:
            product = inventory[i]
            inventory[i] = (product[0], new_quantity, product[2])
            break

# print all products in inventory
def print_inventory():
    print("Inventory:")
    for product in inventory:
        print("Name:", product[0])
        print("Quantity:", product[1])
        print("Price:", product[2])
        print()

# usage
add_product("Widget A", 10, 20)
add_product("Widget B", 5, 15)
update_quantity("Widget A", 15)
print_inventory()

# output -->
    # Inventory:
    # Name: Widget A
    # Quantity: 15
    # Price: 20

    # Name: Widget B
    # Quantity: 5
    # Price: 15