def enter_data():
    num_students = int(input("Enter the number of students: "))

    for student in range(1, num_students + 1):
        student_name = input("Enter student name: ")
        print(f"Processing student: {student_name}")
enter_data()