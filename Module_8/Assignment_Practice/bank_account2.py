import datetime as datetime
import random

# Create a BankAccount class with the following attributes: account_number, balance
class BankAccount:
    """ Class to assign an account number and to implement methods of
    depositing, withdrawing, checking balance, and displaying account 
    details
    """

    def __init__(self, account_number=None, balance=0.0):               
        self.account_number = int(account_number)
        self.balance = float(balance)             

# Create a Bank class that manages a list of bank accounts
class Bank():
    """ Class to create an account with an initial balance input by the user,
    assigned to a unique account number, as well as allow for transactions.     
    """

    def __init__(self, initial_deposit=0.0):
        self.account_numbers = set()
        self.account_objects = {}
        self.initial_deposit = initial_deposit # created to avoid attribute error               

    # create_account: Prompts the user to enter an initial balance and creates a new bank account 
    # with a unique account number.
    def create_account(self):
        """ Take an account number as input and return the corresponding 
            BankAccount object from the list of accounts """ 
                        
        initial_deposit = float(input("How much would you like to deposit? $"))        
        
        while True: 
            account_number = random.randint(1000000, 100000000)
            if account_number not in self.account_objects:
                self.account_numbers.add(account_number)
                new_account = BankAccount(account_number, initial_deposit)
                self.account_objects[account_number] = new_account               
                
                print(f"\nAccount number {account_number} created successfully")
                print(f"Balance: ${initial_deposit:.2f}")
            # unit testing?
            return new_account
        
    # added to view set of accounts created (not in assignment instructions)        
    def get_all_accounts(self):
        # all_accounts = self.account_numbers        
        # print("Here is a list of all of the accounts:", *all_accounts, sep = "\n")
        print("Here is a list of all of the accounts with their corresponding balances:\n")
        for account_number, account_object in self.account_objects.items():
            print(f"Account number: {account_number}, Balance: {account_object.balance:.2f}")                          
    
    # helper function - does not appear on menu
    def get_account(self, account_number):        
        if account_number in self.account_objects:
            return self.account_objects[account_number]
        else: 
            return False

    # get_account: Takes an account number as input and returns the corresponding BankAccount 
    # object from the list of accounts.
    def get_account_balance(self):
        account_number = int(input("To check a balance, please enter the account number: "))
        if account_number in self.account_objects:
            # account = self.account_objects[account_number]
            print(f"Account number {account_number} has a balance of ${self.account_objects[account_number].balance:.2f}")
        else:
            print("That account number does not exist")     
    
    def deposit(self):
        """ Take an account number and amount as input and deposit the specified 
            amount into the account """
        account = self.get_account(int(input("Please enter your account number: ")))
        if account:
            amount = float(input("Please enter the amount you would like to deposit: $")) 
            account.balance += amount
            timestamp = datetime.datetime.now()
            time_of_deposit = timestamp.strftime("%m/%d/%Y at %H:%M:%S")            
            print(f"Thank you. Deposit of ${amount:.2f} received on: {time_of_deposit}.")
            
        else: 
            print("Sorry, that account does not seem to exist.")        

    def withdraw(self):
        """ Take an account number and amount as input and withdraw the specified amount from 
        the account. """
        account = self.get_account(int(input("Please enter your account number: ")))
        if account:
            amount = float(input("Please enter the amount you would like to withdraw: $"))
            if account.balance < amount:
                print("Sorry, insufficient funds.")
            else:
                account.balance -= amount                
                print(f"Thank you. ${amount:.2f} has been withdrawn.")
        else: 
            print("Sorry, that account does not seem to exist.")

    def transfer(self):
        """ Take two account numbers and an amount as input and transfer the 
            specified amount from one account to another """
        account_1 = self.get_account(int(input("Please enter the account number to transfer from: ")))
        account_2 = self.get_account(int(input("Please enter the account number to transfer to: ")))
        if account_1 and account_2:
            amount = float(input("Please enter the amount to transfer: $"))
            account_1.balance -= amount
            account_2.balance += amount
            print("\nTransfer successful!")
            print(f"${amount:.2f} was transfered from account number {account_1.account_number} to account number {account_2.account_number}.")
            print(f"Account number {account_1.account_number} now has a remaining balance of ${account_1.balance:.2f}.")
            print(f"Account number {account_2.account_number} now has a total balance of ${account_2.balance:.2f}.")
        else:
            if not account_1:
                print("Transfer failed: Initiating account not found")
            elif not account_2:
                print("Transfer failed: Receiving account not found")         


def execute_choice(new_client):
    """ Prompt the user for their choice and execute the corresponding operation """ 

    # dash = "-" * 37
    # print()
    # print("$", dash, "$")
    # print(f"  Hello, Teller. Let's continue.")
    # print("$", dash, "$")   
    
    print("\nChoose from the following options:\n")
    print("[1] Create Account")
    print("[2] Deposit Funds")
    print("[3] Withdraw Funds")
    print("[4] Check Balance")
    print("[5] Transfer Funds")
    print("[6] Get All Accounts")
    print("[7] Quit")
    
    try: 
        choice = int(input("\nPlease enter your choice (1-7): "))
        if choice == 1:
            new_client.create_account()                              
        elif choice == 2:
            print("Ok. Feed us money!")
            new_client.deposit()             
        elif choice == 3:
            print("Aww shucks you're taking our bucks!")
            new_client.withdraw()
        elif choice == 4:
            print("Let's check the equilibrium on your account!")
            new_client.get_account_balance()
        elif choice == 5:
            print("It's fun to transfer funds!")
            new_client.transfer()
        elif choice == 6:
            new_client.get_all_accounts()                
        elif choice == 7: 
            text = "Sorry to see you go, Teller 1. Have a great day!"
            dash_length = len(text)
            dash = "-" * dash_length
            print()
            print(f"${dash}$")
            print(f"{text.center(dash_length + 2)}")
            print(f"${dash}$")            
            exit()            
        else: 
            print("Please choose a valid option.")
    except ValueError:
        print("Sorry, invalid choice. Let's try again.") 

    continue_operation(new_client)                                     

def continue_operation(new_client):   

    lets_do_it = input("\nWould you like to continue with another operation (yes/no)?: ").strip().lower()
    while True:
        
        if lets_do_it == "no":
            text = "You have opted to log off. Goodbye, Teller 1!"
            dash_length = len(text)
            dash = "-" * dash_length
            print()
            print(f"${dash}$")
            print(f"{text.center(dash_length + 2)}")
            print(f"${dash}$")            
            exit()
        elif lets_do_it == "yes":
            text = "Excellent. Let's continue, Teller 1."
            dash_length = len(text)
            dash = "-" * dash_length
            print()
            print(f"${dash}$")
            print(f"{text.center(dash_length + 2)}")
            print(f"${dash}$")            
            execute_choice(new_client)
        else:
            print("Sorry, invalid response. Please try again.")
            lets_do_it = input("\nWould you like to continue with another operation (yes/no)?: ").strip().lower()

def main():
    text = "Hello, Teller 1. The Bank welcomes you."
    dash_length = len(text)
    dash = "-" * dash_length    
    print(f"\n${dash}$")
    print(f"{text.center(dash_length + 2)}")
    print(f"${dash}$")  

    new_client = Bank()
    execute_choice(new_client)
main()