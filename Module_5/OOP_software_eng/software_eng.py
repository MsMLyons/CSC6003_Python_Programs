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
        print(f"Please don't disturb {self.name}. \nHe's in a state of flow, writing code...\n") 

    def code_in_language(self, language):
        print(f"{self.name} prefers coding in {language}.")

    def planning_exploits(self):
        print(f"Please don't disturb {self.name}. \nShe's our mastermind and is busy planning our next zero day exploit.\n")

    def secret_information(self):
        secret_information = f"{self.name}'s salary is {self.salary} a year. \nThis is secret information, so don't share it!\n" 
        return secret_information

# instances of the Software_Engineer class (objects)
# give specific data pertaining to each object
software_engineer1 = Software_Engineer("Software Engineer", "Max", 20, "Junior", 68000)
software_engineer2 = Software_Engineer("Software Engineer", "Elisa", 28, "Senior", 128000)
print("\nGet to know our engineers.\n")
print(f"{software_engineer1.name} is a {software_engineer1.position}. \nHe's {software_engineer1.age} and is a {software_engineer1.level} engineer.")
print(software_engineer1.secret_information())
software_engineer1.code_in_language("Python")
print(f"{software_engineer1.name} is a {Software_Engineer.alias}.")
software_engineer1.code()
print(f"{software_engineer2.name} is a {software_engineer2.position}. \nShe's {software_engineer2.age} and is a {software_engineer2.level} engineer.")
print(software_engineer2.secret_information())
software_engineer2.code_in_language("Java")
software_engineer2.planning_exploits()
print(f"\nThese software engineers belong to the exclusive {Software_Engineer.alias} hacking group. \nShhhh... don't tell anyone lest they come after you.")