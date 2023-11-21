# tuple methods and operations

# creating a tuple
fruits = ("apple", "orange", "grapes")

# accessing and slicing tuple elements
print(fruits[0])
print(fruits[1:3])

# output -->
    # apple
    # ('orange', 'grapes')


# tuple unpacking
a, b, c = fruits
print(a, b, c)

# output --> apple orange grapes


# sorting tuples
sorted_fruits = sorted(fruits)
print(sorted_fruits, "me")

# output --> ['apple', 'grapes', 'orange']


# counting occurrences of an element in a tuple
print(fruits.count("grapes"))

# output --> 1


# finding the index of an element in a tuple
print(fruits.index("apple"))

# output --> 0


# concatenating tuples
colors = ("green", "orange", "purple")
combined = fruits + colors
print(combined)

# output --> ('apple', 'orange', 'grapes', 'green', 'orange', 'purple')


# checking membership in a tuple
print("grapes" in fruits)
print("banana" in fruits)

# output --> True, False


# finding the length of a tuple
print(len(fruits))

# output --> 3


# unpacking a tuple
x, y, z = colors
print(x)
print(y)
print(z)

# output -->
    # green
    # orange
    # purple

# iterating over a tuple
combined_fruits_colors = [("apple", "green"), ("orange", "orange"), ("grapes", "purple")]
for fruit , color in combined_fruits_colors:
    print("Fruit:", fruit, "Color:", color)

# output -->
    # Fruit: apple Color: green
    # Fruit: orange Color: orange
    # Fruit: grapes Color: purple

# tuple packing
summer_fruits = "watermelon", "strawberries", "mangoes"

# accessing the packed tuple
print(summer_fruits)

# output --> ('watermelon', 'strawberries', 'mangoes')

