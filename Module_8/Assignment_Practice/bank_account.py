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

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = int(account_number)
        self.balance = float(balance)

    def deposit(self):
        # ask for value of deposit
        # date/time stamp
        pass

    def withdraw(self, balance, withdrawal_value):        
        new_balance = balance - withdrawal_value        
        print(f"Withdrawal in ammount of ${withdrawal_value}")
        print(f"Updated balance: ${new_balance}")
        # ask for value of withdrawal
        # date/time stamp
        pass

    def check_balance(self):
        # pull value in account
        # date/time stamp
        pass

    def display_account_details(self):
        print(f"Your account number is {self.account_number}")
        print(f"The balance for your account is ${self.balance}")
        # more details?
        
new_account = BankAccount(account_number=123456, balance=78.25)
new_account.display_account_details()
new_account.withdraw(balance=78.25, withdrawal_value=15.00)

# output -->
    # Your account number is 123456
    # The balance for your account is $78.25
    # Withdrawal in ammount of $15.0
    # Updated balance: $63.25