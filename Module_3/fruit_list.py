my_fruits = []
my_fruits.append('apple')
my_fruits.append('banana')
my_fruits.append('orange')
print(my_fruits)
# output --> ['apple', 'banana', 'orange']

# clear list of my_fruits
my_fruits.clear()
print(my_fruits)
# output --> []

# append a new list of fruits to my_fruits
new_fruits = ['apple', 'banana', 'orange']
my_fruits.append(new_fruits)
print(my_fruits)
# output --> [['apple', 'banana', 'orange']]

# print the value at the indicated index of the list
print(new_fruits[0])
print(new_fruits[1])
print(new_fruits[2])
# output --> apple
# output --> banana
# output --> orange

# modify an element in the list
new_fruits[1] = "grape"
print(new_fruits)
# output --> ['apple', 'grape', 'orange']

# add another fruit to the list
new_fruits.append("kiwi")
new_fruits.append("pineapple")
print(new_fruits)
# output --> ['apple', 'grape', 'orange', 'kiwi', 'pineapple']

# get length of list
print(len(new_fruits))
# output --> 5

# sort the list
new_fruits.sort()
print(new_fruits)
# output --> ['apple', 'grape', 'kiwi', 'orange', 'pineapple']

# slicing a list
print(new_fruits[1:4])
# output --> ['grape', 'kiwi', 'orange']

# slicing with a step
# start at index 0, skip to index 2, skip to index 4
# elements: first, third, fifth
print(new_fruits[::2])
# output --> ['apple', 'kiwi', 'pineapple']

# make a new list
best_fruits = new_fruits[::2]
print(best_fruits)
# output --> ['apple', 'kiwi', 'pineapple']

# concatenation
best_vegetables = ["green beans", "broccoli"]
combined = best_fruits + best_vegetables
print(combined)
# output --> ['apple', 'kiwi', 'pineapple', 'green beans', 'broccoli']

# iterating over a list with a for loop
for fruit in best_fruits:
    print(fruit)
# output --> apple
#            kiwi
#            pineapple

# list membership testing
print("banana" in best_fruits)
# output --> False 
print("kiwi" in best_fruits)
# output --> True