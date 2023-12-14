class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else: print("Insufficient funds")

    def get_balance(self):
        return self.balance
    
my_account = BankAccount("123456789", 450)
my_account.deposit(500)
my_account.withdraw(30)
print(my_account.get_balance())

# output --> 920 from ((450 + 500) - 30)



# def display_account_details(self):
    #     print(f"Your account number is {self.account_number}")
    #     print(f"The balance for your account is ${self.balance}")
    #     # more details?
    #     pass 