class Account:
    def __init__(self, account_number, holder_name, opening_balance, account_type):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = opening_balance
        self.account_type = account_type

    def deposit(self, amount):
        print(f"Depositing ${amount:.2f}")
        self.balance += amount

    def withdraw(self, amount):
        print(f"Withdrawing ${amount:.2f}")
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(f"Balance: ${self.balance:.2f}")
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.holder_name}, Account Type: {self.account_type}, Account Balance: {self.balance:.2f}"


class CurrentAccount(Account):
    def __init__(
        self,
        account_number,
        holder_name,
        opening_balance,
        account_type,
        overdraft_limit,
    ):
        super().__init__(account_number, holder_name, opening_balance, account_type)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        print(f"Withdrawing ${amount:.2f}")
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            print("Withdrawal denied: Exceeds overdraft limit")


account1 = Account("123", "John", 10.05, "current")
account2 = Account("345", "John", 23.55, "savings")
account3 = Account("567", "Phoebe", 12.45, "investment")

print(account1)
print(account2)
print(account3)

print()

account1.deposit(23.45)
account1.withdraw(12.33)
account1.get_balance()

print()
current_account = CurrentAccount("789", "Alex", 50.00, "current", 100.00)
print(current_account)
current_account.withdraw(120)
print("Balance after withdrawal:", current_account.get_balance())
current_account.withdraw(50)
print("Balance after withdrawal:", current_account.get_balance())
