def sum_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result
total = sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Total: {total}")

# output --> Total: 45

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
display_info(name="Bluey", age=82, city="Cordoba")

# output -->
    # name:Bluey
    # age:82
    # city:Cordoba    