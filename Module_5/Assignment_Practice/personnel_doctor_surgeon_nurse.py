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
        print(f"\nDr {self.name} is {self.age} years old, makes ${self.hourly_rate} an hour, and their specialty is {self.specialty}.") 
                
class Surgeon(Personnel):
    """ Create child class of Personnel for Surgeon with inherited attributes and methods """
    def __init__(self, name, age, hourly_rate):
        Personnel.__init__(self, name, age, hourly_rate)        

    def board_certification(self, board_certified):
        """ Method to display board certification status of the surgeon """
        if board_certified == True:            
            print(f"Dr {self.name} is board certified.")
        else: 
            print(f"Dr {self.name} is not board certified.")
    
    def display_surgeon(self):
        """ Method to display the data of an instantiated surgeon object
            that inherits from Personnel.display()        
        """
        Personnel.display(self)
        print(f"\nDr {self.name} is {self.age} years old, and makes ${self.hourly_rate} an hour.")

class Nurse(Personnel):
    """ Create child class of Personnel for Nurse with inherited attributes and methods """
    def __init__(self, name, age, hourly_rate, rank=0):
        Personnel.__init__(self, name, age, hourly_rate)
        self.rank = rank 

    def display_nurse(self):
        """ Method to display the data of an instantiated nurse object
            that inherits from Personnel.display()        
        """
        Personnel.display(self)
        print(f"\nNurse {self.name} is {self.age} years old, and makes ${self.hourly_rate} an hour.")
        print(f"Nurse {self.name} is ranked #{self.rank} amongst the nursing staff.")

new_doctor = Doctor("Alicia", 27, 300, "rheumatology")
new_doctor.display_doctor()

new_surgeon = Surgeon("Patricia", 32, 345)
new_surgeon.display_surgeon()
new_surgeon.board_certification(board_certified=False)

new_nurse = Nurse("Thomas", 38, 150, rank=3)
new_nurse.display_nurse()