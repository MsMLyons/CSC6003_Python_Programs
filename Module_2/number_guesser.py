import random

def number_guesser():
    target_number = random.randint(1, 10)
    guess = 0       
    
    while True:
        user_guess = int(input("Enter a number from 1 - 10: "))
        print()
        guess += 1
        print(f"Total guesses: {guess} \n")
        
        if user_guess > target_number:
            print(f"Too high. Guess a number lower than {user_guess}.")
            
        if user_guess < target_number:
            print(f"Too low. Guess a number greater than {user_guess}.")
            
        if user_guess == target_number:            
            print("You guessed it!")            
            break        

number_guesser()