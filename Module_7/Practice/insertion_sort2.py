import timeit

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

numbers = [7, 2, 5, 1, 8, 3]

execution_time = timeit.timeit(lambda: insertion_sort(numbers), number = 1)
print(f"Insertion sort execution time: {execution_time} seconds")

print(f"Sorted list: {numbers}")

# output --> 
    # Insertion sort execution time: 7.899943739175797e-06 seconds
    # Sorted list: [1, 2, 3, 5, 7, 8]