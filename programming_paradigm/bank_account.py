class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return False
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return False
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        # Must print exactly: "Current Balance: $<amount>"
        print(f"Current Balance: ${self._fmt(self.account_balance)}")

    @staticmethod
    def _fmt(x):
        # Print integers without .0; otherwise up to 2 decimals without trailing zeros
        x = float(x)
        if x.is_integer():
            return str(int(x))
        return f"{x:.2f}".rstrip('0').rstrip('.')



    