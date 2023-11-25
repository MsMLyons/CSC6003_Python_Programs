class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_name(self):
        return self.name
    
    def get_grade(self):
        return self.grade
    
new_student = Student("Anna", "A")
print("The new student's name is:", new_student.get_name(), "and her grade is:", new_student.get_grade())

# output -->
#   The new student's name is: Anna and her grade is: A