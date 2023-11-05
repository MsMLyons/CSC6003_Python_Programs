def sum_evens():
    total = 0

    for num in range(2, 101, 2):
        total += num
    print(f"The sum of even numbers from 1 to 100 is: {total}")

sum_evens()