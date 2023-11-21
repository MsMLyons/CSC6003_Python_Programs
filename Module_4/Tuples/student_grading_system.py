# Student Grading System
# Implement a student grading system that stores student
# details along with their scores for different subjects. Use
# tuples to represent each student's information.

# initialize students list
students = []

# add a student name and scores
def add_student(name, scores):
    student = (name, scores)
    students.append(student)

# calculate the average score for a student
def calculate_average_score(student):
    scores = student[1]
    total = sum(scores)
    average = total / len(scores)
    return average

# print the student with the highest average score
def print_highest_scoring_student():
    highest_average = 0
    highest_student = None

    for student in students:
        average = calculate_average_score(student)
        if average > highest_average:
            highest_average = average
            highest_student = student

    if highest_student:
        print("Highest Scoring Student:")
        print("Name:", highest_student[0])
        print("Average Score:", highest_average)

# usage
add_student("Johe Dohe", [85, 90, 77])
add_student("Anna Banda", [95, 92, 99])
print_highest_scoring_student()

# output --> 
    # Highest Scoring Student:
    # Name: Anna Banda
    # Average Score: 95.33333333333333
