# Employee Database
# Create an employee database to store employee details. 
# Implement the following functionalities:
#     Add an employee to the database with their name, designation, and salary.
#     Retrieve the designation and salary of a given employee.
#     Print all employees in the database.

# initialize dictionary
employee_db = {}

# add an employee to the database
def add_employee(emp_id, name, designation, salary):
    employee_db[emp_id] = {"name": name, "designation": designation, "salary": salary}

# retrieve designation and salary of a given employee
def get_employee_details(emp_id):
    return employee_db.get(emp_id)

# print all employees in the database
def print_employees():
    for emp_id, details in employee_db.items():
        print("Employee ID:", emp_id)
        print("Name:", details['name'])
        print("Designation:", details['designation'])
        print("Salary:", details['salary'])
        print()

# usage
add_employee("E001", "Luca Lorini", "Product Manager", 85000)
add_employee("E002", "Silvia Sarkar", "Engineer", 175000)
print(get_employee_details("E002"))
print_employees()

# output --> 
    # {'name': 'Silvia Sarkar', 'designation': 'Engineer', 'salary': 175000}

    # Employee ID: E001
    # Name: Luca Lorini
    # Designation: Product Manager
    # Salary: 85000

    # Employee ID: E002
    # Name: Silvia Sarkar
    # Designation: Engineer
    # Salary: 175000