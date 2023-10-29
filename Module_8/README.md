Final Project: Bank Account Management

Assignment Instructions: You have been assigned the task of creating a bank account management system. The system should allow users to create bank accounts, deposit funds, withdraw funds, check the account balance, and perform transfers between accounts. Implement the program using object-oriented programming, lists, dictionaries, and recursion.

Instructions:

Create a BankAccount class with the following attributes:

account_number (integer): The account number assigned to the bank account.
balance (float): The current balance of the bank account. Implement methods for depositing, withdrawing, checking balance, and displaying the account details.
Create a Bank class that manages a list of bank accounts. Implement the following methods:

create_account: Prompts the user to enter an initial balance and creates a new bank account with a unique account number.
get_account: Takes an account number as input and returns the corresponding BankAccount object from the list of accounts.
deposit: Takes an account number and amount as input and deposits the specified amount into the account.
withdraw: Takes an account number and amount as input and withdraws the specified amount from the account.
transfer: Takes two account numbers and an amount as input and transfers the specified amount from one account to another.
Create a menu function that displays the available operations to the user:

Create Account
Deposit
Withdraw
Check Balance
Transfer
Quit
Implement an execute_choice function that prompts the user for their choice and executes the corresponding operation.

Implement a recursive function continue_operation that asks the user if they want to continue performing operations after each operation. If the user chooses to continue, the function should call execute_choice again; otherwise, it should exit the program.