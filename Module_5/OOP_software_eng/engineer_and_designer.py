# parent class
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working hard over here!")

# child class that inherits from Employee
class Software_Engineer(Employee):
    
    # inherit from and override the parent class
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    # override method from parent class
    def work(self):
        print(f"{self.name} is coding the next big thing...")

    # proprietary method for this class
    def debug(self):
        print(f"{self.name} is debugging the code 🐞 🐞 🐞")
        
# child class that inherits from Employee
class Designer(Employee):

    # override method from parent class
    def work(self):
        print(f"{self.name} is designing.")
    
    # proprietary method for this class
    def draw(self):
        print(f"{self.name} is drawing some awesome art for our next project!")        

se = Software_Engineer("Alexia", 32, 125000, "Mid-Level")
print(se.name, se.age)
se.work()
se.debug()

des = Designer("Mariana", 28, 95000)
print(des.name, des.age)
des.work()
des.draw()

print()
print("~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~")
print()

# polymorphism
employees = [Software_Engineer("Alexia", 32, 125000, "Mid-Level"),
            Software_Engineer("Alexander", 29, 75000, "Junior"),
            Designer("Max", 23, 65000)]

def motivate_employees(employees):
    for employee in employees:
        employee.work()
        print(f"Good work!")
motivate_employees(employees)