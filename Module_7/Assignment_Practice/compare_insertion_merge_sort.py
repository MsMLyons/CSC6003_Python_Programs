import random
import timeit
from datetime import datetime


def generate_random_dataset(size):
    return [random.randint(1, 100000) for _ in range(size)] 

dataset = generate_random_dataset(100000)

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

start_time = datetime.now()
execution_time = timeit.timeit(lambda: insertion_sort(dataset), number = 1)
end_time = datetime.now()

print("\n--* Insertion Sort Results *--")
print(f"\nInsertion Sort Beginning Timestamp: {start_time.timestamp()}")
print(f"Insertion Sort took {execution_time} seconds to run")
print(f"Insertion Sort Ending Timestamp: {end_time.timestamp()}")

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
print(f"Merge Sort took {execution_time} seconds to run")
print(f"Merge Sort Ending Timestamp: {end_time.timestamp()}")