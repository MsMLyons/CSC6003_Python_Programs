# extracting values from a dictionary

sales_record = {"price": 3.24, "num_items": 4, "client": "Jennifer"}
sales_statement = "{} bought {} item(s) at a price of {} each for a total of {}"
print(sales_statement.format(sales_record["client"], 
                            sales_record["num_items"], 
                            sales_record["price"], 
                            (sales_record["num_items"] * sales_record["price"])))
# output --> Jennifer bought 4 item(s) at a price of 3.24 each for a total of 12.96

# streamlined
sales_record = {"price": 6.18, "num_items": 3, "client": "Lola"}
total_price = sales_record["num_items"] * sales_record["price"]
sales_statement = "{} bought {} item(s) at a price of {} each for a total of {}"
print(sales_statement.format(sales_record["client"], 
                            sales_record["num_items"], 
                            sales_record["price"], 
                            total_price))
# output --> Lola bought 3 item(s) at a price of 6.18 each for a total of 18.54


