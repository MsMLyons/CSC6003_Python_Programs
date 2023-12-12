""" 
File: lyonsm_module_7.py
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 7
Date Created: 2023-12-09
Date Updated: 2023-12-10

Description: The objective of this program is to compare 
two sorting algorithms for their time efficiency in sorting 
a large, randomized, dataset. The sorting algorithms chosen
for this comparison are insertion sort and merge sort.
"""
import random
import timeit
from datetime import datetime


def generate_random_dataset(size):
    """ Function to generate a random dataset """
    return [random.randint(1, 1000000) for _ in range(size)] 

# set the size of the dataset
dataset = generate_random_dataset(900000)

def insertion_sort(arr):
    """ Function to sort a randomized data set by implementing 
        the insertion sort algorithm 
    """
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# set the start and end times, as well as measure the execution time based on
# one set of data
start_time = datetime.now()
insertion_sort_execution_time = timeit.timeit(lambda: insertion_sort(dataset), number = 1)
end_time = datetime.now()

# print the results
print("\n--* Insertion Sort Results *--")
print(f"\nInsertion Sort Beginning Timestamp: {start_time.timestamp()}")
print(f"Insertion Sort took {insertion_sort_execution_time} seconds to run")
print(f"Insertion Sort Ending Timestamp: {end_time.timestamp()}")

def merge_sort(dataset):
    """ Function to sort a dataset by implementing the merge sort algorithm """
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_half = dataset[:mid]
        right_half = dataset[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        return merge(left_half, right_half)
    
def merge(left_half, right_half):
    """ Function to merge sublists of a dataset """
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

# set the start and end times, as well as measure the execution time based on
# one set of data
start_time = datetime.now()
merge_sort_execution_time = timeit.timeit(lambda: merge_sort(dataset), number = 1)
end_time = datetime.now()

# print the results
print("\n--* Merge Sort Results *--")
print(f"\nMerge Sort Beginning Timestamp: {start_time.timestamp()}")
print(f"Merge Sort took {merge_sort_execution_time} seconds to run")
print(f"Merge Sort Ending Timestamp: {end_time.timestamp()}")

if __name__ == "__main__":
    def get_final_result():
        """ Function to print a comparison of the sorting algorithms """
        print("\n--* Comparison of Insertion Sort and Merge Sort *--")
        print(f"\nThe dataset included {len(dataset)} randomly generated numbers.")    
        if insertion_sort_execution_time == merge_sort_execution_time:
            print("Result: Both Insertion Sort and Merge Sort are equally time efficient.")
        elif insertion_sort_execution_time > merge_sort_execution_time:
            print("Result: Insertion Sort is slower than Merge Sort.")
        else:
            print("Result: Insertion Sort is faster than Merge Sort.")
get_final_result()