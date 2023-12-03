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

    # instance methods
    def code(self):
        print(f"Please don't disturb {self.name}, whose in a state of flow and writing code...\n") 

    def code_in_language(self, language):
        print(f"{self.name} prefers coding in {language}.")    

    # dunder method
    def __str__(self):
        information = f"\nname = {self.name}, position = {self.position}, age = {self.age}, level = {self.level}, salary = {self.salary}" 
        return information
    
    # compares memory address
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    # decorators
    @staticmethod
    def starting_salary(age):
        if age <= 25:
            return 65000
        elif age < 30:
            return 100000
        else:
            return 125000
        
    
software_engineer1 = Software_Engineer("Software Engineer", "Max", 20, "Junior", 68000)
software_engineer2 = Software_Engineer("Software Engineer", "Elisa", 28, "Senior", 128000)
software_engineer3 = Software_Engineer("Software Engineer", "Lisa", 32, "Senior", 150000)
print(software_engineer1)
print(f"{software_engineer1.name}'s starting salary was {software_engineer1.starting_salary(20)}.")
print(software_engineer2)
print(f"{software_engineer2.name}'s starting salary was {software_engineer2.starting_salary(28)}.")
print(software_engineer3)
print(software_engineer3.starting_salary(32))
print(f"{software_engineer3.name}'s starting salary was {software_engineer3.starting_salary(32)}.")
print(software_engineer2 == software_engineer3)