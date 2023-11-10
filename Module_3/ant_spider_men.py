# assign strings to variables
h1 = "Antman"
h2 = "Spiderman"

# get value at index position 3
print(h1[3])
# output --> m

# get value at index position 3
print(h2[5])
# output --> r

# slice and get values up to, but not including, index position 3
print(h1[:3])
# output --> Ant

# slice and get values from index position 6 to the end of the string
print(h2[6:])
# output --> man

# slice and get values from index position 4 up to, but not including, 8
print(h2[4:8])
# output --> erma

# slice and get values from index position 2 up to, but not including, 4
print(h1[2:4])
# output --> tm

# get length of value stored in variable h1
print(len(h1))
# output --> 6

# get length of value stored in variable h2
print(len(h2))
# output --> 9

# get values stored at index position 2 up to, but not including, 4, 
# then repeat them 3 times
print(h1[2:4] * 3)
# output --> tmtmtm

# concatenate sliced elements from variables h1 & h2 and
# assign to a new variable to store the new data
animal_heroes = h1[:3] + " and " + h2[:6] + " Men"
print(animal_heroes)
# output --> Ant and Spider Men

# get length of the new string
print(len(animal_heroes))
# output --> 18