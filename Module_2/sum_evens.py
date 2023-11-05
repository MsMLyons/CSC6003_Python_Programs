def sum_evens():
    num_list = []
    Sum = 0

    for i in range(1, 101):
        if i % 2 == 0:
            num_list.append(i)
            Sum += i
    
    print(f"The sum of all even numbers from 1 - 100 is: {Sum}")

sum_evens()