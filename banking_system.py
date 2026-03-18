class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    def show_account_details(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
class SavingsAccount(BankAccount):
    def __init__(self, account_holder_name, account_number, balance, interest_rate):
        super().__init__(account_holder_name, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest earned: {interest}")
class CurrentAccount(BankAccount):
    def __init__(self, account_holder_name, account_number, balance, overdraft_limit):
        super().__init__(account_holder_name, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")   

# Example usage
savings_account = SavingsAccount("Alice", "SA123", 1000, 5)
savings_account.show_account_details()  
savings_account.deposit(500)
savings_account.calculate_interest()
current_account = CurrentAccount("Bob", "CA456", 500, 200)
current_account.show_account_details()  
current_account.withdraw(600)
current_account.withdraw(200) 