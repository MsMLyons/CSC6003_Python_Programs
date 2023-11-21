# inventory database
inventory = {
    "product1" : {"name": "Product A", "quantity": 10, "price": 9.99},
    "product2" : {"name": "Product B", "quantity": 5, "price": 12.99},
    "product3" : {"name": "Product C", "quantity": 3, "price": 15.99}
}

# accessing product information
product_id = "product2"
product_info = inventory.get(product_id)
if product_info:
    print("Product Name:", product_info["name"])
    print("Quantity:", product_info["quantity"])
    print("Price:", product_info["price"])
else:
    print("Sorry. Product not found.")

# output -->
    # Product Name: Product B
    # Quantity: 5
    # Price: 12.99