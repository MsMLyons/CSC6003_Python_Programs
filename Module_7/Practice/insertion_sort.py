def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

numbers = [7, 2, 5, 1, 9, 3]
insertion_sort(numbers)
print(numbers)

# output --> [1, 2, 3, 5, 7, 9]