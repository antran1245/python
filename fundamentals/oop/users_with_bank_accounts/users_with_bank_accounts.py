class User:
    def __init__(self, name, email, numAccount = 1):
        self.name = name
        self.email = email
        self.all_accounts = []
        for num in range(numAccount):
            self.all_accounts.append(BankAccount(int_rate = 0.01, balance = 0))
            
    def make_deposit(self, amount, thisBankAccount = 0):
        if(thisBankAccount > len(self.all_accounts)):
            thisBankAccount = 0
            print("Outside the number of account you created. No deposit of", amount )
        self.all_accounts[thisBankAccount].deposit(amount)
        return self
    def make_withdrawal(self, amount, thisBankAccount = 0):
        if(thisBankAccount > len(self.all_accounts)):
            thisBankAccount = 0
            print("Outside the number of account you created. No withdraw of", amount)
        self.all_accounts[thisBankAccount].withdraw(amount)
        return self
    def display_user_balance(self, thisBankAccount = 0):
        print(f"User: {self.name}, Account: {thisBankAccount}, {self.all_accounts[thisBankAccount].display_account_info()}")
        return self
    def transfer_money(self, amount, other, thisBankAccount = 0,  otherBankAccount = 0):
        if(self.all_accounts[thisBankAccount].can_withdraw(self.all_accounts[thisBankAccount].balance, amount)):
            
            print(f"A {thisBankAccount} ", self.all_accounts[thisBankAccount].balance)
            self.all_accounts[thisBankAccount].withdraw(amount)
            print(f"B {thisBankAccount} ", self.all_accounts[thisBankAccount].balance)
            
            other.all_accounts[otherBankAccount].deposit(amount)
            print(f"First User: {self.name}, {self.all_accounts[thisBankAccount].display_account_info()}")
            print(f"Second User: {other.name}, {other.all_accounts[otherBankAccount].display_account_info()}")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.all_accounts[thisBankAccount].balance -= 5
        return self

class BankAccount:
    # don't forget to add some default values for these parameters!
    
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
        return f"Balance: ${self.balance}"
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
            
# User(name, email, number of bank account)
tony = User("tony", "tony@gmail.com", 2)

# Deposits
tony.make_deposit(200)
tony.make_deposit(210,1)
tony.make_deposit(320,3)

# Withdraw
tony.make_withdrawal(200,1)
tony.make_withdrawal(40)

# Transfer
zac = User("zac", "zac@gmail.com")
tony.transfer_money(100, zac)
