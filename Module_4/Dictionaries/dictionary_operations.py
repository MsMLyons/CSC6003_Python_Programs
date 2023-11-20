# create a dictionary
student = {
    "name": "Janet", 
    "age": 22, 
    "grade": "A"
}


# accessing values using keys
print(student["name"])
# output --> Janet
print(student.get("grade"))
# output --> A


# modifying values
student["age"] = 21
student["grade"] = "A+"
print(student, "update 1")
# ouptut --> {'name': 'Janet', 'age': 21, 'grade': 'A+'} update 1


# adding new key-value pairs
student["city"] = "New York City"
print(student, "update 2")
# ouptut --> {'name': 'Janet', 'age': 21, 'grade': 'A+', 'city': 'New York City'} update 2


# removing key-value pairs
del student["grade"]
print(student, "update 3")
# ouptut --> {'name': 'Janet', 'age': 21, 'city': 'New York City'} update 3


# checking if a key exists
print("age" in student)
# ouptut --> True
print("grade" in student)
# ouptut --> False


# getting all keys and values
keys = student.keys()
values = student.values()
print(keys)
# ouptut --> dict_keys(['name', 'age', 'city'])
print(values)
# ouptut --> dict_values(['Janet', 21, 'New York City'])


# iterating over keys and values
for key in student:
    print(key, "=", student[key])
# ouptut --> 
    # name = Janet
    # age = 21
    # city = New York City


# getting the length of the dictionary
print(len(student))
# ouptut --> 3


# removing all key-value pairs
student.clear()
print(student, "update 4")
# ouptut --> {} update 4 (empty dictionary)