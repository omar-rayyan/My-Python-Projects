class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

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

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.account.balance += amount
        return self

omar = User("Omar", "omar@axsos.academy")
jalal = User("Jalal", "jalal@axsos.academy")

omar.account.deposit(300).deposit(3000).deposit(50).withdraw(1000).yield_interest().display_account_info()
jalal.account.deposit(5000).deposit(10000).withdraw(500).withdraw(2000).withdraw(20).withdraw(50).yield_interest().display_account_info()