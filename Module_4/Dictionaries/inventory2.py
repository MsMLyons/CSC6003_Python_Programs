# Product Inventory
# Create an inventory system to store product details. 
# Implement the following functionalities:
#     Add a product to the inventory with its price and quantity.
#     Retrieve the price and quantity of a given product.
#     Print all products in the inventory.

# initialize dictionary
inventory = {}

# add a product to the inventory
def add_product(product_id, price, quantity):
    inventory[product_id] = {"price": price, "quantity": quantity}

# retrieve price and quantity of a given product
def get_product_details(product_id):
    return inventory.get(product_id)

# print all products in the inventory
def print_inventory():
    for product_id, details in inventory.items():
        print("Product ID:", product_id)
        print("Price:", details['price'])
        print("Quantity:", details['quantity'])
        print()

# usage
add_product("P001", 9.99, 12)
add_product("P002", 12.99, 5)
print(get_product_details("P001"))
print_inventory()

# output -->
    # {'price': 9.99, 'quantity': 12}

    # Product ID: P001
    # Price: 9.99
    # Quantity: 12

    # Product ID: P002
    # Price: 12.99
    # Quantity: 5