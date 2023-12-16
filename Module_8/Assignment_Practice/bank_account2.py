import datetime as datetime
import random

class BankAccount:
    """ Class to assign an account number and to implement methods of
    depositing, withdrawing, checking balance, and displaying account 
    details
    """

    def __init__(self, account_number=None, balance=0.0):               
        self.account_number = int(account_number)
        self.balance = float(balance)             

class Bank():
    """ Class to create an account with an initial balance input by the user,
    assigned to a unique account number, as well as allow for transactions.     
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
                time_of_creation = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"\nAccount number {account_number} created successfully on {time_of_creation}.")
                print(f"\nInitial balance: ${initial_deposit:.2f}")                            
            return new_account
                
    def get_all_accounts(self):
        """ Method to generate a list of all accounts and their corresponding balances """
    
        if len(self.account_objects) == 0:
            print("\nSorry, there are no existing accounts at this time.")            
        else:
            print("Here's the list of all of the accounts with their corresponding balances:\n")
            for account_number, account_object in self.account_objects.items():
                print(f"Account number: {account_number}, Balance: {account_object.balance:.2f}")                 
            
    def get_account(self, account_number):
        """ Helper method to return an account number for use in other methods """
        
        if account_number in self.account_objects:
            return self.account_objects[account_number]
        else: 
            return False

    def get_account_balance(self):
        """ Method to take an account number as input and verify the current balance """

        account_number = int(input("\nTo check a balance, please enter the account number: "))
        if account_number in self.account_objects:            
            print(f"\nAccount number {account_number} has a balance of ${self.account_objects[account_number].balance:.2f}")
        else:
            print("\nSorry, that account number does not exist.")                 
    
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
        else: 
            print("\nSorry, that account number does not exist.")                                                      

    def withdraw(self):
        """ Method to take an account number and amount as input and withdraw the specified 
            amount from the specified account. """
        
        account = self.get_account(int(input("\nPlease enter your account number: ")))
        if account:
            amount = float(input("\nPlease enter the amount you would like to withdraw: $"))
            if account.balance < amount:
                print("\nSorry, insufficient funds.")                
            else:
                account.balance -= amount
                time_of_withdrawal = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"\nThank you. ${amount:.2f} has been withdrawn on {time_of_withdrawal}.")
                print(f"\nAccount number {account.account_number} has a remaining balance of ${account.balance:.2f}.")                
        else: 
            print("\nSorry, that account number does not exist.")            

    def transfer(self):
        """ Method to take two account numbers and an amount as input and transfer the 
            specified amount from one account to another """
        
        account_1 = self.get_account(int(input("\nPlease enter the account number to transfer from: ")))
        account_2 = self.get_account(int(input("\nPlease enter the account number to transfer to: ")))
        if account_1 and account_2:
            amount = float(input("\nPlease enter the amount to transfer: $"))
            account_1.balance -= amount
            account_2.balance += amount
            time_of_transfer = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
            print("\nTransfer successful!")
            print(f"\n${amount:.2f} was transfered from account number {account_1.account_number} to account number {account_2.account_number} on {time_of_transfer}.")
            print(f"\nAccount number {account_1.account_number} now has a remaining balance of ${account_1.balance:.2f}.")
            print(f"\nAccount number {account_2.account_number} now has a total balance of ${account_2.balance:.2f}.")            
        else:
            if not account_1 and not account_2:
                print("\nSorry, neither of those accounts exist in the database.")
            elif not account_1:
                print("\nSorry, transfer failed: Initiating account not found.")
            elif not account_2:
                print("\nSorry, transfer failed: Receiving account not found.")

def execute_choice(new_client):
    """ Function to prompt the user for their choice and execute the corresponding operation """ 
    
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
            print("\nYou've chosen to make a deposit.")
            new_client.deposit()             
        elif choice == 3:
            print("\nYou've chosen to make a withdrawal.")
            new_client.withdraw()
        elif choice == 4:
            print("\nYou've chosen to check the balance on an account.")
            new_client.get_account_balance()
        elif choice == 5:
            print("\nYou've chosen to transfer funds.")
            new_client.transfer()
        elif choice == 6:
            print("\nYou've chosen to see a list of all accounts.")
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
    except ValueError:
        print("\nSorry, that's not a valid choice.")        

    continue_operation(new_client)

def prompt_teller():
    """ Function to stylize message to prompt the teller """

    teller_prompt_text = "Teller 1, would you like to continue with another operation?"
    dash_length = len(teller_prompt_text)
    dash = "-" * dash_length    
    print(f"\n${dash}$")
    print(f"{teller_prompt_text.center(dash_length + 2)}")    
    print(f"${dash}$")                                         

def continue_operation(new_client):   
    """ Function to give the user a choice to continue or quit; this function drives 
        the execute_choice function """

    prompt_teller()
    teller_prompt = input("\nPlease enter yes or no: ").strip().lower()    
    
    while True:   
        if teller_prompt == "no":
            text = "You have opted to log off. Goodbye, Teller 1!"
            dash_length = len(text)
            dash = "-" * dash_length
            print()
            print(f"\n${dash}$")
            print(f"{text.center(dash_length + 2)}")
            print(f"${dash}$")            
            exit()
        elif teller_prompt == "yes":                      
            execute_choice(new_client)
        else:
            print("\nSorry, that's not a valid choice.")            
            prompt_teller()
            teller_prompt = input("\nPlease enter yes or no: ").strip().lower()            

def main():
    """ Main function to run the program """

    text = "Hello, Teller 1. The Bank welcomes you."
    dash_length = len(text)
    dash = "-" * dash_length    
    print(f"\n${dash}$")
    print(f"{text.center(dash_length + 2)}")
    print(f"${dash}$")  

    new_client = Bank()
    execute_choice(new_client)
main()