def student_grade():
    score = int(input("Please enter your score 0 - 100: "))
    if 90 <= score <= 100:
        print("You have an A")
    elif 80 <= score <= 89:
        print("You have a B")
    elif 70 <= score <= 79:
        print("You have a C")
    elif 60 <= score <= 69:
        print("You have a D")
    else:
        print("You have an F")
student_grade()