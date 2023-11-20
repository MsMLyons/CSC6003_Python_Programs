student = {
    "name": "Janet", 
    "age": 22, 
    "grade": "A"
}

# iterate over keys
for key in student:
    print("These are the keys:", key)
# output -->
    # These are the keys: name
    # These are the keys: age
    # These are the keys: grade


# iterate over values
for value in student.values():
    print("These are the values:", value)
# output -->
    # These are the values: Janet
    # These are the values: 22
    # These are the values: A

# iterate over key-value pairs
for key, value in student.items():
    print("These are the keys and values:", key, "=", value)
# output -->
    # These are the keys and values: name = Janet
    # These are the keys and values: age = 22
    # These are the keys and values: grade = A