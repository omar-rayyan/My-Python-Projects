class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

omar = User("Omar", "omar@axsos.academy")
jalal = User("Jalal", "jalal@axsos.academy")
ameed = User("Ameed", "ameed@axsos.academy")

omar.make_deposit(300)
omar.make_deposit(3000)
omar.make_deposit(50)
omar.make_withdrawal(1000)
omar.display_user_balance()

jalal.make_deposit(1000)
jalal.make_deposit(500)
jalal.make_withdrawal(80)
jalal.make_withdrawal(50)
jalal.display_user_balance()

ameed.make_deposit(10000)
ameed.make_withdrawal(500)
ameed.make_withdrawal(100)
ameed.make_withdrawal(20)
ameed.display_user_balance()

omar.transfer_money(ameed, 1200)
ameed.display_user_balance()
omar.display_user_balance()