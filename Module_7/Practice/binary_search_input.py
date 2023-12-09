import timeit

def binary_search(numbers, target):
    low = 0
    high = len(numbers) -1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else: 
            high = mid -1

    return -1

dataset = list(range(100000000))
target = int(input("Enter the target number to search: "))

execution_time = timeit.timeit(lambda: binary_search(dataset, target), number = 10000)
print(f"Binary search took {execution_time} seconds")

# input/output -->
    # Enter the target number to search: 9035782
    # Binary search took 0.03364849998615682 seconds