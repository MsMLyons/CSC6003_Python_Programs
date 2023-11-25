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

class Doctor(Personnel):
    """ Create child class of Personnel with inherited attributes and methods """
    def __init__(self, name, age, hourly_rate, specialty):
        Personnel.__init__(self, name, age, hourly_rate)
        self.specialty = specialty

    def display_doctor(self):
        Personnel.display(self)
        print(f"This doctor's specialty is {self.specialty}")

new_doctor = Doctor("Dr Alicia", 27, 30, "rheumatology")
new_doctor.display_doctor()

# output -->
    # This employee's name is Dr Alicia
    # This employee's age is 27'
    # This employee's hourly rate is 30'
    # This doctor's specialty is rheumatology