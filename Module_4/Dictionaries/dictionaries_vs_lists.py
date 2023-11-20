# dictionary creation example
# key-value pairs
person = {"name": "John", "age": 18, "city": "London"}
print(person)
# ouptut --> {'name': 'John', 'age': 18, 'city': 'London'}

# accessing a value by key
name = person["name"]
print(name)
# output --> John

# mutability of dictionaries
person["age"] = 26 # modifies previous value
person["city"] = "Chicago"
person["occupation"] = "Waiter" # add a new key-value pair
del person["age"] # remove a key-value pair
print(person, "update")
# output --> {'name': 'John', 'city': 'Chicago', 'occupation': 'Waiter'}

# list creation example 
# sequence
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
# output --> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# accessing a value by index
second_number = numbers[1]
print(second_number)
# output --> 2

# mutability of lists
numbers[0] = 10 # modifying elements
numbers.append(6) # add element to end of list
numbers.remove(3) # remove the element 3 from the list
print(numbers, "update")
# output --> [10, 2, 4, 5, 6, 7, 8, 9, 6]

