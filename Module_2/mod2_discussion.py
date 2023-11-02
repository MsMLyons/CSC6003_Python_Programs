def count_back():
    ''' Function to count backward by 5, from 50 - 25 '''    
    for num in range(50, 20, -5):
        print(num)
count_back()

def read_string():
    ''' 
    Function to read a string input from keyboard
    until the user types "exit"
    '''
    
    while True:        
        user_input = str(input("Enter a nice message or type \"Exit\": \n"))
        if user_input.lower() == "exit":
            break
        else:
            continue
read_string()