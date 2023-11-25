""" 
File: lyonsm_module_5.py
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 5
Date Created: 2023-11-25
Date Updated: 2023-11-27

Description: 

This program begins with the creation of the Personnel class,
which will serve as the parent or super class for child classes
Doctor, Surgeon, and Nurse. 

Each child class inherits the attributes name, age, and hourly
rate and the display method from the Personnel class.

Each child class then builds on those attributes and methods to
add and display information specific to each child class.

Finally, each child class is instantiated to display an example
instance of each object.
"""

class Personnel:
    """ Create the Personnel class with the attributes: name, age, and hourly_rate """
    def __init__(self, name, age, hourly_rate):
        self.name = name
        self.age = age
        self.hourly_rate = hourly_rate

    def display(self):
        """ Create a method to display Personnel attributes once an object is instantiated 
        from a child class 
        """
        return self.name, self.age, self.hourly_rate

class Doctor(Personnel):
    """ Create a child class of the Personnel class called Doctor. The Doctor class inherits 
        attributes and methods from the Personnel class, and adds the new attribute: specialty
    """
    def __init__(self, name, age, hourly_rate, specialty):
        Personnel.__init__(self, name, age, hourly_rate)
        self.specialty = specialty

    def display_doctor(self):
        """ Create a method that inherits from the Personnel.display() method to display 
            the data of an instantiated Doctor object
        """
        Personnel.display(self)
        print(f"\nDr {self.name} is {self.age} years old, makes ${self.hourly_rate} an hour, and their specialty is {self.specialty}.") 
                
class Surgeon(Personnel):
    """ Create a child class of Personnel for Surgeon with inherited attributes and methods. This class 
        also displays the board certification status of the Surgeon object
    """
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
    """ Create a child class of Personnel for Nurse with inherited attributes and methods. This class
        also displays the ranking of the nurse instantiated through the Nurse object
    """
    def __init__(self, name, age, hourly_rate, rank):
        Personnel.__init__(self, name, age, hourly_rate)
        self.rank = rank 

    def display_nurse(self):
        """ Method to display the data of an instantiated nurse object that inherits from 
        Personnel.display() 
        """
        Personnel.display(self)
        print(f"\nNurse {self.name} is {self.age} years old, and makes ${self.hourly_rate} an hour.")
        print(f"Nurse {self.name} is ranked {self.rank} amongst the nursing staff.")

# instantiate a doctor object
new_doctor = Doctor("Alicia", 27, 300, "rheumatology")
new_doctor.display_doctor()

# instatiate a surgeon object
new_surgeon = Surgeon("Patricia", 32, 345)
new_surgeon.display_surgeon()
new_surgeon.board_certification(board_certified=False)

# instantiate a nurse object
new_nurse = Nurse("Thomas", 38, 150, rank="#3")
new_nurse.display_nurse()