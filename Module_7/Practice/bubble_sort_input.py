import timeit

# bubble sort takes in an array
def bubble_sort(arr):

    # assign the length of the array to variable n
    n = len(arr)

    # iterate over the array; n - 1 is the last element in the array
    for i in range(n - 1):
        # create a second range to compare elements
        for j in range(n - i - 1):
            # compare elements
            if arr[j] > arr [j + 1]:
                # swap positions depending on the comparison outcome
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# prompt for user input
number_list = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, number_list.split()))

# input / output --> 
    # Enter a list of numbers separated by spaces: 77 902 4 10002 56 294 0 32 1 64 833 96
    # Bubble Sort Execution Time: 1.3200100511312485e-05 seconds
    # Sorted List: [0, 1, 4, 32, 56, 64, 77, 96, 294, 833, 902, 10002]

# measure execution time
execution_time = timeit.timeit(lambda: bubble_sort(numbers), number = 1)
print(f"Bubble Sort Execution Time: {execution_time} seconds")

print(f"Sorted List: {numbers}")