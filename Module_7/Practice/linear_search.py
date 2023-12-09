import timeit

def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1

numbers = [4, 2, 8, 6, 10]
target = 8

execution_time = timeit.timeit(lambda: linear_search(numbers, target), number = 100000)
print(f"Linear search execution time: {execution_time} seconds")

# output --> Linear search execution time: 0.030893299961462617 seconds