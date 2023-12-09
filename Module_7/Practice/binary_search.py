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

numbers = [2, 4, 6, 8, 10]
target = 8

execution_time = timeit.timeit(lambda: binary_search(numbers, target), number = 10000)
print(f"Binary search took {execution_time} seconds")

# output --> Binary search took 0.0029920998495072126 seconds