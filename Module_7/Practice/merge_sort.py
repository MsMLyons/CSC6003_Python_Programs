import timeit

def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left_half = numbers[:mid]
        right_half = numbers[mid:]

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

numbers = [7, 2, 5, 1, 8, 3]

execution_time = timeit.timeit(lambda: merge_sort(numbers), number = 1)
print(f"Merge sort execution time: {execution_time} seconds")

print(f"Sorted list: {numbers}")

# output -->
    # Merge sort execution time: 1.8999911844730377e-05 seconds
    # Sorted list: [7, 2, 5, 1, 8, 3]
