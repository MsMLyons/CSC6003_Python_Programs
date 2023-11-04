def access_account():
    user_name = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if user_name == "admin" and password == "password123":
        print("Access granted")
    else:
        print("Access denied")

access_account()