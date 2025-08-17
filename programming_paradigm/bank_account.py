class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance 
    def deposit(self, amount):
        if amount > 0:
             self.account_balance += amount
        else:
            print("deposited amount should be positive")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"current balance is : ${self.account_balance}")


    