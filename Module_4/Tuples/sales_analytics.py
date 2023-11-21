# Sales Analytics
# Create a sales analytics system that tracks sales
# information for different products. Each product is
# represented by a tuple containing its name, quantity sold,
# and total revenue.

# initialize list
sales_data = []

# add sales data for a product
def add_sales_data(product_name, quantity_sold, revenue):
    product_data = (product_name, quantity_sold, revenue)
    sales_data.append(product_data)

# calculate total revenue for a product
def calculate_total_revenue(product_data):
    return product_data[1] * product_data[2]

def print_highest_revenue_product():
    highest_revenue = 0
    highest_product = None

    for product_data in sales_data:
        revenue = calculate_total_revenue(product_data)
        if revenue > highest_revenue:
            highest_revenue = revenue
            highest_product = product_data

    if highest_product:
        print("Product with highest revenue:")
        print("Name:", highest_product[0])
        print("Quantity Sold:", highest_product[1])
        print("Total Revenue:", highest_revenue)

# usage
add_sales_data("Widget A", 100, 10)
add_sales_data("Widget B", 50, 21)
print_highest_revenue_product()

# output --> 
    # Product with highest revenue:
    # Name: Widget B
    # Quantity Sold: 50
    # Total Revenue: 1050