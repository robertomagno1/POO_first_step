from datetime import datetime

class SavingsAccount:

    def __init__(self, account_rate):
        self.balance = 0.0
        self.rate = account_rate
        self.operations = []
    def deposit(self, amount):
        self.balance+= amount
        new_operation = (datetime.now(), amount)
        self.operations.append(new_operation)

    def withdraw(self, amount):
        self.balance-= amount
        new_operation = (datetime.now(), -amount)
        self.operations.append(new_operation)

    def compute_interest(self):
        interest = self.balance * self.rate/100
        self.deposit(interest)

    def print_operation_list(self):
        print("List of operations")
        for t in self.operations:
            print("Time:", t[0], "\tAmount:", t[1])

    def print_current_balance(self):
        print("Current balance:", self.balance)


"""-------Entry point-------"""

my_account = SavingsAccount(4)
my_account.print_current_balance()
my_account.deposit(100)
my_account.print_current_balance()
my_account.deposit(300)
my_account.print_current_balance()
my_account.withdraw(50)
my_account.print_current_balance()
my_account.compute_interest()
my_account.print_current_balance()
my_account.print_operation_list()
print("Bye bye!")

