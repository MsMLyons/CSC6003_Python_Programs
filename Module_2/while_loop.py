# Using a do-while loop, write a code fragment that reads a String 
# from the keyboard from the user until the user types “EXIT”

def read_string():
    while True:        
        user_input = str(input("Enter a nice message or type \"Exit\": \n"))
        if user_input.lower() == "exit":
            break
        else:
            continue
read_string()

