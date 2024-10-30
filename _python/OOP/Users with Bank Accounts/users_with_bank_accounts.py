class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
        self.accounts.append(BankAccount(int_rate=0.02, balance=0))
    def add_account(self):
        self.accounts.append(BankAccount(int_rate=0.02, balance=0))
    def get_account(self, index=0):
        if index < len(self.accounts):
            return self.accounts[index]
        else:
            print("Account not found.")
            return None

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate

    def transfer_money(self, other_account, amount):
        self.balance -= amount
        other_account.balance += amount
        return self

omar = User("Omar", "omar@axsos.academy")
jalal = User("Jalal", "jalal@axsos.academy")

omar.add_account()
jalal.add_account()

omar.get_account(0).deposit(300).deposit(3000).deposit(50).withdraw(1000).yield_interest().display_account_info()
omar.get_account(1).deposit(5000).withdraw(1000).yield_interest().display_account_info()

omar.get_account(0).transfer_money(jalal.get_account(0), 1000)

jalal.get_account(0).deposit(5000).deposit(10000).withdraw(500).withdraw(2000).withdraw(20).withdraw(50).yield_interest().display_account_info()
jalal.get_account(1).deposit(3000).withdraw(2000).yield_interest().display_account_info()