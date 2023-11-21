# create and retrieve data about a person

def get_person_details():
    name = "Layla Endragon"
    age = 25
    city = "San Francisco"
    # return data as a tuple
    return name, age, city

# call the function and store the returned tuple
person = get_person_details()

# access the tuple elements
print(person[0])
print(person[1])
print(person[2])

# output -->
    # Layla Endragon
    # 25
    # San Francisco