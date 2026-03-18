# Banking System - Python OOPs
# Author: B. Sriram

class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Rs.{amount} deposited successfully.")
            print(f"New Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
            print(f"Current Balance: Rs.{self.balance}")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
            print(f"Remaining Balance: Rs.{self.balance}")

    def check_balance(self):
        print(f"Current Balance: Rs.{self.balance}")

    def show_details(self):
        print("---- Account Details ----")
        print(f"Account Holder : {self.account_holder_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : Rs.{self.balance}")
        print("-------------------------")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder_name, account_number, balance=0, interest_rate=4):
        super().__init__(account_holder_name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest of {self.interest_rate}% added: Rs.{interest}")
        print(f"New Balance after interest: Rs.{self.balance}")

    def show_details(self):
        super().show_details()
        print(f"Account Type   : Savings Account")
        print(f"Interest Rate  : {self.interest_rate}%")
        print("-------------------------")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder_name, account_number, balance=0, overdraft_limit=10000):
        super().__init__(account_holder_name, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance + self.overdraft_limit:
            print("Exceeds overdraft limit!")
            print(f"Maximum you can withdraw: Rs.{self.balance + self.overdraft_limit}")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
            print(f"Remaining Balance: Rs.{self.balance}")
            if self.balance < 0:
                print(f"Warning: You are using overdraft! Overdraft used: Rs.{abs(self.balance)}")

    def show_details(self):
        super().show_details()
        print(f"Account Type   : Current Account")
        print(f"Overdraft Limit: Rs.{self.overdraft_limit}")
        print("-------------------------")


# Main Program
print("========== BANKING SYSTEM ==========\n")

# Creating SavingsAccount object
savings = SavingsAccount("B. Sriram", "SAV001", 5000, 4)
savings.show_details()

print("\n-- Savings Account Operations --")
savings.deposit(3000)
savings.withdraw(1000)
savings.add_interest()
savings.check_balance()

print("\n")

# Creating CurrentAccount object
current = CurrentAccount("B. Sriram", "CUR001", 2000, 10000)
current.show_details()

print("\n-- Current Account Operations --")
current.deposit(5000)
current.withdraw(3000)
current.withdraw(15000)
current.check_balance()

print("\n========== FINAL BALANCES ==========")
print(f"Savings Account Balance : Rs.{savings.balance}")
print(f"Current Account Balance : Rs.{current.balance}")
print("=====================================")