def password_check():
    password = 'pw123'
    attempts = 3

    while attempts >= 1:
        user_input = input("Please enter your password: ")
        if user_input != password:
            attempts -= 1
            print(f"You have {attempts} attempts remaining")
            if attempts == 0:
                print("Your password must be reset")
                break  
        else:
            print("Access granted")
            break  

password_check()
