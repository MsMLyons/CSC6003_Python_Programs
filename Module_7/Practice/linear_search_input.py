import timeit

def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1

large_dataset = list(range(10000000))

target = int(input("Enter the target number to search: "))

execution_time = timeit.timeit(lambda: linear_search(large_dataset, target), number = 1)
print(f"Linear search execution time: {execution_time} seconds")

# input/output --> 
    # Enter the target number to search: 368920
    # Linear search execution time: 0.015246100025251508 seconds