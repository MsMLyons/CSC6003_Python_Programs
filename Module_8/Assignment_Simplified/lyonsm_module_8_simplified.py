"""
File: lyonsm_module_8_simplified.py
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 8
Date Created: 2023-11-25
Date Updated: 2023-12-15

Description: Bank management system that allows for the creation of bank accounts,
as well as transactions such as deposits, withdrawals, and transfers. The program
will also retrieve account details. Additionally, this program uses a while loop 
to call the menu of possible actions by a presumed bank teller, Teller 1.
"""
import datetime as datetime
import random

class BankAccount:
    """ Class to assign an account number and balance to an account """
    
    def __init__(self, account_number=None, balance=0.0):               
        self.account_number = int(account_number)
        self.balance = float(balance)             

class Bank():
    """ Class to create an account with an initial balance input by the user,
    assigned to a unique account number, as well as to implement methods of
    depositing, withdrawing, checking balance, and displaying account details.     
    """

    def __init__(self, initial_deposit=0.0):
        self.account_numbers = set()
        self.account_objects = {}
        self.initial_deposit = initial_deposit               

    def create_account(self):
        """ Method to take an account number as input and return the corresponding 
            BankAccount object from the list of accounts """ 
                        
        initial_deposit = float(input("\nHow much would you like to deposit? $"))        
        
        while True: 
            account_number = random.randint(1000000, 100000000)
            if account_number not in self.account_objects:
                self.account_numbers.add(account_number)                
                new_account = BankAccount(account_number, initial_deposit)
                self.account_objects[account_number] = new_account               
                time_of_creation = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
                print(f"\nAccount number {account_number} created successfully on {time_of_creation}.")
                print(f"\nInitial balance: ${initial_deposit:.2f}")
                continue_message()            
            return new_account               

    def get_account(self, account_number):
        """ Helper method to return an account number for use in other methods """ 

        if account_number in self.account_objects:
            return self.account_objects[account_number]
        else: 
            return False
    
    def get_all_accounts(self):
        """ Method to generate a list of all accounts and their corresponding balances """

        if len(self.account_objects) == 0:
            print("\nSorry, there are no existing accounts at this time.")
            text = "Let's add some accounts to the bank, Teller 1."
            dash_length = len(text)
            dash = "-" * dash_length    
            print(f"\n${dash}$")
            print(f"{text.center(dash_length + 2)}")
            print(f"${dash}$")
        else:
            print("\nHere's the list of all of the accounts with their corresponding balances:")
            for account_number, account_object in self.account_objects.items():
                print(f"\nAccount number: {account_number}, Balance: {account_object.balance:.2f}")                          
            continue_message()        

    def get_account_balance(self):
        """ Method to take an account number as input and verify the current balance """

        account_number = int(input("\nTo check a balance, please enter the account number: "))
        if account_number in self.account_objects:            
            print(f"\nAccount number {account_number} has a balance of ${self.account_objects[account_number].balance:.2f}")
            continue_message()
        else:
            print("\nSorry, that account number does not exist.")
            encouragement_message()     
    
    def deposit(self):
        """ Method to take an account number and amount as input and deposit the specified 
            amount into the specified account """
        
        account = self.get_account(int(input("\nPlease enter your account number: ")))        
        if account:
            amount = float(input("\nPlease enter the amount you would like to deposit: $")) 
            account.balance += amount
            time_of_deposit = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M:%S")                      
            print(f"\nThank you. Deposit of ${amount:.2f} received on {time_of_deposit}.")
            print(f"\nAccount number {account.account_number} has a new balance of ${account.balance:.2f}.")
            continue_message()
        else: 
            print("\nSorry, that account number does not exist.")
            encouragement_message()        

    def withdraw(self):
        """ Method to take an account number and amount as input and withdraw the specified 
            amount from the specified account. """

        account = self.get_account(int(input("\nPlease enter your account number: ")))
        if account:
            amount = float(input("\nPlease enter the amount you would like to withdraw: $"))
            if account.balance < amount:
                print("\nSorry, insufficient funds.")
                encouragement_message()
            else:
                account.balance -= amount
                time_of_withdrawal = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
                print(f"\nThank you. ${amount:.2f} has been withdrawn on: {time_of_withdrawal}.")
                print(f"\nAccount number {account.account_number} has a remaining balance of ${account.balance:.2f}.")
                continue_message()
        else: 
            print("\nSorry, that account number does not exist.")
            encouragement_message()

    def transfer(self):
        """ Method to take two account numbers and an amount as input and transfer the 
            specified amount from one account to another """
        
        account_1 = self.get_account(int(input("\nPlease enter the account number to transfer from: ")))
        account_2 = self.get_account(int(input("\nPlease enter the account number to transfer to: ")))
        if account_1 and account_2:
            amount = float(input("\nPlease enter the amount to transfer: $"))
            if account_1.balance < amount:
                print("\nSorry, insufficient funds to complete the transfer.")
                encouragement_message()
            else:
                account_1.balance -= amount
                account_2.balance += amount
                time_of_transfer = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
                print("\nTransfer successful!")
                print(f"\n${amount:.2f} was transfered from account number {account_1.account_number} to account number {account_2.account_number} on {time_of_transfer}.")
                print(f"\nAccount number {account_1.account_number} now has a remaining balance of ${account_1.balance:.2f}.")
                print(f"\nAccount number {account_2.account_number} now has a total balance of ${account_2.balance:.2f}.")
                continue_message()
        else:
            if not account_1 and not account_2:
                print("\nSorry, neither of those accounts exist in the database.")
            elif not account_1:
                print("\nSorry, transfer failed: Initiating account not found.")
            elif not account_2:
                print("\nSorry, transfer failed: Receiving account not found.")
            encouragement_message()         

def continue_message():
    """ Function that prints a message to the teller, capitalistically 
        encouraging them to continue working """
    
    text = "Excellent. Let's continue, Teller 1."
    dash_length = len(text)
    dash = "-" * dash_length    
    print(f"\n${dash}$")
    print(f"{text.center(dash_length + 2)}")
    print(f"${dash}$")

def encouragement_message():
    """ Function that prints a message to the teller to encourage them
        to keep working when an action fails """
    
    text = "Let's try something else, Teller 1."
    dash_length = len(text)
    dash = "-" * dash_length    
    print(f"\n${dash}$")
    print(f"{text.center(dash_length + 2)}")
    print(f"${dash}$")

def execute_choice(new_client):
    """ Function to prompt the user for their choice and execute the 
        corresponding operation """    
    
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
            choice = int(input("\nPlease enter your choice (1-7): "))
            if choice == 1:
                new_client.create_account()                                              
            elif choice == 2:
                print("\nOk. Feed us money!")
                new_client.deposit()                             
            elif choice == 3:
                print("\nAww shucks you're taking our bucks!")
                new_client.withdraw()                
            elif choice == 4:
                print("\nLet's check the equilibrium on your account!")
                new_client.get_account_balance()                
            elif choice == 5:
                print("\nIt's fun to transfer funds!")
                new_client.transfer()                
            elif choice == 6:
                print("\nListing accounts is a worthy endeavor!")
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
                print("\nSorry, that is not a valid option.")
                encouragement_message()     
        except ValueError:
            print("\nSorry, that's not a valid choice.")
            encouragement_message()                                     

def main():
    """ Main function to run the program """

    new_client = Bank()
    text = "Hello, Teller 1. The Bank welcomes you."
    dash_length = len(text)
    dash = "-" * dash_length    
    print(f"\n${dash}$")
    print(f"{text.center(dash_length + 2)}")
    print(f"${dash}$")
    execute_choice(new_client)
main()