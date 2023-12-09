def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]    
    return arr

numbers = [2, 9, 45, 32, 900, 1, 0, 345, 87, 56]

bubble_sort(numbers)
print(f"Sorted list: {numbers}")

# output --> Sorted list: [0, 1, 2, 9, 32, 45, 56, 87, 345, 900]