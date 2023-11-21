def sum_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")