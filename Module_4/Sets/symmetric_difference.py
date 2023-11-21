# option 1
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

symmetric_difference_result = set1.symmetric_difference(set2)
print(symmetric_difference_result)

# output --> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# option 2
set3 = {11, 12, 13, 14, 15}
set4 = {16, 17, 18, 19, 20}

symmetric_diff_result = set3 ^ set4
print(symmetric_diff_result)

# ouptut --> {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}