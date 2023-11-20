# key-value pairs
# use curly braces and key-value pairs
student1 = {"name": "Janet", "age": 22, "grade": "A"}
print(student1)
# output --> {'name': 'Janet', 'age': 22, 'grade': 'A'}

# dict constructor
# pass key-value pairs as keyword arguments
student2 = dict(name="Jackie", age=18, grade="B")
print(student2)
# output --> {'name': 'Jackie', 'age': 18, 'grade': 'B'}

# zip() function
# combine 2 lists of corresponding elements
keys = ["name", "age", "grade"]
values = ["Josie", 20, "B+"]
student3 = dict(zip(keys, values))
print(student3)
# output --> {'name': 'Josie', 'age': 20, 'grade': 'B+'}