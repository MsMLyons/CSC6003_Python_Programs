import timeit

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

numbers = [2, 9, 45, 32, 900, 1, 0, 345, 87, 56]

execution_time = timeit.timeit(lambda: bubble_sort(numbers), number = 1)
print(f"\nBubble sort execution time: {execution_time} seconds")

print(f"Sorted list: {numbers}")