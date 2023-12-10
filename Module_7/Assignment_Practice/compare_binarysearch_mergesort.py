import random
import timeit
from datetime import datetime


def generate_random_dataset(size):
    return [random.randint(1, 10000000) for _ in range(size)] 

def get_random_target(dataset):
    return random.choice(dataset)

dataset = generate_random_dataset(10000000)
target = get_random_target(dataset)

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

start_time = datetime.now()
execution_time = timeit.timeit(lambda: binary_search(dataset, target), number = 1)
end_time = datetime.now()

print("\n--* Binary Search Results *--")
print(f"\nBinary Search Beginning Timestamp: {start_time.timestamp()}")
print(f"Binary search took {execution_time} seconds")
print(f"Binary Search Ending Timestamp: {end_time.timestamp()}")

def merge_sort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_half = dataset[:mid]
        right_half = dataset[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        return merge(left_half, right_half)
    
def merge(left_half, right_half):
    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged

start_time = datetime.now()
execution_time = timeit.timeit(lambda: merge_sort(dataset), number = 1)
end_time = datetime.now()

print("\n--* Merge Sort Results *--")
print(f"\nMerge Sort Beginning Timestamp: {start_time.timestamp()}")
print(f"Merge Sort took {execution_time} seconds")
print(f"Merge Sort Ending Timestamp: {end_time.timestamp()}")