class Personnel:
    """ Create the Personnel class with the attributes: name, age, and hourly_rate"""
    def __init__(self, name, age, hourly_rate):
        self.name = name
        self.age = age
        self.hourly_rate = hourly_rate

    def display(self):
        """ Create a method to display Personnel data once an object is instantiated"""
        print(f"This employee's name is {self.name}")
        print(f"This employee's age is {self.age}'")
        print(f"This employee's hourly rate is {self.hourly_rate}'")

# Instantiation of an object of the Personnel class
employee_name = "Bob"
employee_age = 32
employee_hourly_rate = 20
employee = Personnel(name=employee_name, age=employee_age, hourly_rate=employee_hourly_rate)

# Call the display method on the instantiated object
employee.display()

# ouptput --> 
    # This employee's name is Bob
    # This employee's age is 32'
    # This employee's hourly rate is 20'
    # None --> 
    #   resulted from print(employee.display())
    #   to avoid, remove the call to print()
    #   or, return a formatted string from the display method

# returning a formatted string from the display method:
# def display(self):
#         return (f"This employee's name is {self.name}\n"
#                 f"This employee's age is {self.age}'\n"
#                 f"This employee's hourly rate is {self.hourly_rate}'")