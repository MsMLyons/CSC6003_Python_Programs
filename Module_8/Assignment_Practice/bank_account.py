""" You have been assigned the task of creating 
a bank account management system. The system 
should allow users to create bank accounts, 
deposit funds, withdraw funds, check the account 
balance, and perform transfers between accounts. 
Implement the program using object-oriented 
programming, lists, dictionaries, and recursion.

Create a BankAccount class with the following attributes:

account_number (integer): The account number assigned to 
the bank account.
balance (float): The current balance of the bank account. 
Implement methods for depositing, withdrawing, checking 
balance, and displaying the account details.
"""
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

    def __init__(self, new_balance=0.0):
        self.account_numbers = set()
        self.account_objects = {}
        self.new_balance = new_balance # created due to attribute error               

    # create_account: Prompts the user to enter an initial balance and creates a new bank account 
    # with a unique account number.
    def create_account(self):
        """ Take an account number as input and return the corresponding 
            BankAccount object from the list of accounts """ 
                        
        new_balance = float(input("How much would you like to deposit? $"))        
        
        while True: 
            account_number = random.randint(1000000, 100000000)
            if account_number not in self.account_objects:
                self.account_numbers.add(account_number)
                new_account = BankAccount(account_number, new_balance)
                self.account_objects[account_number] = new_account               
                
                print(f"\nAccount number {account_number} created successfully")
                print(f"Balance: ${new_balance:.2f}")
            # unit testing?
            return new_account
        
    # added to view set of accounts created (not in assignment instructions)        
    def get_all_accounts(self):
        all_accounts = self.account_numbers
        print("Here is a list of all of the accounts:", *all_accounts, sep = "\n")
        # print(f"These are the account objects: {self.account_objects}")                  
    
    def get_account(self, account_number):
        # account_number = int(input("Please enter your account number: "))
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
            # timestamp = datetime.now()
            # time_of_deposit = timestamp.strftime("%d/%m/%Y %H:%M:%S")
            # print(f"Thank you. ${amount} was deposited on: {time_of_deposit}")
            print(f"Thank you. Deposit of ${amount:.2f} received.")
            
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
                # timestamp = datetime.now()
                # time_of_withdrawal = timestamp.strftime("%d/%m/%Y %H:%M:%S")
                # print(f"Thank you. ${amount} was withdrawn on: {time_of_withdrawal}")
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
            print(f"${amount:.2f} was transfered from {account_1} to {account_2}.")
            print(f"Account {account_1} now has a remaining balance of ${account_1.balance}.")
            print(f"Account {account_2} now has a total balance of ${account_2.balance}.")
            # timestamp = datetime.now()
            # time_of_transfer = timestamp.strftime("%d/%m/%Y %H:%M:%S")
        else:
            if not account_1:
                print("Transfer failed: Initiating account not found")
            elif not account_2:
                print("Transfer failed: Receiving account not found")         


def execute_choice():
    """ Prompt the user for their choice and execute the corresponding operation """
    new_client = Bank()
    dash = "-" * 37
    print()
    print("$", dash, "$")
    print(f"  Hello, Teller. The Bank welcomes you.")
    print("$", dash, "$")
    
    while True:
        print("\nChoose from the following options:\n")
        print("[1] Create Account")
        print("[2] Deposit Funds")
        print("[3] Withdraw Funds")
        print("[4] Check Balance")
        print("[5] Transfer Funds")
        print("[6] Get All Accounts")
        print("[7] Quit")
        
        try: 
            choice = int(input("\nPlease enter your choice (1-6): "))
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
                print("Sorry to see you go. Have a great day!")
                exit()            
            else: 
                print("Please choose a valid option.")
        except ValueError:
            print("Sorry, invalid choice. Let's try again.")
                                            
execute_choice()