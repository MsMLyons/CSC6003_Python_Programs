# import randint
import timeit
from datetime import datetime

date_time = datetime.now()

time_stamp = datetime.timestamp(date_time)
mili_time_stamp = date_time.timestamp() * 1000

dataset = list(range(10000000))

print("\nTarget value: 45678493")

print("\n--* Binary Search Results *--")
print(f"\nBinary Search Beginning Timestamp: {time_stamp}")
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
# target = int(input("Enter the target number to search: "))
target = 45678493

execution_time = timeit.timeit(lambda: binary_search(dataset, target), number = 10000)
print(f"Binary search took {execution_time} seconds")

print(f"Binary Search Ending Timestamp (miliseconds): {mili_time_stamp}")

