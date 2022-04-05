class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if(BankAccount.can_withdraw(self.balance, amount)):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.balance += (self.balance * self.int_rate)
        return self
    
    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - 5 < amount):
            return False
        else:
            return True
    @staticmethod
    def is_positive(balance):
        if(balance > 0):
            return True
        else:
            return False
    @classmethod
    def print_all_instances(cls):
        for account in cls.all_accounts:
            print(f"Interest Rate - {account.int_rate}, Balance - {account.balance}")
# Accounts
tony = BankAccount()
zac = BankAccount(balance = 200) # Initial with a balance of 200

# Display the amount started with.
print("Initial")
tony.display_account_info()
zac.display_account_info()

# 1st Account
print("1st Account")
tony.deposit(300).deposit(200).deposit(1).withdraw(600).display_account_info()

# 2nd Account
print("2nd Account")
zac.deposit(200).deposit(100).withdraw(30).withdraw(20).withdraw(100).withdraw(30).yield_interest().display_account_info()

# BONUS
print("BONUS")
BankAccount.print_all_instances()
