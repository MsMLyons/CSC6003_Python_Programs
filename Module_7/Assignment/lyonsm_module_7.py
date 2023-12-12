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
from datetime import datetime

def generate_random_dataset(size):
    """ Function to generate a random dataset """
    return [random.randint(1, 1000000) for _ in range(size)] 

# set the size of the dataset for use in the insertion sort algorithm
# note: change the parameter to another value to test larger or 
# smaller datasets
dataset = generate_random_dataset(100000)
# create a copy of the dataset for use in the merge sort algorithm
dataset_2 = dataset.copy()

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

def get_insertion_sort_results():
    # print the results
    print("\n--* Insertion Sort Results *--")
    print(f"\nInsertion Sort Beginning Timestamp: {start_time_insertion_sort}")
    print(f"Insertion Sort Ending Timestamp: {end_time_insertion_sort}")
    print(f"Insertion Sort Runtime in Milliseconds: {insertion_sort_execution_time}")    

def merge_sort(dataset_2):
    """ Function to sort a dataset by implementing the merge sort algorithm """
    if len(dataset_2) > 1:
        mid = len(dataset_2) // 2
        left_half = dataset_2[:mid]
        right_half = dataset_2[mid:]

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

def get_merge_sort_results():
    # print the results
    print("\n--* Merge Sort Results *--")
    print(f"\nMerge Sort Beginning Timestamp: {start_time_merge_sort}")
    print(f"Merge Sort Ending Timestamp: {end_time_merge_sort}")
    print(f"Merge Sort Runtime in Milliseconds: {merge_sort_execution_time}")       

def get_final_result():
    """ Function to print a comparison of the sorting algorithms """
    print("\n--* Comparison of Insertion Sort and Merge Sort *--")
    print(f"\nThe dataset and its copy included {len(dataset)} randomly generated numbers.")    
    if insertion_sort_execution_time == merge_sort_execution_time:
        print("Result: Both Insertion Sort and Merge Sort are equally time efficient.")
    elif insertion_sort_execution_time > merge_sort_execution_time:
        print("Result: Insertion Sort is slower than Merge Sort.")
    else:
        print("Result: Insertion Sort is faster than Merge Sort.")


if __name__ == "__main__":
    # set the start and end times, as well as measure the execution time 
    start_time_insertion_sort = datetime.now()
    insertion_sort(dataset)
    end_time_insertion_sort = datetime.now()
    insertion_sort_execution_time = (end_time_insertion_sort - start_time_insertion_sort).total_seconds()

    start_time_merge_sort = datetime.now()
    merge_sort(dataset_2)
    end_time_merge_sort = datetime.now()
    merge_sort_execution_time = (end_time_merge_sort - start_time_merge_sort).total_seconds()

    get_insertion_sort_results()
    get_merge_sort_results()
    get_final_result()