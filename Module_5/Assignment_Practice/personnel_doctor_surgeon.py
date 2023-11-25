class Personnel:
    """ Create the Personnel class with the attributes: name, age, and hourly_rate"""
    def __init__(self, name, age, hourly_rate):
        self.name = name
        self.age = age
        self.hourly_rate = hourly_rate

    def display(self):
        """ Create a method to display Personnel data once an object is instantiated """
        return self.name, self.age, self.hourly_rate

class Doctor(Personnel):
    """ Create child class of Personnel for Doctor with inherited attributes and methods """
    def __init__(self, name, age, hourly_rate, specialty):
        Personnel.__init__(self, name, age, hourly_rate)
        self.specialty = specialty

    def display_doctor(self):
        """ Create a method that inherits from Personnel.display() to display 
            the data of an instantiated Doctor object
        """
        Personnel.display(self)
        print(f"Dr {self.name} is {self.age} years old, makes ${self.hourly_rate} an hour, and their specialty is {self.specialty}.") 
                
class Surgeon(Personnel):
    """ Create child class of Personnel for Surgeon with inherited attributes and methods """
    def __init__(self, name, age, hourly_rate, board_certified):
        Personnel.__init__(self, name, age, hourly_rate)
        self.board_certified = board_certified    
            
    def display_surgeon(self):
        """ Create a method that inherits from Personnel.display() to display 
            the data of an instantiated Surgeon object
        """
        Personnel.display(self)
        print(f"Dr {self.name} is {self.age} years old, makes ${self.hourly_rate} an hour, {self.board_certified}.")

new_doctor = Doctor("Alicia", 27, 30, "rheumatology")
new_doctor.display_doctor()

new_surgeon = Surgeon("Patricia", 32, 45, board_certified="and they are board certified")
new_surgeon.display_surgeon()