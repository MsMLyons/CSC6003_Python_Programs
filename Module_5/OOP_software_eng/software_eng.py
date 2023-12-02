# blueprint for software engineer
# position, name, age, level, salary - attributes
class Software_Engineer:

    # class attribute
    alias = "Keyboard Slayer"

    # initialize object
    def __init__(self, position, name, age, level, salary):

        # instance attributes
        self.position = position
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary    

# instances of the Software_Engineer class (objects)
# give specific data pertaining to each object
software_engineer1 = Software_Engineer("Software Engineer", "Max", 20, "Junior", 68000)
software_engineer2 = Software_Engineer("Software Engineer", "Elisa", 28, "Senior", 128000)
print(software_engineer1.alias)
print(software_engineer1.name, software_engineer1.position, software_engineer1.age, software_engineer1.level, software_engineer1.salary)
print(software_engineer2.name, software_engineer2.position, software_engineer2.age, software_engineer2.level, software_engineer2.salary)
print(f"All of these software engineers belong to the exclusive {Software_Engineer.alias} hacking group")